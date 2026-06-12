from style_intelligence.style_extractor import (
    StyleExtractor
)

from style_intelligence.style_kb_generator import (
    StyleKBGenerator
)

extractor = StyleExtractor()

content = extractor.extract_from_url(
    "https://developers.google.com/style"
)

generator = StyleKBGenerator()

kb = generator.generate_style_kb(
    content
)

generator.save_style_kb(
    kb,
    "google_style_generated.md"
)

print(kb[:5000])