from styles.style_loader import (
    get_style_profile
)

print(
    get_style_profile(
        "Microsoft Technical Writing"
    )["name"]
)

print(
    get_style_profile(
        "Microsoft Test"
    )["name"]
)