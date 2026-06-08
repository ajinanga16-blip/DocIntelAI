from pathlib import Path


def load_style_kb(filename):

    kb_path = (
        Path(__file__).parent
        / "style_kb"
        / filename
    )

    with open(
        kb_path,
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()