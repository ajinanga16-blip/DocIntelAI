import json
from pathlib import Path

import streamlit as st


PROJECT_ROOT = Path(__file__).resolve().parent.parent
NOTIFICATIONS_FOLDER = PROJECT_ROOT / "data" / "notifications"


def show_page():

    st.title("🔔 Notifications")

    notifications = []

    if NOTIFICATIONS_FOLDER.exists():

        for notification_file in NOTIFICATIONS_FOLDER.glob("*.json"):

            with open(notification_file, "r", encoding="utf-8") as file:

                notifications.append(json.load(file))

    if not notifications:

        st.info("No notifications available.")

        return

    notifications.sort(
        key=lambda notification: notification["created_at"],
        reverse=True
    )

    for notification in notifications:

        st.info(
            f"**{notification['title']}**\n\n"
            f"{notification['message']}\n\n"
            f"{notification['created_at']}"
        )