from io import BytesIO

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def export_pdf(
    title,
    content
):
    """
    Export PDF.
    """

    output = BytesIO()

    doc = SimpleDocTemplate(output)

    styles = getSampleStyleSheet()

    story = []

    story.append(

        Paragraph(

            f"<b>{title}</b>",

            styles["Heading1"]

        )

    )

    for line in content.splitlines():

        line = line.strip()

        if not line:
            continue

        if line.startswith("#"):
            continue

        line = line.replace("**", "")

        story.append(

            Paragraph(

                line,

                styles["BodyText"]

            )

        )

    doc.build(story)

    output.seek(0)

    return output