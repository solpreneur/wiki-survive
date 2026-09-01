"""Wikipedia article-retrieval skeleton for Wiki Survival."""


Article = dict[str, str]


def get_wikipedia_articles(
    topic: str,
    search_count: int = 7,
    required_count: int = 5,
) -> list[Article]:
    """Return five usable article titles and one-sentence summaries.

    Search seven Wikipedia articles so that two can be used as backups when
    an article is missing, ambiguous, or otherwise unusable.
    """

    # Temporary mock data for developers working on later parts of the game.
    # Replace this list with live Wikipedia retrieval when that task is built.
    articles = [
        {
            "title": "Mars",
            "summary": "Mars is the fourth planet from the Sun.",
        },
        {
            "title": "Jupiter",
            "summary": "Jupiter is the largest planet in the Solar System.",
        },
        {
            "title": "Saturn",
            "summary": "Saturn is the sixth planet from the Sun.",
        },
        {
            "title": "Venus",
            "summary": "Venus is the second planet from the Sun.",
        },
        {
            "title": "Mercury",
            "summary": "Mercury is the closest planet to the Sun.",
        },
    ]

    return articles
