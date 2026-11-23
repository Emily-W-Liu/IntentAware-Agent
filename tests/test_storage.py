import json
import os
import sqlite3
from dataclasses import replace

import pytest

from intentaware.contracts import ActivityLabel, Condition, Detour, ExperimentEvent, Goal, Progress
from intentaware.memory.store import SQLiteStore


def test_memory_survives_restart_and_preserves_quoted_text(tmp_path):
    path = tmp_path / "memory.sqlite3"
    goal = Goal("完成读书报告", "整理 O'Reilly 的章节")
    progress = Progress(goal.id, "记录了作者的‘主张’与证据")
    detour = Detour(goal.id, "晚点查 '应用案例'", id="detour'1")
    store = SQLiteStore(path)
    try:
        assert store.load_goal() is None
        assert store.load_progress(goal.id) is None
        assert store.list_detours(goal.id) == []
        store.save_goal(goal)
        store.save_progress(progress)
        store.add_detour(detour)
    finally:
        store.close()
        store.close()

    reopened = SQLiteStore(path)
    try:
        assert reopened.load_goal() == goal
        assert reopened.load_progress(goal.id) == progress
        assert reopened.list_detours(goal.id) == [detour]
    finally:
        reopened.close()


def test_saving_existing_goal_activates_it_and_keeps_its_memory(tmp_path):
    path = tmp_path / "memory.sqlite3"
    store = SQLiteStore(path)
    try:
        first = Goal("完成论文", "写正文")
        second = Goal("准备演讲", "找例子", created_at=first.created_at)
        detour = Detour(first.id, "稍后做图")
        progress = Progress(first.id, "写完提纲")
        store.save_goal(first)
        store.add_detour(detour)
        store.save_progress(progress)
        store.save_goal(second)
        assert store.load_goal() == second

        updated = replace(first, next_step="修改正文")
        store.save_goal(updated)
        assert store.load_goal() == updated
        assert store.list_detours(first.id) == [detour]
        assert store.list_detours(second.id) == []
        assert store.load_progress(first.id) == progress
        revised_progress = replace(progress, note="写完第一节")
        store.save_progress(revised_progress)
        assert store.load_progress(first.id) == revised_progress
    finally:
        store.close()

    reopened = SQLiteStore(path)
    try:
        assert reopened.load_goal() == updated
    finally:
        reopened.close()


def test_removing_detour_persists_and_keeps_other_detours(tmp_path):
    path = tmp_path / "memory.sqlite3"
    goal = Goal("完成论文", "写正文")
    removed = Detour(goal.id, "找插图", id="remove'1")
    kept = Detour(goal.id, "查引文")
    store = SQLiteStore(path)
    try:
        store.save_goal(goal)
        store.add_detour(removed)
        store.add_detour(kept)
        store.remove_detour(removed.id)
    finally:
        store.close()

    reopened = SQLiteStore(path)
    try:
        assert reopened.list_detours(goal.id) == [kept]
    finally:
        reopened.close()


def test_event_export_filters_by_run_and_preserves_insertion_order(tmp_path):
    path = tmp_path / "memory.sqlite3"
    filtered_path = tmp_path / "one.jsonl"
    all_path = tmp_path / "all.jsonl"
    first = ExperimentEvent(
        "run'1",
        Condition.D,
        "分类",
        details={"label": ActivityLabel.DIRECT_PROGRESS, "note": "用户输入 '引号'"},
        occurred_at="2026-08-12T10:00:01.000+00:00",
    )
    other = ExperimentEvent("other", Condition.I, "resume_requested")
    last = ExperimentEvent(
        "run'1", Condition.D, "delegation_completed", "goal-1", "job-1",
        occurred_at="2026-08-12T10:00:00.000+00:00",
    )
    store = SQLiteStore(path)
    try:
        for event in (first, other, last):
            store.append_event(event)
    finally:
        store.close()

    reopened = SQLiteStore(path)
    try:
        events = reopened.list_events()
        assert events == [first, other, last]
        assert events[0].condition is Condition.D
        assert reopened.list_events("run'1") == [first, last]
        assert reopened.list_events("missing") == []
        assert reopened.export_events(filtered_path, "run'1") == 2
        assert reopened.export_events(all_path) == 3
    finally:
        reopened.close()

    filtered_text = filtered_path.read_text(encoding="utf-8")
    filtered_rows = [json.loads(line) for line in filtered_text.splitlines()]
    all_rows = [json.loads(line) for line in all_path.read_text(encoding="utf-8").splitlines()]
    assert "用户输入 '引号'" in filtered_text
    assert [row["id"] for row in filtered_rows] == [first.id, last.id]
    assert [row["id"] for row in all_rows] == [first.id, other.id, last.id]
    assert filtered_rows[0]["condition"] == "D"
    assert filtered_rows[0]["details"]["label"] == "direct_progress"
    assert filtered_rows[1]["goal_id"] == "goal-1"
    assert filtered_rows[1]["job_id"] == "job-1"


