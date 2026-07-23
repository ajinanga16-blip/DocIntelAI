import streamlit as st


def render_manual_input_ui():

    st.subheader("Manual Input")

    change_description = st.text_area(
        "Describe the Product Change",
        height=200,
        placeholder="Describe the feature, enhancement, bug fix, or UI change..."
    )

    return change_description