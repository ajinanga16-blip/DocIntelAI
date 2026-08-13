from style_intelligence.ux.builtin_ux_styles import (
    BUILTIN_UX_STYLES
)

from style_intelligence.custom_style_list import (
    CustomStyleList
)


class UXStyleSelector:

    def get_builtin_styles(
        self
    ):

        return BUILTIN_UX_STYLES

    def get_custom_styles(
        self
    ):

        return (
            CustomStyleList()
            .get_styles()
        )

    def get_all_styles(
        self
    ):

        styles = []

        #
        # Built-in UX styles
        #

        for style in self.get_builtin_styles():

            styles.append({

                "name":
                style["name"],

                "type":
                "Built-in",

                "source":
                style["url"]

            })

        #
        # Existing custom styles
        #

        for style in self.get_custom_styles():

            styles.append({

                "name":
                style,

                "type":
                "Custom",

                "source":
                None

            })

        return styles