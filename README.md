# Book-to-Project

**A book can give you an idea. Book-to-Project helps you make something with it.**

Book-to-Project is an AI Skill that connects ideas from a book or document to a problem you are working on. It helps you choose a small project, create an editable artifact, trace important decisions back to the source, and define a real way to test the result.

The artifact might be a learning card, a decision memo, a page draft, a lesson, or a workflow prototype. The goal is to finish with something you can use and check.

> 一本书给你一个想法。Book-to-Project 帮你把它用到眼前的问题中，做出一件能检查的成果。

## Why

Reading often ends with highlights, notes, or a good answer from an AI assistant. Those can be useful, but they do not show whether an idea works in your situation.

Book-to-Project adds one more step: **use the idea to make something, then check what happened.**

| | book-to-skill | Book-to-Project |
| --- | --- | --- |
| Main job | Structure a book into knowledge an agent can load when needed | Connect a source idea to a current problem and a small project |
| Typical output | Frameworks, chapter files, reference aids | An editable artifact, source trace, test, and revision |
| Core question | “What does the book say, and how can I use it?” | “What can I make with this idea, and how will I check it?” |

The original [book-to-skill](https://github.com/virgiliojr94/book-to-skill) inspired this project. Book-to-Project is an independent Skill, not an official extension of that repository. It does not claim to improve learning or project outcomes without real testing.

## How it works

**Source idea → Your problem → Small artifact → Real test**

1. **Find the relevant idea.** Locate what the source says and note when it applies.
2. **Define the problem.** Identify the person, current friction, and desired change.
3. **Make one artifact.** Create a small editable result instead of stopping at advice.
4. **Keep the reasoning visible.** Separate source claims from project decisions and assumptions.
5. **Test and revise.** Record an actual observation, or clearly mark the test as pending.

The Skill uses the labels `[Book]`, `[User]`, `[Design]`, `[Hypothesis]`, and `[Observed]` so that a plausible draft is not mistaken for a tested result.

## What is included

| File | Purpose |
| --- | --- |
| [`SKILL.md`](SKILL.md) | Project workflow and answer rules |
| [`references/project-card.md`](references/project-card.md) | Compact artifact and evidence template |
| [`scripts/extract_source.py`](scripts/extract_source.py) | Text extraction with source locators for EPUB, PDF, DOCX, Markdown, and TXT |
| [`agents/openai.yaml`](agents/openai.yaml) | Skill display metadata |

## Use it

Place this folder in a skills directory supported by your AI agent, then ask:

```text
Use book-to-project with this document and my current problem.
Help me make one small artifact I can actually use, show which ideas
come from the source, and define how I can test the result.
```

For text-heavy documents, the bundled extractor can make local segments and a manifest:

```bash
python3 scripts/extract_source.py ./my-book.epub ../private-extract
```

Keep the source file and extracted text outside a public repository. Text-based PDFs require `pdftotext`; scanned PDFs need OCR through another tool.

## Example: turn a book into a 14-day reading experiment

**The user asks:**

> “I want to read every evening, but after dinner I pick up my phone and the evening disappears. Using *Atomic Habits*, help me design a two-week experiment. I don't want another list of tips—I want something I can actually try and evaluate.”

**What Book-to-Project makes:**

It uses the ideas of making a habit obvious, easy, and satisfying to build a project card for this situation. These ideas are described in [James Clear's public summary](https://jamesclear.com/atomic-habits-summary) and his [two-minute rule article](https://jamesclear.com/how-to-stop-procrastinating). The two-week duration and specific actions below are **project design choices**, not a timetable prescribed by the book.

| Part | Example project card |
| --- | --- |
| Problem | After dinner, opening the phone usually happens before opening a book. |
| Cue | Put the current book where it is visible before dinner. |
| Starting action | After clearing the dinner plate, sit down and read one page before opening an app. Reading more is optional. |
| Reduce friction | Choose the book and mark the next page in advance; keep the phone away from the reading spot. |
| Daily record | Mark whether reading started, how many pages were read, and what got in the way if it did not start. |
| Day 7 adjustment | Look at missed days. Change one obstacle, such as the book's location or the cue's timing, then continue. |
| Day 14 check | Compare planned opportunities with days reading actually began. Record which setup was easiest to repeat. |

**What the Skill does not claim:** The card is a draft experiment, not proof that a habit has formed. Book-to-Project cannot fill in the user's daily record or announce a result before the experiment happens. Afterward, the user can bring back the actual record to examine what worked, what failed, and what to test next.

**Book idea → Personal situation → Usable experiment card → Real observations → Next iteration**

This public example contains no uploaded book text, private reading history, or real user results.

## Limits and privacy

- Generating a plan or draft does not prove that an idea works. Outcomes require real use and observation.
- The extractor handles text-heavy files. Scanned pages, complex tables, diagrams, and code need additional inspection.
- EPUB locators are internal file positions, not printed page numbers.
- Use source materials you are authorized to access. Do not commit copyrighted full text, private source files, extracted text, personal records, or credentials to a public repository.

## Acknowledgment

Inspired by the idea of making books usable in AI workflows, including [book-to-skill](https://github.com/virgiliojr94/book-to-skill). Book-to-Project focuses on turning source ideas into scoped artifacts with a real-world check.
