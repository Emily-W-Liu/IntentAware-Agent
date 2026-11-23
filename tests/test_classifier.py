import pytest

from intentaware.contracts import ActivityContext, ActivityLabel, Goal
from intentaware.nlp.demo import DemoClassifier


@pytest.mark.parametrize(
    ("activity", "label"),
    [
        ("正在撰写论文正文", ActivityLabel.DIRECT_PROGRESS),
        ("查阅论文相关文献", ActivityLabel.NECESSARY_PREPARATION),
        ("刷短视频找撰写论文的灵感", ActivityLabel.OPTIONAL_EXPLORATION),
        ("打开了一个窗口", ActivityLabel.UNCLEAR),
        ("", ActivityLabel.UNCLEAR),
        (" \t\n ", ActivityLabel.UNCLEAR),
    ],
)
def test_demo_classifier_labels_activity_and_explains_rule(activity, label):
    goal = Goal("完成论文", "整理实验结果")
    result = DemoClassifier().classify(ActivityContext(goal, activity))

    assert result.label is label
    assert "规则演示" in result.reason
    assert goal.next_step in result.suggested_next_step


def test_goal_next_step_can_make_reading_direct_progress():
    activity = "阅读第三章"
    classifier = DemoClassifier()
    review_goal = Goal("完成读书报告", "阅读第三章")
    article_goal = Goal("提交文章", "写研究问题")

    review = classifier.classify(ActivityContext(review_goal, activity))
    article = classifier.classify(ActivityContext(article_goal, activity))
    assert review.label is ActivityLabel.DIRECT_PROGRESS
    assert article.label is ActivityLabel.NECESSARY_PREPARATION
