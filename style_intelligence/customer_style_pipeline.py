from style_intelligence.style_extractor import (
    StyleExtractor
)

from style_intelligence.style_kb_generator import (
    StyleKBGenerator
)

from style_intelligence.kb_reviewer import (
    KBReviewer
)

from style_intelligence.custom_style_manager import (
    CustomStyleManager
)

from style_intelligence.style_profile_rules import (
    StyleProfileRules
)


class CustomerStylePipeline:

    def process_pdf(
        self,
        style_name,
        pdf_file
    ):

        extractor = StyleExtractor()

        generator = StyleKBGenerator()

        reviewer = KBReviewer()

        profile_manager = (
            CustomStyleManager()
        )

        rules_manager = (
            StyleProfileRules()
        )

        content = (
            extractor.extract_from_pdf(
                pdf_file
            )
        )

        kb = (
            generator.generate_style_kb(
                content
            )
        )

        kb_file = (
            style_name.lower()
            .replace(" ", "_")
            + ".md"
        )

        generator.save_style_kb(
            kb,
            kb_file
        )

        rules = (
            reviewer.extract_rules(
                kb
            )
        )

        rules_manager.save_rules(
            style_name,
            rules
        )

        profile = (
            profile_manager
            .create_style_profile(
                style_name,
                kb_file,
                rules
            )
        )

        return profile