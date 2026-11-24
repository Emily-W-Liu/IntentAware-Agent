# C 模块：任务记忆与恢复

基于上游 `5f9e1175f6a929283b375e866fbb2648aba4a863`，提交分支为 `feature/task-memory`。

## 功能与接口

- 支线笔记、HTTP(S) 链接和用途的新增、查看、编辑与删除。
- SQLite 保存目标、用户确认的进度及支线，重启后恢复；支线保持原任务归属。
- 基于已保存目标、进度和下一步生成恢复提示，不调用 API，不推断用户已完成的工作。
- 支持忽略当前版本的提示、暂停／开启提示；设置跨重启保留，暂停时仍可手动恢复。
- 修改目标或进度后更新恢复提示；保存失败时保留编辑草稿。
- 数据变更与对应事件在同一事务提交，失败整体回滚。

共享数据结构 `Detour` 在原有字段后增加 `url`、`purpose`，默认均为空字符串，兼容原有构造调用。旧数据库打开时自动追加字段，不删除旧记录。

新增／扩展接口：

```python
session.add_detour(text, url="", purpose="")
session.update_detour(detour_id, text, url="", purpose="")
session.remove_detour(detour_id)
session.recovery_preview()
session.ignore_recovery()
session.set_recovery_paused(paused)
session.resume()
```

新增事件为 `detour_updated`、`recovery_ignored`、`recovery_paused`、`recovery_resumed`。事件记录标识与状态，不附支线正文；`resume_requested` 仍不代表有效主任务编辑。

## 安装与运行

依赖及 Python 版本与项目 README 一致。创建标准虚拟环境后运行：

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -e ".[dev]"
zsh ./test-memory.command
zsh ./start-memory.command
```

两个 `.command` 脚本用于 macOS 本地测试；显式使用脚本对应的 `zsh` 运行，无需依赖网页上传是否保留可执行权限。启动脚本采用手动模式、P 条件和独立的 `local-memory-data/` 数据目录。也可直接使用跨平台命令：

```bash
python -m pytest -q
python -m intentaware --manual --condition P --data-dir ./local-memory-data
```

## 验证结果（2026-11-24）

迁移到具有真实上游 Git 历史的提交分支后，使用已有 Python 3.12 / PySide6-Essentials 6.8.3 环境运行完整测试，结果为 **147 passed in 10.29s**。此前开发目录完整测试同为 147 项通过。

测试覆盖：

- 旧数据库升级、升级后编辑、关闭后重新读取。
- 任务、进度、支线、链接和用途的完整持久化流程及跨任务隔离。
- 多个独立解释器退出／启动后的数据和提示设置恢复。
- 空记录、无效链接、数据库真实写锁，以及解锁后重试。
- 事件写入受约束时的目标、进度及恢复设置整体回滚。
- UI 正常及错误输入、保存失败保留草稿、任务切换关闭旧编辑器。
- G/P/I/D 后端门控与原有界面回归。

实际桌面已确认：目标和进度保存；支线新增／编辑／删除；空输入和无效链接错误反馈；提示更新／忽略／暂停／手动恢复；用户重新启动应用后目标、进度及支线内容恢复。SQLite 独立只读连接的完整性检查为 `ok`。

## 已知限制及交接

- 本机 macOS 实际操作条件下拉框时发生过两次 `SIGSEGV / EXC_BAD_ACCESS`。系统报告主线程栈涉及 `objc_release`、NSArray 释放与 `libqcocoa.dylib`，没有 Python 层异常；根因尚未确认。记录对应 `Python-2026-11-24-144448.ips` 和 `Python-2026-11-24-150149.ips`。实际条件切换的手动验收未完成，请 A/F 复核。实验条件控件及样式保持原样，不声明该问题已修复。
- 完整自动化通过不代表已覆盖上述 macOS 原生交互崩溃。
- 本提交只交付 C；尚未与 NLP PR #13 联合测试。请 F 集成后核对任务／已确认进度传递、旧上下文分类结果处理及共享 UI／会话代码兼容性。
- 测试使用临时数据库；本地示例数据库和运行日志不应提交。
