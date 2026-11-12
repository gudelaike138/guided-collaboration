# Guided Collaboration

一个面向 Codex 的协作技能。它会根据任务复杂度调整解释的深度，让你在完成任务的同时，理解关键步骤、方案取舍和验证方法。

## 它怎么协作

- **简单问题**。先直接回答，需要时用通俗的例子解释。
- **小型实操**。完成任务后，简要说明改了什么、怎么验证。
- **复杂项目**。先讨论目标、交付物和关键选择。执行中说明重要改动的原因，交付时说明结果和验证情况。

你也可以在当次对话里指定节奏，例如「一步一步带我做」「先讨论方案」或「直接完成，最后告诉我怎么验证」。

## 在 Codex 中安装和调用

1. 在仓库首页选择 **Code → Download ZIP**，下载并解压。
2. 把包含 `SKILL.md` 的整个文件夹命名为 `guided-collaboration`，放到 `~/.agents/skills/`。Windows 上对应的位置是 `%USERPROFILE%\.agents\skills\guided-collaboration\`。
3. 在 Codex 新对话里输入 `$guided-collaboration`，后面跟上你的任务。

可以这样发起任务。

> 用 `$guided-collaboration` 带我把一个本地项目上传到 GitHub，顺便解释每一步的作用。

如果希望新对话默认采用这些协作习惯，可以把你想长期使用的规则追加到全局 `~/.codex/AGENTS.md`。

## 主要文件

- [SKILL.md](SKILL.md) 是 Codex 技能入口，包含完整协作流程。
- [中文通用规则](references/universal-rules.md) 可以复制到 DeepSeek 等其他 AI 助手中作为提示词。
