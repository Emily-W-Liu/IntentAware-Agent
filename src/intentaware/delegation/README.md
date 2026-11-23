# D 异步委托

[`demo.py`](demo.py) 的 `DemoDelegator` 在后台返回离线示例。替换时实现 [`Delegator.run(question, cancel) -> DelegationResult`](../contracts/interfaces.py)，通过 `DesktopSession(delegator=...)` 注入。返回非空答案与最多两条来源，外部请求要设置有限超时，并在每段操作前后检查取消信号。

[`session.py`](../session.py) 管理任务状态。检查 I 条件完成即交付，D 条件等待检查点或提前查看，取消后始终隐藏该任务答案。委托任务只在本次应用会话中可操作。

[接入说明](../../../docs/GETTING_STARTED.md#接入分类器或委托执行器) · [认领与验收](https://github.com/Ir1svanquish/IntentAware-Agent/issues/4)
