# B 目标与活动分类

[`demo.py`](demo.py) 的 `DemoClassifier` 通过离线规则分类。替换时实现 [`Classifier.classify(ActivityContext) -> Classification`](../contracts/interfaces.py)，通过 `DesktopSession(classifier=...)` 注入。

返回四类之一、理由和建议下一步。接入外部模型时设置有限的请求超时，界面会在后台调用分类。用 [`tests/test_classifier.py`](../../../tests/test_classifier.py) 检查四类输出，并在窗口中用一条活动验证结果展示。

[接入说明](../../../docs/GETTING_STARTED.md#接入分类器或委托执行器) · [认领与验收](https://github.com/Ir1svanquish/IntentAware-Agent/issues/2)
