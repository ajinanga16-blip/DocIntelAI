from xml.etree.ElementTree import (
    Element,
    SubElement,
    tostring
)


def export_dita(
    title,
    content
):
    """
    Export DITA Topic.
    """

    topic = Element(

        "topic",

        id="docintel-topic"

    )

    topic.set(

        "xml:lang",

        "en-US"

    )

    title_node = SubElement(

        topic,

        "title"

    )

    title_node.text = title

    body = SubElement(

        topic,

        "body"

    )

    p = SubElement(

        body,

        "p"

    )

    p.text = content

    return tostring(

        topic,

        encoding="unicode"

    )