from io import BytesIO

from openpyxl import Workbook


def _save_workbook(wb):

    output = BytesIO()

    wb.save(output)

    output.seek(0)

    return output


def export_inventory(
    inventory
):

    wb = Workbook()

    ws = wb.active

    ws.title = "Inventory"

    ws.append([
        "Title",
        "URL"
    ])

    for article in inventory:

        ws.append([

            article.get(
                "title",
                ""
            ),

            article.get(
                "url",
                ""
            )

        ])

    return _save_workbook(
        wb
    )


def export_matched_articles(
    matched_articles
):

    wb = Workbook()

    ws = wb.active

    ws.title = "Matched Articles"

    ws.append([
        "Selected",
        "Title",
        "URL",
        "Confidence",
        "Matched On",
        "Reason",
        "Affected Section"
    ])

    for article in matched_articles:

        ws.append([

            "",

            article.get(
                "title",
                ""
            ),

            article.get(
                "url",
                ""
            ),

            article.get(
                "confidence",
                ""
            ),

            ", ".join(
                article.get(
                    "matched_on",
                    []
                )
            ),

            article.get(
                "reason",
                ""
            ),

            article.get(
                "affected_section",
                ""
            )

        ])

    return _save_workbook(
        wb
    )