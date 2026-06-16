from style_intelligence.gpt_style_fixer import (
    GPTStyleFixer
)

fixer = GPTStyleFixer()

result = fixer.fix_passive_voice(
    "The primary forecast can be copied."
)

print(result)