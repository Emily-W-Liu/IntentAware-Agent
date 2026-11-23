# C 任务记忆与恢复

[`store.py`](store.py) 的 `SQLiteStore` 保存当前目标、已确认进度、支线和实验事件。更新当前目标时保留目标标识。恢复提示由 [`DesktopSession.resume()`](../session.py) 根据已保存的资料生成。

用同一数据目录重新启动，检查目标、进度和支线是否保留，再验证恢复提示中的下一步。[存储测试](../../../tests/test_storage.py)覆盖数据往返。

[数据目录与测试](../../../docs/GETTING_STARTED.md#本地数据与测试) · [认领与验收](https://github.com/Ir1svanquish/IntentAware-Agent/issues/3)
