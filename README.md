<div align="center">

# 📚 Book-to-Project

### 把书里的一个想法，变成一个能试、能检查的小项目。

Turn an idea from a book or document into a small project you can use and evaluate.

![Type](https://img.shields.io/badge/type-AI%20Skill-7257d5)
![Input](https://img.shields.io/badge/input-book%20%2F%20document-3478c8)
![Output](https://img.shields.io/badge/output-artifact%20%2B%20real%20test-159578)

[为什么需要它](#为什么需要它) · [它会产出什么](#它会产出什么) · [怎么使用](#怎么使用) · [工作流程](#工作流程) · [示例](#示例) · [限制与隐私](#限制与隐私)

</div>

---

## 一句话介绍

Book-to-Project 帮你从一本书或一份长文档里找到与当前目标相关的观点，把它变成一件可编辑、可使用的成果，并设计真实的检查方式。

**书里的观点 → 你的问题 → 一个小成果 → 实际验证 → 下一轮调整**

它不只整理“书里说了什么”，还会和你一起回答：**“我能用这个想法做出什么？怎么知道它对我有没有用？”**

## 为什么需要它

读书时划线、记笔记、听 AI 总结都能帮助理解，但读完之后，常常还是不知道怎样把知识用到自己的工作、学习或生活里。

Book-to-Project 把“理解”往前推一步：挑出一个相关观点，连接到一个具体问题，做出一个小成果，再用实际观察决定下一步。

|  | book-to-skill | Book-to-Project |
| --- | --- | --- |
| 主要目标 | 把书整理成 AI 可按需调用的知识 | 把书里的观点应用到一个现实目标 |
| 常见产出 | 章节摘要、框架、参考资料 | 可编辑成果、来源依据、验证计划 |
| 核心问题 | “这本书讲了什么？” | “我能用它做什么，怎么检查结果？” |

Book-to-Project 受到 [book-to-skill](https://github.com/virgiliojr94/book-to-skill) 的启发，是独立 Skill，并非该项目的官方扩展。

## 它会产出什么

根据目标，产出可以是：

- 一张学习卡或练习材料
- 一份决策备忘录
- 一个页面草稿或工作流原型
- 一个小型实践实验及记录表

每个成果都尽量说明：哪些是书中观点，哪些是项目设计选择，哪些仍是假设，以及实际观察到了什么。

## 怎么使用

将仓库下载并放入你使用的 AI 工具所支持的 Skill 目录，然后提供一本书、文档或节选，并说清你现在想解决的问题。

可以这样提问：

```text
Use book-to-project with this book and my current goal.
Help me make one small artifact I can actually use.
Show which ideas come from the source, and how I can test the result.
```

支持的文本来源包括 PDF、EPUB、DOCX、Markdown、TXT 或用户提供的节选。仓库还提供文本提取脚本；PDF 提取需要安装 `pdftotext`。

## 工作流程

1. **找到相关观点**：标出来源位置、适用条件和注意事项。
2. **界定现实问题**：分清已知事实、用户提供的信息和待确认的假设。
3. **选一个小成果**：范围要小到可以开始做，不停留在宏大路线图。
4. **保留推理依据**：记录“书中观点 → 项目判断 → 设计选择 → 验证方式”。
5. **实际检查并调整**：有真实观察就记录；还没执行就明确标为“待验证”。

## 示例：把《原子习惯》变成晚间阅读实验

**问题：**晚饭后容易拿起手机，一晚上过去了，却没有开始读书。

**项目草案：**把书放到显眼的位置；收拾完晚餐后先读一页；记录当天是否开始，并在第 7 天根据遇到的阻碍调整环境。

**怎么检查：**第 14 天查看实际记录，比较哪些安排更容易重复。这个两周安排是项目设计示例，不是书中规定的时间表，也不代表习惯已经养成。

## 限制与隐私

- 生成计划不等于验证有效；结果需要实际使用和观察。
- 提取脚本适合文本为主的文件；扫描版页面、复杂表格、图片和代码需要额外检查。
- EPUB 的定位是文件内部位置，不一定对应纸书页码。
- 只处理你有权使用的材料。不要把整本书、提取出的原文、私人记录或凭据提交到公开仓库。
- 当前仓库尚未指定开源许可证；公开可见不等于已明确授权他人复制、修改或再发布。

## 仓库内容

| 文件 | 用途 |
| --- | --- |
| [`SKILL.md`](SKILL.md) | Skill 工作流程与输出规则 |
| [`references/project-card.md`](references/project-card.md) | 项目与证据记录模板 |
| [`scripts/extract_source.py`](scripts/extract_source.py) | 为 EPUB、PDF、DOCX、Markdown、TXT 提取文本片段和来源定位 |
| [`agents/openai.yaml`](agents/openai.yaml) | Skill 展示信息 |

---

Inspired by the idea of making book knowledge usable in AI workflows. Book-to-Project focuses on creating a scoped artifact and checking it against real observations.
