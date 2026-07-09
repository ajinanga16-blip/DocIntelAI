from io import BytesIO

from docx import Document


def export_docx(
    title,
    content
):
    """
    Export Microsoft Word document.
    """

    document = Document()

    document.add_heading(
        title,
        level=1
    )

    for line in content.splitlines():

        line = line.strip()

        if not line:
            continue

        if line.startswith("#"):
            continue

        document.add_paragraph(
            line.replace("**", "")
        )

    output = BytesIO()

    document.save(output)

    output.seek(0)

    return output