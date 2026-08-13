import json

import streamlit as st

from ux_intelligence.ux_review_export import (
    build_word_report,
    build_excel_report
)

from ux_intelligence.ux_screen_analyzer import (
    analyze_screen
)

from ux_intelligence.ux_review_engine import (
    review_microcopy
)

from style_intelligence.ux.ux_style_selector import (
    UXStyleSelector
)


def show_page():

    st.title(
        "✍️ UX Intelligence"
    )

    st.caption(
        "Review product microcopy against UX writing style guides."
    )

    #
    # Screen Upload
    #

    st.subheader(
        "🖼 Upload Screens"
    )

    uploaded_screens = st.file_uploader(

        "Upload one or more product screens",

        type=[
            "png",
            "jpg",
            "jpeg",
            "webp"
        ],

        accept_multiple_files=True,

        key="ux_uploaded_screens"

    )

    if uploaded_screens:

        st.success(

            f"{len(uploaded_screens)} "
            "screen(s) uploaded."

        )

        for screen in uploaded_screens:

            st.write(
                f"✓ {screen.name}"
            )

    #
    # UX Style Guide
    #

    st.divider()

    st.subheader(
        "📖 UX Style Guide"
    )

    style_selector = (
        UXStyleSelector()
    )

    styles = (
        style_selector.get_all_styles()
    )

    if not styles:

        st.warning(
            "No UX style guides are available."
        )

        return

    style_names = [
        style["name"]
        for style in styles
    ]

    selected_style_name = (
        st.selectbox(

            "Select UX Style Guide",

            style_names,

            key="ux_selected_style"

        )
    )

    selected_style = next(

        (

            style
            for style in styles

            if style["name"]
            == selected_style_name

        ),

        None

    )

    if selected_style:

        if selected_style["type"] == "Built-in":

            st.caption(
                "Built-in UX writing guide"
            )

            if selected_style["source"]:

                st.caption(
                    selected_style["source"]
                )

        else:

            st.caption(
                "Custom UX style guide"
            )

    #
    # Review
    #

    st.divider()

    st.subheader(
        "🔍 Review"
    )

    review_clicked = st.button(

        "🔍 Review UX",

        width="stretch",

        key="ux_review_button"

    )

    #
    # Run review
    #

    if review_clicked:

        #
        # Validate screens
        #

        if not uploaded_screens:

            st.warning(

                "Please upload at least one screen "
                "before reviewing the UX."

            )

            return

        #
        # Validate style
        #

        if not selected_style:

            st.warning(
                "Please select a UX style guide."
            )

            return

        #
        # Analyze and review all screens
        #

        reviewed_results = []

        with st.spinner(
            "Analyzing and reviewing screen microcopy..."
        ):

            for screen in uploaded_screens:

                screen_result = {

                    "screen":
                    screen.name,

                    "analysis":
                    None,

                    "microcopy_items":
                    [],

                    "findings":
                    [],

                    "error":
                    None

                }

                try:

                    #
                    # Step 1:
                    # Extract visible microcopy
                    #

                    analysis = (
                        analyze_screen(
                            screen
                        )
                    )

                    screen_result[
                        "analysis"
                    ] = analysis

                    #
                    # Step 2:
                    # Parse extraction result
                    #

                    extracted = json.loads(
                        analysis
                    )

                    microcopy_items = (
                        extracted.get(
                            "items",
                            []
                        )
                    )

                    screen_result[
                        "microcopy_items"
                    ] = microcopy_items

                    #
                    # Step 3:
                    # Review extracted microcopy
                    #

                    if microcopy_items:

                        review = (
                            review_microcopy(

                                microcopy_items,

                                selected_style_name

                            )
                        )

                        screen_result[
                            "findings"
                        ] = review.get(

                            "findings",

                            []

                        )

                except Exception as error:

                    screen_result[
                        "error"
                    ] = str(error)

                reviewed_results.append(
                    screen_result
                )

        #
        # Store results
        #

        st.session_state[
            "ux_review_results"
        ] = reviewed_results

        st.session_state[
            "ux_review_style"
        ] = selected_style_name

        st.session_state[
            "ux_review_completed"
        ] = True

    #
    # Stop here if there is no review yet
    #

    if not st.session_state.get(
        "ux_review_completed",
        False
    ):

        return

    #
    # Retrieve stored review
    #

    reviewed_results = (
        st.session_state.get(
            "ux_review_results",
            []
        )
    )

    review_style = (
        st.session_state.get(
            "ux_review_style",
            selected_style_name
        )
    )

    #
    # Review Results
    #

    st.divider()

    st.header(
        "UX Review Results"
    )

    st.caption(
        f"Style Guide: {review_style}"
    )

    #
    # Calculate summary
    #

    screens_reviewed = len(
        reviewed_results
    )

    microcopy_reviewed = 0

    acceptable_count = 0

    improvement_count = 0

    issue_count = 0

    for result in reviewed_results:

        for finding in result.get(
            "findings",
            []
        ):

            microcopy_reviewed += 1

            assessment = (
                finding.get(
                    "assessment",
                    ""
                ).lower()
            )

            if assessment == "acceptable":

                acceptable_count += 1

            elif assessment == "improvement":

                improvement_count += 1

            elif assessment == "issue":

                issue_count += 1

    #
    # Summary
    #

    st.subheader(
        "Review Summary"
    )

    col1, col2, col3, col4, col5 = (
        st.columns(5)
    )

    with col1:

        st.metric(
            "Screens",
            screens_reviewed
        )

    with col2:

        st.metric(
            "Items Reviewed",
            microcopy_reviewed
        )

    with col3:

        st.metric(
            "Acceptable",
            acceptable_count
        )

    with col4:

        st.metric(
            "Improvements",
            improvement_count
        )

    with col5:

        st.metric(
            "Issues",
            issue_count
        )

    #
    # Finding filter
    #

    st.subheader(
        "Findings"
    )

    finding_filter = st.radio(

        "Show",

        [
            "All",
            "Issues & Improvements"
        ],

        horizontal=True,

        key="ux_finding_filter"

    )

    show_all = (
        finding_filter == "All"
    )

    #
    # Display each screen
    #

    for result in reviewed_results:

        screen_name = (
            result["screen"]
        )

        st.markdown(
            "---"
        )

        st.subheader(
            screen_name
        )

        #
        # Find uploaded image
        #

        screen_file = next(

            (

                screen

                for screen in uploaded_screens

                if screen.name
                == screen_name

            ),

            None

        )

        #
        # Display uploaded screenshot
        #

        if screen_file:

            st.image(

                screen_file,

                caption=screen_name,

                width="stretch"

            )

        #
        # Display processing error
        #

        if result.get(
            "error"
        ):

            st.error(
                result["error"]
            )

            continue

        #
        # Get findings
        #

        findings = (
            result.get(
                "findings",
                []
            )
        )

        #
        # No reviewable microcopy
        #

        if not findings:

            st.info(

                "No reviewable UX findings "
                "were identified on this screen."

            )

            continue

        #
        # Apply display filter
        #

        visible_findings = []

        for finding in findings:

            assessment = (
                finding.get(
                    "assessment",
                    "improvement"
                ).lower()
            )

            if show_all:

                visible_findings.append(
                    finding
                )

            elif assessment in [

                "improvement",

                "issue"

            ]:

                visible_findings.append(
                    finding
                )

        #
        # Nothing matching filter
        #

        if not visible_findings:

            st.success(

                "No issues or improvements "
                "were identified on this screen."

            )

            continue

        #
        # Display findings
        #

        for finding in visible_findings:

            assessment = (
                finding.get(
                    "assessment",
                    "improvement"
                ).lower()
            )

            severity = (
                finding.get(
                    "severity",
                    "medium"
                )
            )

            if assessment == "acceptable":

                status_label = (
                    "✓ Acceptable"
                )

            elif assessment == "improvement":

                status_label = (
                    "⚠ Improvement"
                )

            else:

                status_label = (
                    "🔴 Issue"
                )

            st.markdown(
                "---"
            )

            st.markdown(

                f"### "
                f"{finding.get('text', '')}"

            )

            st.write(

                f"**Assessment:** "
                f"{status_label}"

            )

            st.write(

                f"**Element:** "
                f"{finding.get('element_type', '')}"

            )

            st.write(

                f"**Context:** "
                f"{finding.get('approximate_context', '')}"

            )

            if finding.get(
                "recommended_text"
            ):

                st.info(

                    "Recommended microcopy: "
                    f"**{finding['recommended_text']}**"

                )

            st.write(

                f"**Reason:** "
                f"{finding.get('reason', '')}"

            )

            st.write(

                f"**Style rule:** "
                f"{finding.get('style_rule', '')}"

            )

            st.write(

                f"**Severity:** "
                f"{severity}"

            )
        #
    # Export Review
    #

    st.divider()

    st.header(
        "📥 Export Review"
    )

    st.caption(
        "Download the completed UX review "
        "for sharing with product, design, "
        "and content teams."
    )

    #
    # Build Word report
    #

    word_report = build_word_report(

        reviewed_results,

        review_style,

        uploaded_screens

    )

    #
    # Build Excel report
    #

    excel_report = build_excel_report(

        reviewed_results,

        review_style

    )

    #
    # Download buttons
    #

    col1, col2 = st.columns(2)

    with col1:

        st.download_button(

            label="📄 Download Word Report",

            data=word_report,

            file_name="UX_Microcopy_Review.docx",

            mime=(
                "application/vnd.openxmlformats-"
                "officedocument.wordprocessingml.document"
            ),

            width="stretch",

            key="ux_download_word"

        )

    with col2:

        st.download_button(

            label="📊 Download Excel Report",

            data=excel_report,

            file_name="UX_Microcopy_Review.xlsx",

            mime=(
                "application/vnd.openxmlformats-"
                "officedocument.spreadsheetml.sheet"
            ),

            width="stretch",

            key="ux_download_excel"

        )        