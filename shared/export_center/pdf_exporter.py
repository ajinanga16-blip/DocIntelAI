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
    Export PDF while preserving
    basic Markdown structure.
    """

    output = BytesIO()

    doc = SimpleDocTemplate(
        output
    )

    styles = getSampleStyleSheet()

    story = []

    #
    # Document Title
    #

    story.append(

        Paragraph(

            title,

            styles["Title"]

        )

    )

    #
    # Process Markdown
    #

    for line in content.splitlines():

        line = line.strip()

        if not line:
            continue

        #
        # Heading 5
        #

        if line.startswith("##### "):

            story.append(

                Paragraph(

                    line[6:].strip(),

                    styles["Heading3"]

                )

            )

            continue

        #
        # Heading 4
        #

        if line.startswith("#### "):

            story.append(

                Paragraph(

                    line[5:].strip(),

                    styles["Heading3"]

                )

            )

            continue

        #
        # Heading 3
        #

        if line.startswith("### "):

            story.append(

                Paragraph(

                    line[4:].strip(),

                    styles["Heading3"]

                )

            )

            continue

        #
        # Heading 2
        #

        if line.startswith("## "):

            story.append(

                Paragraph(

                    line[3:].strip(),

                    styles["Heading2"]

                )

            )

            continue

        #
        # Heading 1
        #

        if line.startswith("# "):

            story.append(

                Paragraph(

                    line[2:].strip(),

                    styles["Heading1"]

                )

            )

            continue

        #
        # Bullet List
        #

        if line.startswith("- "):

            story.append(

                Paragraph(

                    "• " + line[2:].strip(),

                    styles["BodyText"]

                )

            )

            continue

        if line.startswith("* "):

            story.append(

                Paragraph(

                    "• " + line[2:].strip(),

                    styles["BodyText"]

                )

            )

            continue

        #
        # Numbered List
        #

        if (
            len(line) > 3
            and line[0].isdigit()
            and line[1:3] == ". "
        ):

            story.append(

                Paragraph(

                    line,

                    styles["BodyText"]

                )

            )

            continue

        #
        # Normal Paragraph
        #

        clean_line = line.replace(
            "**",
            ""
        )

        story.append(

            Paragraph(

                clean_line,

                styles["BodyText"]

            )

        )

    doc.build(
        story
    )

    output.seek(
        0
    )

    return output