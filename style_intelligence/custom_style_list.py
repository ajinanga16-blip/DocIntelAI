from style_intelligence.style_profile_list import (
    StyleProfileList
)


class CustomStyleList:

    def get_styles(self):

        return (
            StyleProfileList()
            .get_profiles()
        )