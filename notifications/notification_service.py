import json
from pathlib import Path
from datetime import datetime


PROJECT_ROOT = Path(__file__).resolve().parent.parent

NOTIFICATIONS_FOLDER = PROJECT_ROOT / "data" / "notifications"

NOTIFICATIONS_FOLDER.mkdir(parents=True, exist_ok=True)


def create_notification(title, message):

    notification = {
        "title": title,
        "message": message,
        "created_at": datetime.now().isoformat(),
        "read": False
    }

    filename = datetime.now().strftime("%Y%m%d%H%M%S%f") + ".json"

    with open(
        NOTIFICATIONS_FOLDER / filename,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(notification, file, indent=4)