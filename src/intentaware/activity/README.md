# 前台观察与任务监视器

本模块把前台应用与窗口标题转换为可供用户修正的任务线索。它不读取页面或文档正文，不采集截图、键盘输入或剪贴板，也不发送网络请求。

| 文件 | 作用 |
| --- | --- |
| [`models.py`](models.py) | 不可变的 `ActivitySnapshot`、`CaptureResult` 与 `TaskSuggestion`；观察键由应用名称和标题生成。 |
| [`observer.py`](observer.py) | Windows 原生接口与 Linux X11 `xprop` 适配；过滤自身窗口、已知密码管理器与隐私窗口标记，明确报告不可用环境。 |
| [`monitor.py`](monitor.py) | `TaskMonitor` 在后台采样，在主线程应用稳定结果，协调首次任务建立、后续活动分析、人工修正、暂停与排除设置。 |
| [`demo.py`](demo.py) | `DemoObserver` 返回固定示例，`--demo` 显式使用，来源标记为 `demo`。 |

## 观察与更新

`create_observer().capture()` 返回 `CaptureResult`。正常结果包含快照；其他状态为 `idle`、`excluded` 或 `unavailable`。Windows 不需要额外采集依赖；Linux X11 需要 `DISPLAY` 与 `xprop`。macOS、Wayland 或无法读取前台窗口的环境保留手动任务和活动输入。

常规采样间隔为 1 秒，窗口信息稳定约 3 秒后应用。首次观察具有足够信息时生成任务；信息不足时需要人工补充。已有主任务不会被后续窗口切换替换，用户可以选择采用新任务建议。活动描述与四分类仍会自动更新。

`analyze_manual(activity)` 提交人工补充的活动分析；任务与观察上下文不变时保留该结果，新的活动再恢复自动分析。`correct_task()` 更新当前任务与用户填写的进度。`adopt_suggestion()` 建立新任务，旧支线仍属于旧任务。暂停、排除或关闭会使已发出的过期观察结果失效，避免延迟结果重新显示。自己的工作台获得焦点时，界面可继续显示最近一次外部活动。

## 数据边界

隐私过滤可能需要临时读取标题来识别隐私标记；匹配的窗口跳过识别，不显示或保存相关活动。已知规则不能代替用户自己的排除设置。在界面按应用名称添加排除项，每行一个；大小写与 `.exe` 后缀会归一化。暂停和排除偏好保存在本地。

持续窗口观察的事件只记录来源、摘要键、类别和置信度，不附原始应用名称或窗口标题。自动建立的任务标题仍会保存在本地任务中，可能含页面或文件名称。任何观察和分类都不能填入已确认进度。

## 验证

[`test_observer.py`](../../../tests/test_observer.py) 使用可控系统接口检查 Windows 句柄、X11 标题、过滤、超时与不可用环境；[`test_monitor.py`](../../../tests/test_monitor.py) 检查稳定采样、自动任务、人工修正、重启设置与延迟结果。还需在支持的桌面环境中运行 `python -m intentaware`，切到真实工作窗口后确认来源、活动与任务显示符合实际。

[上手指南](../../../docs/GETTING_STARTED.md) · [本地推断](../nlp/README.md) · [共享接口](../contracts/README.md)
