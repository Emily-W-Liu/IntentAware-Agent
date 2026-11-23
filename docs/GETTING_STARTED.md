# 桌面应用上手指南

先安装 Python 3.11 或更新版本，再按[快速开始](../README.md#快速开始)安装项目并启动窗口。离线演示在运行时无需联网，也无需配置 API 密钥。

## 六步跑通离线演示

1. 保持实验条件为 **D**，点击 **填入示例**，再点击 **保存目标**。「填入示例」只填表。再次保存会更新同一个当前目标，已有支线仍关联该目标。
2. 点击 **分析活动**，等待界面显示类别、理由和建议下一步。类别有直接进展、必要准备、可选探索和不确定四种。
3. 点击 **暂存为支线**，在「支线与恢复」页确认记录出现。点击 **恢复任务**，确认提示包含已确认进度和下一步。关闭应用后，以同一个数据目录重启，确认目标、进度和支线仍在，再点击一次 **恢复任务**，以便在当前轮次的导出中看到该事件。
4. 打开「异步委托」页，输入问题并点击 **提交委托**。任务状态应从「处理中」变为「待交付」。等待时可以操作窗口，答案此时仍隐藏。
5. 点击 **到达检查点**，确认状态变为「已交付」，并出现离线演示结果。再提交两次，分别检查 **提前查看** 与 **取消委托**。提前查看需要选中「待交付」的任务。取消可用于「处理中」或「待交付」的任务。取消后应显示「已取消」，且结果区不出现该任务的答案。
6. 打开「运行事件」页，点击 **导出 JSONL** 并选一个文件名。检查同一个 `job_id` 的 `delegation_completed` 和 `delegation_delivered` 是两条独立记录。点击恢复任务对应 `resume_requested`。研究所需的「下一次有效主任务编辑」需要另行观测。

### 对照条件

| 条件 | 可验证的行为 |
| --- | --- |
| G | 可以保存目标并分析活动。 |
| P | 在 G 的基础上，可暂存支线并恢复任务。 |
| I | 在 P 的基础上，可提交异步委托，结果就绪即交付。 |
| D | 在 P 的基础上，可提交异步委托。结果就绪后，在检查点交付，也可提前查看。 |

启动时可用 `--condition G` 等参数指定初始条件。切换条件会开启新的实验轮次（`run_id`）并清空委托列表，旧轮次事件仍保留在 SQLite 中。界面导出只包含当前轮次，因此应在切换前完成该轮导出。切换前须等分析结束，并交付或取消所有「处理中」或「待交付」的委托。委托任务只在当前轮次中可操作，重启后可继续使用本地的目标、进度和支线。

## 开发从哪个文件开始

按认领板块打开对应的源码与测试。

| 板块 | 改动入口 | 验证方式 |
| --- | --- | --- |
| [A 桌面交互](https://github.com/Ir1svanquish/IntentAware-Agent/issues/1) | [`ui/window.py`](../src/intentaware/ui/window.py) 的 `MainWindow`。负责输入、反馈、操作按钮和结果展示。 | [`tests/test_ui.py`](../tests/test_ui.py) 和上述六步。 |
| [B 目标与活动分类](https://github.com/Ir1svanquish/IntentAware-Agent/issues/2) | [`nlp/demo.py`](../src/intentaware/nlp/demo.py) 的 `DemoClassifier`，新实现放在 `src/intentaware/nlp/`。 | [`tests/test_classifier.py`](../tests/test_classifier.py)，覆盖四种返回类别。 |
| [C 任务记忆与恢复](https://github.com/Ir1svanquish/IntentAware-Agent/issues/3) | [`memory/store.py`](../src/intentaware/memory/store.py) 的 `SQLiteStore`，恢复提示由 [`session.py`](../src/intentaware/session.py) 的 `DesktopSession.resume()` 组织。 | [`tests/test_storage.py`](../tests/test_storage.py) 和重启检查。 |
| [D 异步委托](https://github.com/Ir1svanquish/IntentAware-Agent/issues/4) | [`delegation/demo.py`](../src/intentaware/delegation/demo.py) 的 `DemoDelegator`，新实现放在 `src/intentaware/delegation/`。后台执行和交付状态由 [`session.py`](../src/intentaware/session.py) 管理。 | [`tests/test_session.py`](../tests/test_session.py)，检查完成、交付、失败和取消。 |
| [E 研究评估](https://github.com/Ir1svanquish/IntentAware-Agent/issues/5) | [`experiments/`](../experiments/) 放实验材料和分析。[`contracts/models.py`](../src/intentaware/contracts/models.py) 定义 `ExperimentEvent`，[`session.py`](../src/intentaware/session.py) 记录事件。 | 分别导出 G/P/I/D 的 JSONL；按 `run_id` 和 `job_id` 核对事件。 |
| [F 接口与集成](https://github.com/Ir1svanquish/IntentAware-Agent/issues/6) | [`contracts/models.py`](../src/intentaware/contracts/models.py) 和 [`contracts/interfaces.py`](../src/intentaware/contracts/interfaces.py) 定义契约。[`session.py`](../src/intentaware/session.py) 协调流程，[`__main__.py`](../src/intentaware/__main__.py) 装配应用，[`config.py`](../src/intentaware/config.py) 选择默认数据目录。 | [`tests/test_session.py`](../tests/test_session.py) 和完整测试。 |

## 接入分类器或委托执行器

在 `nlp/` 或 `delegation/` 新建实现类，按 [`contracts/interfaces.py`](../src/intentaware/contracts/interfaces.py) 实现对应方法。开发时用构造函数注入；若要让命令行入口使用新实现，在 [`__main__.py`](../src/intentaware/__main__.py) 创建 `DesktopSession` 的位置传入实例。

```python
session = DesktopSession(
    store,
    classifier=my_classifier,
    delegator=my_delegator,
    condition=Condition.D,
)
```

`store` 为 `SQLiteStore` 实例，`my_classifier` 和 `my_delegator` 为新实现实例。只替换其中一个时，可省略另一个参数以继续使用对应的离线实现。

- `Classifier.classify(context: ActivityContext) -> Classification` 从 `context.goal`、`context.activity`、`context.progress` 取得输入，返回 `ActivityLabel`、理由与建议下一步。调用外部模型时，为请求设置有限超时。界面通过 `session.start_analysis(activity)` 提交分类，由工作线程运行。直接调用时可使用同步的 `session.analyze(activity)`。
- `Delegator.run(question: str, cancel: threading.Event) -> DelegationResult` 返回非空答案与最多两条 `Source(title, url)`。给外部请求设置有限超时，并在请求前后及连续操作之间检查 `cancel.is_set()`。若需等待，使用支持提前结束的等待，例如 `cancel.wait(seconds)`，并在收到取消信号时尽快退出。
- 分类和委托的后台实现只处理输入并返回结果，或抛出异常交给会话处理。由主线程调用 `session.poll()` 接收后台结果并更新数据，界面随后刷新。Qt 控件与 SQLite 连接都应留在主线程。

当前界面中的「离线演示」文案和 `session.py` 事件中的 `offline_demo` 标记是演示配置。接入真实模型用于评估前，同步更新这些标记，并记录所用模型与提示词版本。

扩展存储时，使用 `with store.transaction():` 将同一次操作的数据修改与事件记录一起提交。保存失败时，该操作整体回滚；界面状态只在提交成功后更新。

## 本地数据与测试

SQLite 文件名为 `intentaware.sqlite3`，默认保存于下列目录。

| 系统 | 数据目录 |
| --- | --- |
| Windows | `%LOCALAPPDATA%\IntentAware` |
| macOS | `~/Library/Application Support/IntentAware` |
| Linux | `$XDG_DATA_HOME/IntentAware`，未设置时用 `~/.local/share/IntentAware` |

可用 `python -m intentaware --demo --data-dir ./demo-data` 指定单独的演示目录，或设置系统环境变量 `INTENTAWARE_DATA_DIR`。命令行参数优先。应用不会自动加载 `.env`。

安装开发依赖后，在已激活的虚拟环境中运行 `python -m pytest`，也可使用快速开始中的虚拟环境 Python 路径替换 `python`。Linux 无显示环境可运行 `QT_QPA_PLATFORM=offscreen python -m pytest`。提交 PR 时，附上相关模块的测试结果，以及上述可复现的正常、失败或取消流程。

[项目首页](../README.md) · [认领任务](WORKSTREAMS.md)
