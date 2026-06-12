from style_intelligence.style_kb_generator import (
    StyleKBGenerator
)


sample_content = """
Use active voice.
Use sentence-case headings.
Use inclusive language.
Use clear and concise writing.
"""

generator = StyleKBGenerator()

result = generator.generate_style_kb(
    sample_content
)

print(result)