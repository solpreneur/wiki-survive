"""Gameplay, results, and replay skeleton for Wiki Survival."""

from typing import Any


STARTING_LIVES = 3
POINTS_PER_CORRECT_ANSWER = 1


def present_question(question: dict[str, Any]) -> int:
    """Display one question with four choices and return the selected answer."""

    pass


def check_answer(question: dict[str, Any], selected_answer: int) -> bool:
    """Check the selection against the question's single correct answer."""

    pass


def play_game(player_name: str, questions: list[dict[str, Any]]) -> dict[str, Any]:
    """Run the question loop while tracking points and three lives.

    Correct answers add one point. Wrong answers remove one life and reveal
    the correct answer. The game ends after all questions or at zero lives.
    """

    pass


def display_results(player_name: str, result: dict[str, Any]) -> None:
    """Display win/loss status, total points, and remaining lives."""

    pass


def play_again() -> bool:
    """Ask whether the player wants to choose a new topic and play again."""

    pass
