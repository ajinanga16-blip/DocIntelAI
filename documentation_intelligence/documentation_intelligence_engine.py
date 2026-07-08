from streamlit import context

from documentation_intelligence.knowledge_search_engine import (
    search_repository
)

from candidate_selection.ai_candidate_selector import (
    ai_candidate_search
)

from agents.candidate_article_content_fetcher import (
    fetch_candidate_content
)

from ranking.hybrid_ranker import (
    rank_articles
)

from documentation_intelligence.screen_context_builder import (
    build_screen_context
)


def discover_candidate_articles(
    repository_name,
    context
):
    """
    Documentation Intelligence Engine

    Shared by:

    • Screenshot Intelligence
    • Gap Analysis
    • Impact Analysis
    • Future Intelligence Modules
    """
    #
    # Normalize Screenshot Context
    #

    if "page_title" in context or "screen_name" in context:

        context = build_screen_context(context)
    
    print("=" * 60)
    print("NORMALIZED SCREEN CONTEXT")
    print(context)
    print("=" * 60)
    #
    # Stage 1
    # Fast Repository Search
    #

    repository_matches = search_repository(

        repository_name,

        context,

        top_k=20

    )

    print("=" * 60)
    print("STAGE 1 - Repository Search")
    print(f"Matches: {len(repository_matches)}")
    print("=" * 60)

    inventory = [

        item["article"]

        for item in repository_matches

    ]

    #
    # Stage 2
    # AI Candidate Selection
    #

    candidates = ai_candidate_search(

        context,

        inventory

    )

    print("=" * 60)
    print("STAGE 2 - AI Candidate Selection")
    print(f"Matched: {len(candidates.get('matched_articles', []))}")
    print("=" * 60)

    #
    # Stage 3
    # Fetch Candidate Content
    #

    content_articles = fetch_candidate_content(

        candidates["matched_articles"],

        max_articles=len(
            candidates["matched_articles"]
        )

    )
    print("=" * 60)
    print("STAGE 3 - Content Fetch")
    print(f"Fetched: {len(content_articles)}")
    print("=" * 60)

    #
    # Stage 4
    # Hybrid Ranking
    #

    queries = []

    #
    # Generic Documentation Intelligence
    #

    for field in [

        "summary",
        "title",
        "description",
        "acceptance_criteria",
        "primary_screen",
        "primary_action",
        "user_intent"
        

    ]:

        value = context.get(field)

        if value:

            queries.append(value)

    queries.extend(
        context.get(
         "important_keywords",
            []
        )
    )

    queries.extend(
        context.get(
         "ui_context",
            []
        )
    )

    ranked = rank_articles(

        queries,

        content_articles

    )

    print("=" * 60)
    print("STAGE 4 - Hybrid Ranking")
    print(f"Ranked: {len(ranked)}")
    print("=" * 60)

    return ranked