"""OpenAI question-generation skeleton for Wiki Survival."""

from typing import Any

from wiki_data import Article


Question = dict[str, Any]


def generate_questions(articles: list[Article]) -> list[Question]:
    """Generate one four-choice question for each of five articles.

    Every generated question should contain four possible answers and exactly
    one correct answer.
    """

    pass
