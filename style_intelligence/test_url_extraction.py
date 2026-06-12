from style_intelligence.style_extractor import (
    StyleExtractor
)

extractor = StyleExtractor()

content = extractor.extract_from_url(
    "https://developers.google.com/style"
)

print(content[:5000])