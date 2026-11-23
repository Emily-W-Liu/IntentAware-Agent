"""以少量中文关键词演示四分类流程。"""

from intentaware.contracts import ActivityContext, ActivityLabel, Classification


# 活动描述未匹配下一步时，按顺序使用第一个匹配的规则。
_RULES = (
    (
        ActivityLabel.OPTIONAL_EXPLORATION,
        ("刷短视频", "刷微博", "闲聊", "购物", "打游戏", "玩游戏", "顺便", "无关"),
        "可能是可以稍后处理的支线",
        "先记下支线，然后回到下一步",
    ),
    (
        ActivityLabel.NECESSARY_PREPARATION,
        ("查阅", "阅读", "查找", "教程", "收集资料", "查资料", "准备", "预习"),
        "看起来是在为任务查找资料或做准备",
        "找够当前所需的信息后，回到下一步",
    ),
    (
        ActivityLabel.DIRECT_PROGRESS,
        ("撰写", "编写", "写正文", "修改", "整理", "绘制", "实现", "运行实验", "提交"),
        "看起来是在执行任务或更新成果",
        "继续当前工作，并对照下一步",
    ),
)


class DemoClassifier:
    def classify(self, context: ActivityContext) -> Classification:
        activity = context.activity.strip().casefold()
        next_step = context.goal.next_step.strip()
        if next_step and next_step.casefold() in activity:
            return Classification(
                ActivityLabel.DIRECT_PROGRESS,
                "规则演示：活动描述包含你为当前目标设定的下一步。",
                f"继续执行下一步：{next_step}",
            )

        for label, keywords, explanation, suggestion in _RULES:
            matched = next((keyword for keyword in keywords if keyword in activity), None)
            if matched:
                return Classification(
                    label,
                    f"规则演示：检测到“{matched}”，{explanation}。",
                    f"{suggestion}：{next_step}",
                )

        return Classification(
            ActivityLabel.UNCLEAR,
            f"规则演示：描述中的信息不足以判断活动如何帮助“{context.goal.title}”。",
            f"补充活动会带来的具体结果，然后对照下一步：{next_step}",
        )
