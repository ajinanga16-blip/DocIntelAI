from style_intelligence.customer_style_pipeline import (
    CustomerStylePipeline
)

pipeline = (
    CustomerStylePipeline()
)

profile = (
    pipeline.process_url(
        "Google URL Test",
        "https://developers.google.com/style"
    )
)

print(profile)