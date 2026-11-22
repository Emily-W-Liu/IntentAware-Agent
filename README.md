语言 / Language：**简体中文** | [English](README.en.md)

# IntentAware-Agent

**香港大学 COMP7607 自然语言处理 · 第 14 组**  
**项目名称：** An Agent with Intent Awareness for Task Continuity and Asynchronous Delegation  
**当前状态：** 项目规划与初始搭建中，功能尚未实现。

## 项目简介

本项目计划开发一款基于浏览器侧边栏的 AI 专注助手：理解用户的当前目标，结合任务上下文判断浏览行为，记录有价值的临时分心内容，并在用户返回主任务时提供具体的继续操作建议。用户还可以把支线问题委托给后台 Agent 处理，选择立即查看答案或等待预设的任务检查点再展示。

## 计划功能

1. **目标澄清与活动理解：** 确认用户目标及下一步行动，将当前活动分类为「直接进展」「必要准备」「可选探索」或「不确定」。拟使用的 API 标签为 `direct_progress`、`necessary_preparation`、`optional_exploration` 和 `unclear`。
2. **分心记录与任务恢复：** 保存链接和笔记、记录已确认的任务进度，并给出可执行的恢复建议。
3. **异步委托：** 将支线问题整理成可编辑的委托请求，后台最多检索两份公开来源，并生成经过来源核查、附带引用的简短答案。
4. **延迟展示：** 可在用户选定的检查点展示答案，也支持提前查看或取消。

## 拟采用的技术架构

- **浏览器扩展：** React + TypeScript、Chrome Manifest V3 侧边栏
- **后端：** Python + FastAPI、独立异步 Worker
- **NLP：** 可替换的预训练语言模型服务接口
- **状态管理：** 浏览器会话存储与必要的后端持久化
- **评估：** 可复现的实验脚本与事件日志

> 这些是建议采用的实现方式，不表示功能已经完成，也不构成额外课程要求。具体研究范围以已提交的 Proposal 为准。

## 仓库结构

```text
apps/extension/       # 浏览器扩展与侧边栏
services/backend/     # API、NLP 与 Agent
experiments/          # 实验任务、基线及分析
docs/                 # 架构、API 协议与研究说明
tests/                # 自动化测试
TODO.md               # 中文任务清单
TODO.en.md            # English task list
CONTRIBUTING.md       # 中文协作规范
CONTRIBUTING.en.md    # English contribution guide
```

## 研究计划

按照 Proposal，设计四种实验条件：

| 条件 | 功能 |
|---|---|
| **G** | 目标感知提醒 |
| **P** | G + 分心记录与任务恢复 |
| **I** | P + 异步委托，答案就绪后立即展示 |
| **D** | P + 异步委托，答案延迟到检查点展示 |

计划先进行预实验，再开展 12–18 名成年参与者的组内平衡实验；此外，使用 60 个任务上下文样本评估活动分类，并使用 40 个保留请求评估委托结果。具体指标与控制条件见 Proposal。

## 开始协作

1. 阅读 [TODO 任务清单](TODO.md)，确定分工和首轮目标。
2. 全组先统一数据结构与 API 协议，再开始并行开发。
3. 遵循 [协作规范](CONTRIBUTING.md)，每项功能在独立分支开发，通过 Pull Request 合并。
4. **目前仅有项目文档和目录骨架，尚无可运行应用。**


## 自由认领工作板块

项目已开放 [六个可认领的 GitHub Issues](https://github.com/Ir1svanquish/IntentAware-Agent/issues)：A 浏览器扩展、B NLP 目标与分类、C 任务记忆、D 异步委托、E 实验评估、F 共享 API 与集成（由志愿者牵头、全组评审）。**目前均未指派成员**。每个 Issue 包含任务范围、实施步骤、交付物和验收标准。

查看 [中文认领指南](docs/WORKSTREAMS.md) 或 [English claiming guide](docs/WORKSTREAMS.en.md)。选中任务后直接在对应 Issue 评论认领，可单独认领子任务，不必包下整个模块。

## 隐私与研究规范

不要提交 API 密钥、私密浏览内容、参与者身份信息或未经同意收集的数据；不要伪造实验结果或引用。
