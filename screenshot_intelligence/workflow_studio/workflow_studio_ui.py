import streamlit as st

from screenshot_intelligence.workflow_studio.workflow_step_extractor import (
    extract_workflow_steps
)

from screenshot_intelligence.workflow_studio.workflow_generator import (
    generate_workflow
)

from screenshot_intelligence.workflow_studio.gif_generator import (
    generate_workflow_gif
)
from ui.procedure_renderer import (
    render_procedure
)


MAX_SCREENSHOTS = 15


def render_workflow_studio():

    st.title("🧩 Workflow Studio")

    st.caption(
        "Create intelligent workflows from screenshots."
    )

    st.divider()

    workflow_name = st.text_input(

        "Workflow Name",

        placeholder="Example: Create Templates"

    )

    uploaded_files = st.file_uploader(

        "Upload Workflow Screenshots",

        type=["png", "jpg", "jpeg"],

        accept_multiple_files=True

    )

    if uploaded_files and len(uploaded_files) > MAX_SCREENSHOTS:

        st.error(
            f"Maximum {MAX_SCREENSHOTS} screenshots are allowed."
        )

        return

    #
    # Initialize session state
    #

    if uploaded_files:

        names = [x.name for x in uploaded_files]

        previous = st.session_state.get(
            "workflow_file_names",
            []
        )

        if names != previous:

            st.session_state["workflow_file_names"] = names

            st.session_state["workflow_screens"] = list(
                uploaded_files
            )

    screens = st.session_state.get(
        "workflow_screens",
        []
    )

    if screens:

        st.success(
            f"{len(screens)} screenshots uploaded."
        )

        st.info(
            "Use ↑ and ↓ to reorder screenshots before generating the workflow."
        )

        st.subheader("Workflow Preview")

        for index, image in enumerate(screens):

            col1, col2 = st.columns([6, 1])

            with col1:

                st.image(

                    image,

                    caption=f"Step {index + 1}",

                    width="stretch"

                )

            with col2:

                if index > 0:

                    if st.button(

                        "⬆",

                        key=f"up_{index}"

                    ):

                        screens[index], screens[index-1] = (
                            screens[index-1],
                            screens[index]
                        )

                        st.rerun()

                if index < len(screens)-1:

                    if st.button(

                        "⬇",

                        key=f"down_{index}"

                    ):

                        screens[index], screens[index+1] = (
                            screens[index+1],
                            screens[index]
                        )

                        st.rerun()

    st.divider()

    if st.button(

        "🚀 Build Workflow",

        width="stretch"

    ):

        if not workflow_name:

            st.warning(
                "Enter a workflow name."
            )

            return

        if len(screens) < 2:

            st.warning(
                "Upload at least two screenshots."
            )

            return

        progress = st.progress(0)

        progress.progress(10)

        with st.spinner(
            "Analyzing screenshots..."
        ):

            workflow_steps = extract_workflow_steps(
                screens
            )

        progress.progress(60)

        with st.spinner(
            "Generating workflow..."
        ):

            workflow = generate_workflow(

                workflow_name,

                workflow_steps

            )

        progress.progress(90)

        gif = generate_workflow_gif(
            screens
        )

        progress.progress(100)

        st.success(
            "Workflow generated successfully."
        )

        st.session_state["generated_workflow"] = workflow

        st.session_state["generated_gif"] = gif

    #
    # Output
    #

    if "generated_workflow" in st.session_state:

        st.divider()

        st.subheader("📄 Generated Workflow")

        render_procedure(

            workflow_name,

            st.session_state[
                "generated_workflow"
            ]

        )

        st.download_button(

            "⬇ Download Text",

            data=st.session_state[
                "generated_workflow"
            ],

            file_name="workflow.txt",

            mime="text/plain",

            width="stretch"

        )

        st.divider()

        st.subheader("🎬 Workflow GIF")

        st.image(

            st.session_state[
                "generated_gif"
            ]

        )

        st.download_button(

            "⬇ Download GIF",

            data=st.session_state[
                "generated_gif"
            ],

            file_name="workflow.gif",

            mime="image/gif",

            width="stretch"

        )
    