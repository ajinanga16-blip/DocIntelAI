import streamlit as st


def set_inventory(inventory):
    st.session_state["inventory"] = inventory


def get_inventory():
    return st.session_state.get(
        "inventory",
        []
    )


def set_matched_articles(articles):
    st.session_state["matched_articles"] = articles


def get_matched_articles():
    return st.session_state.get(
        "matched_articles",
        []
    )


def set_documentation_impact(impact):
    st.session_state[
        "documentation_impact"
    ] = impact


def get_documentation_impact():
    return st.session_state.get(
        "documentation_impact"
    )


def clear_documentation_impact():

    st.session_state.pop(
        "documentation_impact",
        None
    )