from style_intelligence.style_profile_rules import (
    StyleProfileRules
)


class StyleProfileService:

    def get_rules(
        self,
        style_name
    ):

        rules_manager = (
            StyleProfileRules()
        )

        return (
            rules_manager.load_rules(
                style_name
            )
        )