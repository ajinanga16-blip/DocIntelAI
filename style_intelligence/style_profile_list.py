from pathlib import Path


class StyleProfileList:

    def get_profiles(self):

        profiles_dir = (
            Path(__file__).parent.parent
            / "style_profiles"
        )

        profiles = []

        for file in profiles_dir.glob(
            "*.json"
        ):

            if (
                "_rules"
                not in file.name
            ):

                profiles.append(
                    file.stem.replace(
                        "_",
                        " "
                    ).title()
                )

        return profiles