import streamlit as st

from job_engine.job_results.result_manager import (
    load_job_result
)

from gap_analysis.action_plan_renderer import (
    render_action_plan
)


def show_page(job_id):

    if not job_id:

        st.error(
            "No job selected."
        )

        return

    result = load_job_result(job_id)

    if not result:

        st.error(
            "Result not found."
        )

        return

    result_type = result.get(
        "result_type",
        ""
    )

    st.title(result_type)

    #
    # Back to Job Manager
    #

    if st.button(
    "← Back to Job Manager",
    type="primary"
    ):

        st.session_state["selected_page"] = "⚙ Job Manager"

        st.session_state.pop(
            "selected_job_id",
            None
        )

        st.rerun()

    st.caption(
        f"Repository: {result.get('repository','')}"
    )

    st.divider()

    #
    # Temporary Debug
    #

    st.write("Result Type:", result_type)

    #
    # Documentation Action Plan
    #

    if result_type == "Documentation Action Plan":

        render_action_plan(

            result.get(
                "data",
                []
            )

        )

    else:
    
            st.json(result)

    st.divider()

    if st.button(
        "← Back to Job Manager",
        key="back_bottom",
        type="primary"
    ):

        st.session_state["selected_page"] = "⚙ Job Manager"

        st.session_state.pop(
            "selected_job_id",
            None
        )

        st.rerun()

    #
    # Fallback
    #

    