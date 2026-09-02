"""Gameplay, results, and replay skeleton for Wiki Survival."""

import os
import time
from pathlib import Path
from typing import Any

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import pygame


STARTING_LIVES = 3
POINTS_PER_CORRECT_ANSWER = 1
RESULT_WIDTH = 60
ASCII_ART_DELAY = 0.08
SOUND_DIRECTORY = Path(__file__).parent / "sounds"
SOUND_FILES = {
    "start": "start.wav",
    "correct": "correct.wav",
    "wrong": "wrong.wav",
    "win": "win.wav",
    "game_over": "game_over.wav",
}

# Basic terminal colors
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

WIN_ART = r"""__   __  ___   _   _    __        __ ___  _   _
\ \ / / / _ \ | | | |   \ \      / /|_ _|| \ | |
 \ V / | | | || | | |    \ \ /\ / /  | | |  \| |
  | |  | |_| || |_| |     \ V  V /   | | | |\  |
  |_|   \___/  \___/       \_/\_/   |___||_| \_|"""

LOSS_ART = r"""  ____    _    __  __ _____    _____     _______ ____
 / ___|  / \  |  \/  | ____|  / _ \ \   / / ____|  _ \
| |  _  / _ \ | |\/| |  _|   | | | \ \ / /|  _| | |_) |
| |_| |/ ___ \| |  | | |___  | |_| |\ V / | |___|  _ <
 \____/_/   \_\_|  |_|_____|  \___/  \_/  |_____|_| \_\
""".rstrip()


def load_sounds() -> dict[str, Any]:
    """Load the game sounds, or return an empty dictionary if audio fails."""

    try:
        pygame.mixer.init()
        return {
            name: pygame.mixer.Sound(SOUND_DIRECTORY / filename)
            for name, filename in SOUND_FILES.items()
        }
    except (FileNotFoundError, NotImplementedError, pygame.error):
        return {}


SOUNDS = load_sounds()


def play_sound(name: str) -> None:
    """Play a game sound when audio is available."""

    sound = SOUNDS.get(name)
    if sound:
        pygame.mixer.stop()
        sound.play()


def animate_ascii_art(art: str, color: str) -> None:
    """Reveal ASCII art one line at a time."""

    for line in art.splitlines():
        print(f"{BOLD}{color}{line}{RESET}", flush=True)
        time.sleep(ASCII_ART_DELAY)


def present_question(
    question: dict[str, Any], question_number: int, total_questions: int
) -> int:
    """Display one question with four choices and return the selected answer."""

    print(
        f"\n{BOLD}{YELLOW}QUESTION {question_number} OF "
        f"{total_questions}{RESET}"
    )
    print(f"{BOLD}{CYAN}{question['question']}{RESET}")

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

    play_sound("start")
    print(f"\n{BOLD}{CYAN}The game begins now, {player_name}!{RESET}")

    for question_number, question in enumerate(questions, start=1):
        selected_answer = present_question(
            question, question_number, len(questions)
        )
        answered_questions += 1

        if check_answer(question, selected_answer):
            score += POINTS_PER_CORRECT_ANSWER
            correct_answers += 1
            play_sound("correct")
            print(f"{GREEN}Correct! You earned 1 point.{RESET}")
        else:
            lives -= 1
            correct_answer = question["correct_answer"]
            correct_number = question["choices"].index(correct_answer) + 1
            play_sound("wrong")
            print(f"{RED}Incorrect!{RESET}")
            print(
                f"{GREEN}The correct answer was: "
                f"{correct_number}. {correct_answer}{RESET}"
            )

            if lives > 0:
                life_word = "life" if lives == 1 else "lives"
                print(f"{YELLOW}You have {lives} {life_word} remaining.{RESET}")

        another_question_remains = answered_questions < len(questions)
        if lives > 0 and another_question_remains:
            input(f"\n{YELLOW}Press enter to continue.{RESET}")

        if lives == 0:
            break

    won = answered_questions == len(questions) and lives > 0

    return {
        "won": won,
        "score": score,
        "correct_answers": correct_answers,
        "answered_questions": answered_questions,
        "total_questions": len(questions),
        "remaining_lives": lives,
    }


def display_results(player_name: str, result: dict[str, Any]) -> None:
    """Display win/loss status, total points, and remaining lives."""

    print(f"\n\n{CYAN}{'=' * RESULT_WIDTH}{RESET}")

    if result["won"]:
        play_sound("win")
        animate_ascii_art(WIN_ART, GREEN)
        print(f"{GREEN}Congratulations, {player_name}! You won!{RESET}")
    else:
        play_sound("game_over")
        animate_ascii_art(LOSS_ART, RED)
        print(f"{RED}Game over, {player_name}. You lost.{RESET}")
        if result["remaining_lives"] == 0:
            print(f"{RED}Reason: You lost all your lives.{RESET}")

    print()
    print(f"{YELLOW}Total points: {result['score']}{RESET}")
    correct = result["correct_answers"]
    total = result["total_questions"]
    print(f"Correct answers: {correct}/{total}")
    print(f"{YELLOW}Remaining lives: {result['remaining_lives']}{RESET}")
    print(f"{CYAN}{'=' * RESULT_WIDTH}{RESET}")


def play_again() -> bool:
    """Ask whether the player wants to choose a new topic and play again."""

    print(f"\n{CYAN}{'-' * RESULT_WIDTH}{RESET}")
    print(f"{BOLD}{CYAN}PLAY AGAIN?{RESET}")

    while True:
        answer = input(
            f"{YELLOW}Would you like to play again? (yes/no): {RESET}"
        ).strip().lower()

        if answer in ("yes", "y"):
            return True
        if answer in ("no", "n"):
            print(f"{CYAN}Thanks for playing Wiki Survival!{RESET}")
            return False

        print(f"{RED}Invalid choice. Please enter yes or no.{RESET}")
