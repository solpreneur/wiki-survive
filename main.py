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
        topic = choose_topic()
        announce_round(topic)

        print(f"\nWelcome, {player_name}!")
        print(f"Your selected topic is: {topic}")

        # 4. Search seven candidates and return five usable article summaries.
        articles = get_wikipedia_articles(topic)

        # 5. Generate five questions with four choices and one correct answer.
        questions = generate_questions(articles)

        # 6-10. Run the game, show results, and offer replay.
        result = play_game(player_name, questions)
        display_results(player_name, result)

        if not play_again():
            break


if __name__ == "__main__":
    main()
