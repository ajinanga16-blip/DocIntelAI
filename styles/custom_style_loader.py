from pathlib import Path


def load_custom_style(
    style_name
):

    file_name = (
        style_name.lower()
        .replace(" ", "_")
        + ".md"
    )

    kb_file = (
        Path(__file__).parent.parent
        / "style_kb"
        / file_name
    )

    if not kb_file.exists():
        return None

    with open(
        kb_file,
        "r",
        encoding="utf-8"
    ) as file:

        return {
            "name": style_name,
            "knowledge_base":
            file.read(),
            "is_custom": True
        }