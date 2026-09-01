"""Player setup skeleton: welcome message, name, and topic choice."""

TOPICS = [
    {"name": "Fish", "wiki_page": "List_of_fish_by_common_name"},
    {"name": "English People", "wiki_page": "List_of_English_people"},
    {"name": "Dinosaur", "wiki_page": "List_of_dinosaur_genera"},
]


def display_welcome() -> None:
    """Display the Wiki Survival welcome message."""

    pass


def get_player_name() -> str:
    """Ask the player to enter their name."""

    pass


def display_game_instructions() -> None:
    """Explain the rules, lives, scoring, and announce the game start."""

    pass


def choose_topic() -> tuple[str, str]:
    """Display the topics and return the selected name and Wikipedia page."""

    selected_topic = TOPICS[0]
    return selected_topic["name"], selected_topic["wiki_page"]


def announce_round(topic: str) -> None:
    """Announce the beginning of a round for the selected topic."""

    pass
