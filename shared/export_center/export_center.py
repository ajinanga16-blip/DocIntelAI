import streamlit as st

from shared.export_center.txt_exporter import export_txt
from shared.export_center.markdown_exporter import export_markdown
from shared.export_center.html_exporter import export_html
from shared.export_center.xml_exporter import export_xml
from shared.export_center.dita_exporter import export_dita
from shared.export_center.docx_exporter import export_docx
from shared.export_center.pdf_exporter import export_pdf


def render_export_center(
    title,
    content
):
    """
    Shared Export Center

    Used by:

    - Workflow Studio
    - Screenshot Intelligence
    - Gap Analysis
    - Impact Analyzer
    - Documentation Generator
    """

    st.markdown("---")

    st.subheader("📤 Export Documentation")

    st.caption(
        "Download the generated documentation in your preferred format."
    )

    #
    # Row 1
    #

    col1, col2, col3 = st.columns(3)

    with col1:

        st.download_button(

            "📘 Microsoft Word",

            data=export_docx(
                title,
                content
            ),

            file_name=f"{title}.docx",

            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",

            width="stretch"

        )

    with col2:

        st.download_button(

            "📕 PDF",

            data=export_pdf(
                title,
                content
            ),

            file_name=f"{title}.pdf",

            mime="application/pdf",

            width="stretch"

        )

    with col3:

        st.download_button(

            "🌐 HTML",

            data=export_html(
                title,
                content
            ),

            file_name=f"{title}.html",

            mime="text/html",

            width="stretch"

        )

    #
    # Row 2
    #

    col4, col5, col6 = st.columns(3)

    with col4:

        st.download_button(

            "📝 Markdown",

            data=export_markdown(
                content
            ),

            file_name=f"{title}.md",

            mime="text/markdown",

            width="stretch"

        )

    with col5:

        st.download_button(

            "📄 Plain Text",

            data=export_txt(
                content
            ),

            file_name=f"{title}.txt",

            mime="text/plain",

            width="stretch"

        )

    with col6:

        st.download_button(

            "🗂 XML",

            data=export_xml(
                title,
                content
            ),

            file_name=f"{title}.xml",

            mime="application/xml",

            width="stretch"

        )

    #
    # Row 3
    #

    col7, col8, col9 = st.columns(3)

    with col7:

        st.download_button(

            "📚 DITA XML",

            data=export_dita(
                title,
                content
            ),

            file_name=f"{title}.dita",

            mime="application/xml",

            width="stretch"

        )

    with col8:

        st.empty()

    with col9:

        st.empty()