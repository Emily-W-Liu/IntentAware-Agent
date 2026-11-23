# C 任务记忆与恢复

[`store.py`](store.py) 的 `SQLiteStore` 保存任务、用户确认的进度、支线、实验事件，以及识别暂停和排除应用设置。自动生成的任务标题会保存在本地，可能包含文件或页面名称；原始持续窗口标题不会逐条写入事件。

点击「修正」后保存会更新同一个当前任务，保留其支线关联。采用新任务建议会创建新的任务标识；旧支线仍归属于旧任务，当前界面只展示当前任务的支线。任务识别与分类不能被当作已确认进度。

[`DesktopSession.resume()`](../session.py) 根据保存的进度与下一步组织恢复提示。用同一数据目录重启，检查任务、进度、支线和设置是否保留。恢复按钮产生 `resume_requested` 事件，研究中的下一次有效主任务编辑需要另行记录。

修改存储后运行 [`test_storage.py`](../../../tests/test_storage.py)；涉及观察设置或任务切换时也运行 [`test_monitor.py`](../../../tests/test_monitor.py)。数据修改与对应事件应在同一事务中提交，失败时整体回滚。

[数据目录与测试](../../../docs/GETTING_STARTED.md#本地数据与测试) · [认领与验收](https://github.com/Ir1svanquish/IntentAware-Agent/issues/3)
