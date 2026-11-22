# IntentAware-Agent

**HKU COMP7607 Natural Language Processing · Group 14**  
**Project / 项目名称:** An Agent with Intent Awareness for Task Continuity and Asynchronous Delegation

> **Status / 当前状态:** Planning and initial setup / 规划与初始搭建阶段。The code modules are not implemented yet. / 目前尚未实现功能模块。

## Overview / 项目简介

**EN:** A proposed browser-based focus companion that understands a user's current goal, interprets browsing activities in context, captures useful detours, helps resume unfinished work, and optionally delegates side questions to a background agent. Results can be delivered immediately or at a user-selected checkpoint.

**中文：** 本项目计划开发一款浏览器侧边栏 AI 助手，理解用户当前目标、结合上下文判断浏览行为、保存临时分心内容，并帮助用户恢复未完成任务。用户也可将支线问题交给后台 Agent，选择立即查看结果或等到指定检查点再查看。

## Planned features / 计划功能

1. **Goal clarification & activity interpretation / 目标澄清与活动理解** — Confirm the goal and classify activities as `direct_progress`, `necessary_preparation`, `optional_exploration`, or `unclear` (four provisional API labels corresponding to the proposal's four categories). / 确认任务目标，将活动判为直接进展、必要准备、可选探索或不确定。
2. **Detour capture & task resumption / 分心记录与任务恢复** — Save links/notes, record confirmed progress, and suggest a concrete next step. / 保存链接和笔记、记录已确认的进度，并提出可执行的下一步。
3. **Asynchronous delegation / 异步委托** — Confirm an editable request, retrieve at most two public sources, and produce a checked, source-linked answer. / 确认可编辑的查询请求，最多检索两份公开来源，生成带来源链接并经过核对的答案。
4. **Deferred delivery / 延迟展示** — Show answers at a user-selected checkpoint while allowing early viewing or cancellation. / 在用户选定的检查点展示结果，同时支持提前查看与取消。

## Planned architecture / 计划架构

- **Browser extension / 浏览器扩展:** React + TypeScript, Chrome Manifest V3 sidebar.
- **Backend / 后端:** Python + FastAPI, with a separate asynchronous worker.
- **NLP / 语言模型:** Replaceable pretrained language-model provider / 可替换的预训练语言模型接口。
- **State / 状态管理:** Session/browser storage with backend persistence where required / 浏览器会话存储及必要的后端持久化。
- **Evaluation / 评估:** Reproducible scripts and experiment logging / 可复现的实验脚本与事件日志。

These are **implementation proposals**, not completed features or additional course requirements.  
以上为**拟采用的实现方案**，并不代表功能已经完成，也不代表新增了课程要求。

## Repository / 仓库目录

```text
apps/extension/       # Browser sidebar / 浏览器侧边栏
services/backend/     # API and NLP/agent modules / 后端与 NLP/Agent 模块
experiments/          # Research tasks and analysis / 研究任务与分析
docs/                 # Architecture and decisions / 架构与决策
tests/                # Automated tests / 自动化测试
TODO.md               # Project checklist / 项目任务清单
CONTRIBUTING.md       # Team workflow / 团队协作规范
```

## Research plan / 研究计划

The proposal defines four experimental conditions: **G** (goal-aware reminders), **P** (+ detour capture and resumption), **I** (+ delegation, immediate delivery), and **D** (+ delegation, deferred delivery). Planned evaluation includes a pilot, a counterbalanced within-participant study with 12–18 adults, 60 task-context examples, and 40 held-out requests. Details are in the approved group proposal.  
Proposal 规定四组条件：**G**（目标感知提醒）、**P**（增加分心记录与任务恢复）、**I**（增加委托并立即展示）、**D**（增加委托并延迟展示）。拟开展预实验、12–18 人的组内平衡实验，并评估 60 个活动上下文样本与 40 个保留请求。具体要求以已提交 Proposal 为准。

## Start here / 从这里开始

1. Read [TODO.md](TODO.md) / 阅读任务清单。
2. Agree on API contracts and responsibilities before coding / 开发前统一 API 协议与人员分工。
3. Follow [CONTRIBUTING.md](CONTRIBUTING.md) and open a feature branch / 依照协作规范建立功能分支。
4. **No runnable application is included yet.** / **当前仅为初始化骨架，尚无可运行应用。**

## Privacy / 隐私

Do not commit API keys, private browsing content, participant identifiers, or unconsented user data.  
不要上传 API 密钥、私人浏览内容、参与者身份信息或未经同意收集的用户数据。
