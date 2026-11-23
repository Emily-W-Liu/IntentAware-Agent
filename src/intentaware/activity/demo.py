"""An explicit deterministic sample; never used for real foreground collection."""

from intentaware.activity.models import ActivitySnapshot, CaptureResult


class DemoObserver:
    def capture(self) -> CaptureResult:
        return CaptureResult(ActivitySnapshot(
            app_name="Code.exe",
            window_title="window.py - IntentAware-Agent - Visual Studio Code",
            source="demo",
        ))
