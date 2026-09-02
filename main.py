"""Application entry-point skeleton for Wiki Survival."""

from game_play import display_results, play_again, play_game
from openai_data import generate_questions
from setup import (
    announce_round,
    choose_topic,
    display_game_instructions,
    display_welcome,
    get_player_name,
)
from wiki_data import get_wikipedia_articles


def main() -> None:
    """Coordinate setup, content loading, gameplay, results, and replay."""

    print("Wiki Survival")

    # 1. Use setup.py for the welcome, player name, and instructions.
    display_welcome()
    player_name = get_player_name()
    display_game_instructions()

    while True:
        topic, wiki_page = choose_topic()
        announce_round(topic)

        # Search seven candidates and return five usable article summaries.
        print("\nLoading articles from Wikipedia...", flush=True)
        articles = get_wikipedia_articles(wiki_page)

        # Generate five questions with four choices and one correct answer.
        print("Generating questions. Please wait...", flush=True)
        questions = generate_questions(articles)

        # Run the game, show results, and offer replay.
        result = play_game(player_name, questions)
        display_results(player_name, result)

        if not play_again():
            break


if __name__ == "__main__":
    main()
