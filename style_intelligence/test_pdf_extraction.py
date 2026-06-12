from style_intelligence.style_extractor import (
    StyleExtractor
)

extractor = StyleExtractor()

content = extractor.extract_from_pdf(
    "style_guides/Microsoft-style-guide.pdf"
)

print(content[:5000])