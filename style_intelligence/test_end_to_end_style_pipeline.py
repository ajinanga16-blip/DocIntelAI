from style_intelligence.style_extractor import (
    StyleExtractor
)

from style_intelligence.style_kb_generator import (
    StyleKBGenerator
)

from style_intelligence.kb_reviewer import (
    KBReviewer
)

extractor = StyleExtractor()

content = extractor.extract_from_pdf(
    "style_guides/Microsoft-style-guide.pdf"
)

generator = StyleKBGenerator()

kb = generator.generate_style_kb(
    content
)

generator.save_style_kb(
    kb,
    "microsoft_style_generated.md"
)

reviewer = KBReviewer()

rules = reviewer.extract_rules(
    kb
)

print(f"Rules extracted: {len(rules)}")