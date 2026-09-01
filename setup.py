"""Player setup skeleton: welcome message, name, and topic choice."""

TOPICS = [
    {"name": "Fish", "wiki_page": "List_of_fish_by_common_name"},
    {"name": "English People", "wiki_page": "List_of_English_people"},
    {"name": "Dinosaur", "wiki_page": "List_of_dinosaur_genera"},
]


def display_welcome() -> None:
    """Display the Wiki Survival welcome message."""

    print("=" * 40)
    print("           WIKI SURVIVAL")
    print("=" * 40)
    print("Test your knowledge and try to survive!")


def get_player_name() -> str:
    """Ask the player to enter their name."""

    name = input("What is your name, adventurer? ")
    return name


def display_game_instructions() -> None:
    """Explain the rules, lives, scoring, and announce the game start."""

    print()
    print("HOW TO PLAY:")
    print(" - Pick a topic you're interested in.")
    print(" - Answer 5 multiple-choice questions.")
    print(" - You start with 3 lives.")
    print(" - Correct answer -> +1 point.")
    print(" - Wrong answer   -> lose 1 life (we show you the answer).")
    print(" - Survive all 5 questions with at least 1 life to WIN!")
    print()
    print("Let the game begin!")
    print("=" * 40)


def choose_topic() -> tuple[str, str]:
    """Display the topics and return the selected name and Wikipedia page."""

    selected_topic = TOPICS[0]
    return selected_topic["name"], selected_topic["wiki_page"]


def announce_round(topic: str) -> None:
    """Announce the beginning of a round for the selected topic."""

    print()
    print("-" * 40)
    print(f"A new round begins! Topic: {topic}")
    print("-" * 40)


# Quick manual test — runs ONLY when you run this file directly
# (python setup.py). It does NOT run when main.py imports this file.
if __name__ == "__main__":
    display_welcome()
    player_name = get_player_name()
    display_game_instructions()
    topic_name, wiki_page = choose_topic()
    announce_round(topic_name)
