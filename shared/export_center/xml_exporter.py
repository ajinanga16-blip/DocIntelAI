from xml.etree.ElementTree import (
    Element,
    SubElement,
    tostring
)


def export_xml(
    title,
    content
):
    """
    Export generic XML.
    """

    root = Element("document")

    title_node = SubElement(
        root,
        "title"
    )

    title_node.text = title

    content_node = SubElement(
        root,
        "content"
    )

    content_node.text = content

    return tostring(

        root,

        encoding="unicode"

    )