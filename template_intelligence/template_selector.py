class TemplateSelector:

    def get_template_name(
        self,
        document_type
    ):

        mapping = {

            "User Guide":
            "user_guide_template",

            "FAQ":
            "faq_template",

            "Release Notes":
            "release_notes_template",

            "Knowledge Base":
            "knowledge_base_template",

            "Quick Start Guide":
            "quick_start_guide_template",

            "Video Script":
            "video_script_template",

            "Solution Article":
            "solution_article_template",

            "API Guide":
            "api_guide_template"
        }

        return mapping.get(
            document_type
        )