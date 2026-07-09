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

    st.subheader("📤 Export")

    c1, c2, c3, c4 = st.columns(4)

    #
    # Row 1
    #

    with c1:

        st.download_button(

            "📝 TXT",

            data=export_txt(content),

            file_name=f"{title}.txt",

            mime="text/plain",

            width="stretch"

        )

    with c2:

        st.download_button(

            "📄 Markdown",

            data=export_markdown(content),

            file_name=f"{title}.md",

            mime="text/markdown",

            width="stretch"

        )

    with c3:

        st.download_button(

            "🌐 HTML",

            data=export_html(title, content),

            file_name=f"{title}.html",

            mime="text/html",

            width="stretch"

        )

    with c4:

        st.download_button(

            "🗂 XML",

            data=export_xml(title, content),

            file_name=f"{title}.xml",

            mime="application/xml",

            width="stretch"

        )

    c5, c6, c7 = st.columns(3)

    #
    # Row 2
    #

    with c5:

        st.download_button(

            "📚 DITA",

            data=export_dita(title, content),

            file_name=f"{title}.dita",

            mime="application/xml",

            width="stretch"

        )

    with c6:

        st.download_button(

            "📘 DOCX",

            data=export_docx(title, content),

            file_name=f"{title}.docx",

            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",

            width="stretch"

        )

    with c7:

        st.download_button(

            "📕 PDF",

            data=export_pdf(title, content),

            file_name=f"{title}.pdf",

            mime="application/pdf",

            width="stretch"

        )