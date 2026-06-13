from style_intelligence.builtin_styles import (
    BUILTIN_STYLES
)

from style_intelligence.custom_style_list import (
    CustomStyleList
)


class StyleSelector:

    def get_builtin_styles(
        self
    ):

        return BUILTIN_STYLES

    def get_custom_styles(
        self
    ):

        return (
            CustomStyleList()
            .get_styles()
        )