"""Gameplay, results, and replay skeleton for Wiki Survival."""

from typing import Any


STARTING_LIVES = 3
POINTS_PER_CORRECT_ANSWER = 1

# Basic terminal colors
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"


def present_question(question: dict[str, Any]) -> int:
    """Display one question with four choices and return the selected answer."""

    print(f"\n{BOLD}{CYAN}{question['question']}{RESET}")

    choices = question["choices"]
    for number, choice in enumerate(choices, start=1):
        print(f"{number}. {choice}")

    while True:
        answer = input(f"{YELLOW}Choose an answer (1-4): {RESET}").strip()

        if answer.isdigit():
            selected_answer = int(answer)
            if 1 <= selected_answer <= len(choices):
                return selected_answer

        print(f"{RED}Invalid choice. Please enter a number from 1 to 4.{RESET}")


def check_answer(question: dict[str, Any], selected_answer: int) -> bool:
    """Check the selection against the question's single correct answer."""

    choices = question["choices"]

    if selected_answer < 1 or selected_answer > len(choices):
        return False

    selected_choice = choices[selected_answer - 1]
    return selected_choice == question["correct_answer"]


def play_game(player_name: str, questions: list[dict[str, Any]]) -> dict[str, Any]:
    """Run the question loop while tracking points and three lives.

    Correct answers add one point. Wrong answers remove one life and reveal
    the correct answer. The game ends after all questions or at zero lives.
    """

    lives = STARTING_LIVES
    score = 0
    correct_answers = 0
    answered_questions = 0

    print(f"\n{BOLD}{CYAN}The game begins now, {player_name}!{RESET}")

    for question in questions:
        selected_answer = present_question(question)
        answered_questions += 1

        if check_answer(question, selected_answer):
            score += POINTS_PER_CORRECT_ANSWER
            correct_answers += 1
            print(f"{GREEN}Correct! You earned 1 point.{RESET}")
        else:
            lives -= 1
            print(f"{RED}Incorrect!{RESET}")
            print(f"{GREEN}The correct answer was: {question['correct_answer']}{RESET}")
            print(f"{YELLOW}You have {lives} lives remaining.{RESET}")

            if lives == 0:
                print(f"{RED}You have lost all your lives. The game is over.{RESET}")
                break

    won = answered_questions == len(questions) and lives > 0

    return {
        "won": won,
        "score": score,
        "correct_answers": correct_answers,
        "answered_questions": answered_questions,
        "remaining_lives": lives,
    }


def display_results(player_name: str, result: dict[str, Any]) -> None:
    """Display win/loss status, total points, and remaining lives."""

    print(f"\n{BOLD}{CYAN}===== Game Results ====={RESET}")

    if result["won"]:
        print(f"{GREEN}Congratulations, {player_name}! You won!{RESET}")
    else:
        print(f"{RED}Game over, {player_name}. You lost.{RESET}")

    print(f"{YELLOW}Total points: {result['score']}{RESET}")
    print(f"Correct answers: {result['correct_answers']}")
    print(f"Questions answered: {result['answered_questions']}")
    print(f"{YELLOW}Remaining lives: {result['remaining_lives']}{RESET}")


def play_again() -> bool:
    """Ask whether the player wants to choose a new topic and play again."""

    while True:
        answer = input(
            f"\n{YELLOW}Would you like to play again? (yes/no): {RESET}"
        ).strip().lower()

        if answer in ("yes", "y"):
            return True
        if answer in ("no", "n"):
            print(f"{CYAN}Thanks for playing Wiki Survival!{RESET}")
            return False

        print(f"{RED}Invalid choice. Please enter yes or no.{RESET}")
