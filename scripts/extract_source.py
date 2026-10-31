#!/usr/bin/env python3
"""Text-heavy book extraction with source locators; not an OCR/diagram parser."""
import argparse
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import subprocess
import sys
import zipfile
from xml.etree import ElementTree as ET

MAX_SOURCE = 100 * 1024 * 1024
MAX_MEMBER = 15 * 1024 * 1024
MAX_TOTAL = 80 * 1024 * 1024


class TextHTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts, self.skip = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1
        elif tag in ("p", "div", "h1", "h2", "h3", "h4", "li", "br"):
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip = max(0, self.skip - 1)
        elif tag in ("p", "div", "li", "h1", "h2", "h3", "h4"):
            self.parts.append("\n")

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)

    def text(self):
        t = "".join(self.parts).replace("\xa0", " ")
        return re.sub(r"\n{3,}", "\n\n", t).strip()


def safe_members(z):
    total = 0
    for item in z.infolist():
        total += item.file_size
        if item.file_size > MAX_MEMBER or total > MAX_TOTAL:
            raise ValueError("Archive member or uncompressed total exceeds the extraction limit")


def epub_segments(path):
    with zipfile.ZipFile(path) as z:
        safe_members(z)
        container = ET.fromstring(z.read("META-INF/container.xml"))
        opf = container.find(".//{*}rootfile").attrib["full-path"]
        root = ET.fromstring(z.read(opf))
        base = str(Path(opf).parent)
        manifest = {x.attrib["id"]: x.attrib.get("href", "") for x in root.findall(".//{*}manifest/{*}item")}
        from urllib.parse import unquote
        from posixpath import normpath, join
        for item in root.findall(".//{*}spine/{*}itemref"):
            href = manifest.get(item.attrib.get("idref", ""), "")
            if not href or not href.lower().split("#")[0].endswith((".html", ".htm", ".xhtml")):
                continue
            member = normpath(join(base, unquote(href.split("#")[0])))
            if member.startswith("../") or member not in z.namelist():
                continue
            parser = TextHTML()
            parser.feed(z.read(member).decode("utf-8-sig", errors="replace"))
            if parser.text():
                yield member, parser.text()


def docx_segments(path):
    with zipfile.ZipFile(path) as z:
        safe_members(z)
        root = ET.fromstring(z.read("word/document.xml"))
        for i, para in enumerate(root.findall(".//{*}p"), 1):
            text = "".join(n.text or "" for n in para.findall(".//{*}t")).strip()
            if text:
                yield f"paragraph:{i}", text


def source_segments(path):
    suffix = path.suffix.lower()
    if suffix == ".epub":
        yield from epub_segments(path)
    elif suffix == ".docx":
        yield from docx_segments(path)
    elif suffix == ".pdf":
        try:
            result = subprocess.run(["pdftotext", "-layout", str(path), "-"], capture_output=True, check=True)
        except (FileNotFoundError, subprocess.CalledProcessError) as e:
            raise ValueError("PDF text extraction needs a working pdftotext; scanned pages require OCR") from e
        for i, page in enumerate(result.stdout.decode("utf-8", errors="replace").split("\f"), 1):
            if page.strip():
                yield f"pdf-page:{i} (extracted page order)", page.strip()
    elif suffix in (".txt", ".md", ".markdown"):
        yield "whole-file", path.read_text(encoding="utf-8-sig", errors="replace")
    else:
        raise ValueError(f"Unsupported suffix: {suffix}")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("source", type=Path)
    p.add_argument("output_dir", type=Path)
    args = p.parse_args()
    if not args.source.is_file() or args.source.stat().st_size > MAX_SOURCE:
        p.error("Source missing or over 100 MB")
    if args.output_dir.exists() and any(args.output_dir.iterdir()):
        p.error("Output directory must be new or empty")
    segments = [(locator, content) for locator, content in source_segments(args.source) if content.strip()]
    if not segments:
        p.error("No readable text; check source structure or OCR")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    manifest = {"source_name": args.source.name, "source_sha256": hashlib.sha256(args.source.read_bytes()).hexdigest(),
                "format": args.source.suffix.lower(), "segments": [], "warning": "Text only; inspect tables, images and extraction order. Locators are source-specific, not necessarily printed pages."}
    for i, (locator, content) in enumerate(segments, 1):
        name = f"segment-{i:04d}.txt"
        (args.output_dir / name).write_text(content, encoding="utf-8")
        manifest["segments"].append({"file": name, "locator": locator, "characters": len(content)})
    (args.output_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"segments": len(segments), "characters": sum(len(x[1]) for x in segments), "output": str(args.output_dir)}, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, KeyError, zipfile.BadZipFile, ET.ParseError) as exc:
        print(f"Extraction failed: {exc}", file=sys.stderr)
        sys.exit(1)
