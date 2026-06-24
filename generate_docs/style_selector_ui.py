import streamlit as st

from style_intelligence.style_selector import (
    StyleSelector
)


def render_style_selector():

    selector = StyleSelector()

    builtin_styles = (
        selector.get_builtin_styles()
    )

    custom_styles = (
        selector.get_custom_styles()
    )

    style_source = st.radio(
        "Style Source",
        [
            "Built-in",
            "Custom"
        ]
    )

    if style_source == "Built-in":

        style_guide = st.selectbox(
            "Built-in Style Guide",
            builtin_styles
        )

    else:

        if not custom_styles:

            st.warning(
                "No custom style guides available."
            )

            style_guide = None

        else:

            style_guide = st.selectbox(
                "Custom Style Guide",
                custom_styles
            )

    return style_guide