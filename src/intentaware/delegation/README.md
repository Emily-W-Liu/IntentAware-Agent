# D 异步委托

[`demo.py`](demo.py) 的 `DemoDelegator` 在后台返回明确标注的离线示例，没有进行实时检索。真实公开来源检索、引用核验与答案评估仍待实现。

替换时实现 [`Delegator.run(question, cancel) -> DelegationResult`](../contracts/interfaces.py)，通过 `DesktopSession(delegator=...)` 注入。返回非空答案与最多两条来源，外部请求需有有限超时，并在每段操作前后检查取消信号。

[`session.py`](../session.py) 管理任务状态。在「委托」页面检查 I 条件完成即交付、D 条件等待检查点或提前查看，以及取消后不显示该任务答案。G/P 不提供委托。委托只在当前应用会话和实验轮次中可操作；切换条件前须交付或取消未结束的任务。

用 [`test_session.py`](../../../tests/test_session.py) 验证完成、交付、失败与取消。完成事件与交付事件分开记录，避免把后台结果就绪当成用户已经看到答案。

[接入说明](../../../docs/GETTING_STARTED.md#接入分类器或委托执行器) · [认领与验收](https://github.com/Ir1svanquish/IntentAware-Agent/issues/4)
