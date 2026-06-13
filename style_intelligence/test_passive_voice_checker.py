from style_intelligence.passive_voice_checker import (
    PassiveVoiceChecker
)

checker = PassiveVoiceChecker()

document = """
The report was generated automatically.

Users create forecasts.

The file was uploaded by the user.
"""

results = checker.find_passive_voice(
    document
)

print(results)