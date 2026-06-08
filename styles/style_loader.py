from style_kb_loader import load_style_kb
from styles.microsoft import get_style_profile as microsoft_profile
from styles.google import get_style_profile as google_profile
from styles.ibm import get_style_profile as ibm_profile
from styles.chicago import get_style_profile as chicago_profile


def get_style_profile(style_guide):

    profiles = {
        "Microsoft Technical Writing": microsoft_profile(),
        "Google Developer Documentation": google_profile(),
        "IBM Technical Documentation": ibm_profile(),
        "Chicago Editorial Style": chicago_profile()
    }

    profile = profiles.get(
        style_guide,
        microsoft_profile()
    )

    profile["knowledge_base"] = load_style_kb(
        profile["kb_file"]
    )

    return profile