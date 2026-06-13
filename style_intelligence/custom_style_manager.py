import json

from pathlib import Path
from datetime import datetime

from style_intelligence.style_profile_schema import (
    STYLE_PROFILE_SCHEMA
)


class CustomStyleManager:

    def create_style_profile(
        self,
        style_name,
        kb_file,
        rules
    ):

        profile = (
            STYLE_PROFILE_SCHEMA.copy()
        )

        profile["style_name"] = (
            style_name
        )

        profile["source_type"] = (
            "custom"
        )

        profile["kb_file"] = (
            kb_file
        )

        profile["rule_count"] = (
            len(rules)
        )

        profile["created_at"] = (
            datetime.now().isoformat()
        )

        profiles_dir = (
            Path(__file__).parent.parent
            / "style_profiles"
        )

        profiles_dir.mkdir(
            exist_ok=True
        )

        file_name = (
            style_name.lower()
            .replace(" ", "_")
            + ".json"
        )

        profile_file = (
            profiles_dir / file_name
        )

        with open(
            profile_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                profile,
                file,
                indent=4
            )

        return profile

    def load_style_profile(
        self,
        style_name
    ):

        profiles_dir = (
            Path(__file__).parent.parent
            / "style_profiles"
        )

        file_name = (
            style_name.lower()
            .replace(" ", "_")
            + ".json"
        )

        profile_file = (
            profiles_dir / file_name
        )

        with open(
            profile_file,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)