from style_intelligence.style_extractor import (
    StyleExtractor
)

from style_intelligence.style_kb_generator import (
    StyleKBGenerator
)

extractor = StyleExtractor()

content = extractor.extract_from_pdf(
    "style_guides/Microsoft-style-guide.pdf"
)

generator = StyleKBGenerator()

result = generator.generate_style_kb(
    content
)

generator.save_style_kb(
    result,
    "microsoft_style_generated.md"
)

print("KB saved successfully")