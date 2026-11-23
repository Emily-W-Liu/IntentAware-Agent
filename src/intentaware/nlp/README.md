# B 目标与活动分类

[`local.py`](local.py) 提供两个本地规则入口：

- `LocalTaskRecognizer.infer(ActivitySnapshot) -> TaskSuggestion`：利用应用名称和窗口标题，生成候选任务、下一步、活动描述、置信度和理由。标题信息不足时返回低置信度，由用户补充或修正。
- `LocalActivityClassifier.classify(ActivityContext) -> Classification`：结合任务与活动描述，返回直接进展、必要准备、可选探索或不确定，以及理由和建议下一步。

规则覆盖 VS Code 系编辑器、Word/WPS 文档、PDF 阅读器与常见浏览器；未覆盖的应用或通用标题会保留不确定。

这些规则不读取页面或文档正文，不调用 LLM，也不能确认用户已完成任何工作。[`demo.py`](demo.py) 的 `DemoClassifier` 保留原有关键词演示实现。LLM 目标澄清、语义理解和正式评估仍待完成。

替换分类器时实现 [`Classifier`](../contracts/interfaces.py)，通过 `DesktopSession(classifier=...)` 注入，并在命令行入口装配新实例。外部请求需设置有限超时，界面通过后台任务运行分类，主线程接收结果。

用 [`test_task_inference.py`](../../../tests/test_task_inference.py) 检查中英文标题、无足够信息的标题与任务推断；用 [`test_classifier.py`](../../../tests/test_classifier.py) 检查原有四分类规则。与任务状态有关的行为在 [`test_monitor.py`](../../../tests/test_monitor.py) 验证，包括首次建立任务、人工修正与主任务保留。

[接入说明](../../../docs/GETTING_STARTED.md#接入分类器或委托执行器) · [认领与验收](https://github.com/Ir1svanquish/IntentAware-Agent/issues/2)