def test_export_cannot_overwrite_the_database(tmp_path):
    path = tmp_path / "memory.sqlite3"
    store = SQLiteStore(path)
    goal = Goal("完成论文", "写正文")
    try:
        store.save_goal(goal)
        with pytest.raises(ValueError):
            store.export_events(path)
        assert store.load_goal() == goal
    finally:
        store.close()


def test_nested_transaction_commits_only_after_outer_exit(tmp_path):
    path = tmp_path / "memory.sqlite3"
    store = SQLiteStore(path)
    reader = SQLiteStore(path)
    goal = Goal("完成论文", "写正文")
    progress = Progress(goal.id, "写完提纲")
    event = ExperimentEvent("run", Condition.D, "goal_saved", goal.id)
    try:
        with store.transaction():
            store.save_goal(goal)
            with store.transaction():
                store.save_progress(progress)
                store.append_event(event)
            assert reader.load_goal() is None
            assert reader.list_events() == []
        assert reader.load_goal() == goal
        assert reader.load_progress(goal.id) == progress
        assert reader.list_events() == [event]
    finally:
        reader.close()
        store.close()


def test_nested_transaction_rolls_back_goal_progress_and_events(tmp_path):
    store = SQLiteStore(tmp_path / "memory.sqlite3")
    goal = Goal("完成论文", "写正文")
    updated = replace(goal, next_step="修改正文")
    event = ExperimentEvent("run", Condition.D, "goal_saved", goal.id)
    try:
        store.save_goal(goal)
        with pytest.raises(sqlite3.IntegrityError):
            with store.transaction():
                store.save_goal(updated)
                with store.transaction():
                    store.save_progress(Progress(goal.id, "写完提纲"))
                    store.append_event(event)
                    store.append_event(event)
        assert store.load_goal() == goal
        assert store.load_progress(goal.id) is None
        assert store.list_events() == []
    finally:
        store.close()


def test_caught_nested_error_prevents_partial_commit(tmp_path):
    store = SQLiteStore(tmp_path / "memory.sqlite3")
    goal = Goal("完成论文", "写正文")
    event = ExperimentEvent("run", Condition.D, "goal_saved", goal.id)
    try:
        with pytest.raises(RuntimeError):
            with store.transaction():
                store.save_goal(goal)
                store.append_event(event)
                with pytest.raises(sqlite3.IntegrityError):
                    store.append_event(event)
        assert store.load_goal() is None
        assert store.list_events() == []
    finally:
        store.close()


def test_transaction_can_retry_after_commit_fails(tmp_path):
    path = tmp_path / "memory.sqlite3"
    store = SQLiteStore(path)
    database = sqlite3.connect(path)
    goal = Goal("完成论文", "写正文")
    try:
        database.executescript(
            """CREATE TABLE deferred_check (
                   goal_id TEXT REFERENCES goals(id) DEFERRABLE INITIALLY DEFERRED
               );
               CREATE TRIGGER reject_goal AFTER INSERT ON goals BEGIN
                   INSERT INTO deferred_check VALUES ('missing');
               END;"""
        )
        with pytest.raises(sqlite3.IntegrityError):
            with store.transaction():
                store.save_goal(goal)
                assert store.load_goal() == goal
        assert store.load_goal() is None

        database.execute("DROP TRIGGER reject_goal")
        store.save_goal(goal)
        assert database.execute("SELECT id FROM goals").fetchone() == (goal.id,)
    finally:
        database.close()
        store.close()


def test_export_rejects_a_database_hard_link(tmp_path):
    path = tmp_path / "memory.sqlite3"
    alias = tmp_path / "events.jsonl"
    store = SQLiteStore(path)
    try:
        store.append_event(ExperimentEvent("run", Condition.D, "goal_saved"))
        alias.hardlink_to(path)
        with pytest.raises(ValueError):
            store.export_events(alias)
        assert path.read_bytes().startswith(b"SQLite format 3\0")
        assert alias.samefile(path)
    finally:
        store.close()


@pytest.mark.parametrize("failure_stage", ["read", "replace"])
def test_failed_export_preserves_previous_file(tmp_path, monkeypatch, failure_stage):
    path = tmp_path / "memory.sqlite3"
    target = tmp_path / "events.jsonl"
    previous_bytes = b'{"id":"previous"}\n'
    target.write_bytes(previous_bytes)
    store = SQLiteStore(path)
    try:
        store.append_event(ExperimentEvent("run", Condition.D, "goal_saved"))
        if failure_stage == "read":
            original_rows = store._event_rows

            def failing_rows(run_id):
                yield from original_rows(run_id)
                raise OSError("export read failed")

            monkeypatch.setattr(store, "_event_rows", failing_rows)
        else:
            def failing_replace(source, destination):
                raise OSError("export replace failed")

            monkeypatch.setattr(os, "replace", failing_replace)

        with pytest.raises(OSError, match=f"export {failure_stage} failed"):
            store.export_events(target)
        assert target.read_bytes() == previous_bytes
        assert set(tmp_path.iterdir()) == {path, target}
    finally:
        store.close()
