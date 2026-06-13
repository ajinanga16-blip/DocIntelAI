from style_intelligence.style_profile_list import (
    StyleProfileList
)

profiles = (
    StyleProfileList()
    .get_profiles()
)

print(profiles)