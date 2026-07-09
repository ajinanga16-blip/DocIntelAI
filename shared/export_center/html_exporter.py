import markdown


def export_html(
    title,
    content
):
    """
    Export HTML.
    """

    body = markdown.markdown(content)

    return f"""
<html>

<head>

<title>{title}</title>

<style>

body {{

    font-family: Arial;

    max-width:900px;

    margin:auto;

    padding:40px;

}}

</style>

</head>

<body>

{body}

</body>

</html>
"""