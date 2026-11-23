语言 / Language：**简体中文** | [English](README.en.md)

# IntentAware-Agent

**HKU COMP7607 · Natural Language Processing · Group 14**

## 项目简介

**IntentAware-Agent** 是一款面向学习、写作与编程场景的桌面 AI 任务助手。它根据用户的主要目标和当前活动上下文，判断支线活动是否有助于完成任务，保存临时想法与进度，并帮助用户在中断后继续工作。对于可以稍后处理的问题，用户可以委托 Agent 异步检索，并选择合适的时间查看结果。

### 典型使用流程

1. **设定目标：** 输入当前任务及希望完成的下一步，例如“完成论文的 Related Work 部分”。
2. **提交上下文：** 输入当前活动、问题或粘贴需要分析的文本。
3. **理解活动：** Agent 判断该活动属于直接进展、必要准备、可选探索还是不确定，并说明理由。
4. **记录与委托：** 保存分心内容或把支线问题交给 Agent 在后台处理。
5. **恢复任务：** 根据已确认的进度获得具体的继续操作建议；委托结果可立即查看或留到任务检查点展示。

## 核心功能

| 模块 | 功能 |
| --- | --- |
| **Goal & Intent** | 澄清任务目标、提取下一步行动；结合上下文进行四分类并解释判断依据 |
| **Detour & Resume** | 保存链接、笔记与已确认进度；生成具体的任务恢复建议 |
| **Async Delegation** | 将问题整理成可编辑的委托请求；后台检索最多两份公开来源并生成带引用的回答 |
| **Deferred Delivery** | 根据用户选定的检查点控制答案展示，支持提前查看和取消 |
| **Experiment & Evaluation** | 记录任务事件，切换实验条件并评估分类、任务恢复与委托效果 |

## 技术架构

| 组件 | 技术 |
| --- | --- |
| 桌面界面 | **Python + PySide6** |
| NLP 推理 | 可替换的预训练 LLM API |
| 本地数据 | SQLite |
| 异步处理 | Python 后台 Worker / 线程 |
| 实验分析 | pandas + scikit-learn |
| 自动化测试 | pytest |

应用采用 Python 模块化结构。用户主动提供需要分析的上下文，任务和进度保存在本地数据库；耗时的检索任务在后台执行，避免阻塞桌面界面。

## 研究与实验

项目采用四种功能条件进行比较：

| 条件 | 功能 |
| --- | --- |
| **G** | 目标感知提醒 |
| **P** | G + 分心记录与任务恢复 |
| **I** | P + 异步委托，结果就绪后展示 |
| **D** | P + 异步委托，在任务检查点展示结果（支持提前查看） |

计划开展预实验及 12–18 名成年参与者的组内对照研究；另外评估 **60 个活动上下文样本**和 **40 个独立保留的委托请求**。

主要指标包括活动分类的 Macro-F1 和误提醒率、任务完成与输出质量、恢复主任务所需时间、委托答案的引用支持情况、用户感知负担、延迟和 Token 使用量。恢复时间以可记录的下一次有效主任务编辑为终点。

## 四周开发计划

| 周次 | 主要交付 |
| --- | --- |
| **第 1 周** | 项目框架、PySide6 界面、共享数据结构、SQLite 与 LLM 接口；启动实验准备 |
| **第 2 周** | Goal & Intent、Detour & Resume 的完整基础流程 |
| **第 3 周** | Async Delegation、Deferred Delivery、实验条件切换与集成测试 |
| **第 4 周** | 预实验与评估、结果分析、演示和最终报告 |

## 项目结构

```text
src/intentaware/
├── ui/             # 桌面界面
├── nlp/            # 目标理解与活动分类
├── memory/         # 任务进度、分心记录与恢复
├── delegation/     # 异步委托与结果交付
└── contracts/      # 共享数据结构与接口

experiments/        # 实验任务、日志与分析
tests/              # 自动化测试
docs/               # 技术文档与分工说明
TODO.md             # 开发任务清单
CONTRIBUTING.md     # 团队协作规范
```

## 小组协作

项目开放六个任务板块，组员可以在对应 GitHub Issue 中认领整个模块或具体子任务：

**[A 桌面界面](https://github.com/Ir1svanquish/IntentAware-Agent/issues/1)** · **[B NLP](https://github.com/Ir1svanquish/IntentAware-Agent/issues/2)** · **[C 任务记忆](https://github.com/Ir1svanquish/IntentAware-Agent/issues/3)** · **[D 异步委托](https://github.com/Ir1svanquish/IntentAware-Agent/issues/4)** · **[E 研究评估](https://github.com/Ir1svanquish/IntentAware-Agent/issues/5)** · **[F 接口与集成](https://github.com/Ir1svanquish/IntentAware-Agent/issues/6)**

[查看所有待认领任务](https://github.com/Ir1svanquish/IntentAware-Agent/issues) · [详细认领与验收指南](docs/WORKSTREAMS.md) · [开发 TODO](TODO.md) · [协作规范](CONTRIBUTING.md)


### 加入开发组

组员可在 [加入申请 Issue #7](https://github.com/Ir1svanquish/IntentAware-Agent/issues/7) 留下 GitHub 用户名和想认领的模块，维护者确认后邀请加入；也可先 Fork 仓库提交 Pull Request。

## 数据与隐私

仅使用用户主动提供或明确授权的上下文；模型 API 密钥保存在本地环境变量中，实验记录避免包含可识别的个人数据。
