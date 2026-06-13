import json

from pathlib import Path


class StyleProfileRules:

    def save_rules(
        self,
        style_name,
        rules
    ):

        rules_dir = (
            Path(__file__).parent.parent
            / "style_profiles"
        )

        rules_dir.mkdir(
            exist_ok=True
        )

        file_name = (
            style_name.lower()
            .replace(" ", "_")
            + "_rules.json"
        )

        rules_file = (
            rules_dir / file_name
        )

        with open(
            rules_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                rules,
                file,
                indent=4
            )

    def load_rules(
        self,
        style_name
    ):

        rules_dir = (
            Path(__file__).parent.parent
            / "style_profiles"
        )

        file_name = (
            style_name.lower()
            .replace(" ", "_")
            + "_rules.json"
        )

        rules_file = (
            rules_dir / file_name
        )

        with open(
            rules_file,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)