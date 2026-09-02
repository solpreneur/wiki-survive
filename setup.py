"""Player setup: welcome message, name, instructions, and topic choice."""


TOPICS = [
    {"name": "Fish", "wiki_page": "List_of_fish_by_common_name"},
    {"name": "English People", "wiki_page": "List_of_English_people"},
    {"name": "Dinosaur", "wiki_page": "List_of_dinosaur_genera"},
    {
        "name": "European Geography",
        "wiki_page": "List_of_cities_in_the_European_Union_by_population_within_city_limits",
    },
    {"name": "Bridges", "wiki_page": "Lists_of_bridges"},
]

# Terminal colors (same scheme as the rest of the game)
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

BANNER = r"""
   __        __  ___   _  __  ___
   \ \      / / |_ _| | |/ / |_ _|
    \ \ /\ / /   | |  | ' /   | |
     \ V  V /    | |  | . \   | |
      \_/\_/    |___| |_|\_\ |___|
     S  U  R  V  I  V  A  L
"""


def display_welcome() -> None:
    """Display the Wiki Survival welcome message."""

    print(f"{BOLD}{CYAN}{BANNER}{RESET}")
    print(f"{YELLOW}   Only the sharpest minds make it out alive...{RESET}")
    print(f"{CYAN}{'=' * 44}{RESET}")


def get_player_name() -> str:
    """Ask the player to enter their name."""

    name = input(f"{YELLOW}Speak your name, challenger: {RESET}").strip()
    print(f"{GREEN}Welcome to the arena, {name}!{RESET}")
    return name


def display_game_instructions() -> None:
    """Explain the rules, lives, scoring, and announce the game start."""

    print()
    print(f"{BOLD}{CYAN}HOW TO SURVIVE:{RESET}")
    print(f"  {CYAN}>{RESET} Pick a topic and face 5 brutal questions.")
    print(f"  {CYAN}>{RESET} You get 3 lives. Guard them well.")
    print(f"  {GREEN}>{RESET} Correct answer  ->  +1 point.")
    print(f"  {RED}>{RESET} Wrong answer    ->  lose a life.")
    print(f"  {CYAN}>{RESET} Survive all 5 with a life left, and you WIN.")
    print()
    print(f"{BOLD}{YELLOW}Let the survival begin!{RESET}")
    print(f"{CYAN}{'=' * 44}{RESET}")


def choose_topic() -> tuple[str, str]:
    """Display the topics and return the selected name and Wikipedia page."""

    print(f"\n{BOLD}{CYAN}CHOOSE YOUR BATTLEGROUND:{RESET}")
    for index in range(len(TOPICS)):
        # players see 1, 2, 3..., but the list is indexed 0, 1, 2...
        print(f"  {YELLOW}[{index + 1}]{RESET} {TOPICS[index]['name']}")

    # keep asking until the player enters a valid number from the list
    while True:
        choice = input(f"{YELLOW}Enter your choice: {RESET}").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(TOPICS):
            selected_topic = TOPICS[int(choice) - 1]
            return selected_topic["name"], selected_topic["wiki_page"]
        print(f"{RED}That's not a valid choice. Pick a number from the list.{RESET}")


def announce_round(topic: str) -> None:
    """Announce the beginning of a round for the selected topic."""

    print()
    print(f"{CYAN}{'-' * 44}{RESET}")
    print(f"{BOLD}{GREEN}  THE BATTLE BEGINS  ->  {topic.upper()}{RESET}")
    print(f"{CYAN}{'-' * 44}{RESET}")


# Quick manual test — runs ONLY when you run this file directly
# (python setup.py). It does NOT run when main.py imports this file.
if __name__ == "__main__":
    display_welcome()
    player_name = get_player_name()
    display_game_instructions()
    topic_name, wiki_page = choose_topic()
    announce_round(topic_name)
