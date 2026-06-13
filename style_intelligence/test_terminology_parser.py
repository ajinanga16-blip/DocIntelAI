from style_intelligence.terminology_parser import (
    TerminologyParser
)

parser = TerminologyParser()

print(
    parser.extract_term_mapping(
        "Use allow list instead of whitelist"
    )
)

print(
    parser.extract_term_mapping(
        "Use block list instead of blacklist"
    )
)