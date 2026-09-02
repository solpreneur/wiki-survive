import random
import textwrap

RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"


DID_YOU_KNOW_FACTS = [
    "Octopuses have three hearts, blue blood, and no bones, which helps them squeeze through extremely small spaces.",
    "Elephants can recognize themselves in mirrors, which is a sign of advanced self-awareness.",
    "Crows can remember human faces and may warn other crows about people they see as dangerous.",
    "Honeybees communicate by dancing, using movements to show other bees where food can be found.",
    "Dolphins have unique whistle sounds that can work a little bit like names for identifying each other.",
    "Penguins can jump out of the water like rockets to escape predators and land on ice.",
    "Some turtles can live for more than 100 years, making them among the longest-living animals on Earth.",
    "Axolotls can regrow body parts, including legs, tails, and even parts of their heart and brain.",
    "The mantis shrimp can punch so fast that the water around its claw briefly creates tiny bubbles of heat and light.",
    "Whales sing complex songs underwater, and some whale songs can travel very long distances through the ocean.",
    "A group of flamingos is called a flamboyance, which sounds almost as colorful as the birds look.",
    "Ants can build huge underground cities with tunnels, storage rooms, and special areas for the queen and young ants.",
    "Cats can rotate their ears separately, which helps them detect sounds from different directions very quickly.",
    "Dogs have a sense of smell so powerful that they can be trained to detect diseases, explosives, and missing people.",
    "Giraffes have the same number of neck bones as humans, but each bone is much longer.",
    "Marie Curie was the first person to win two Nobel Prizes, and she won them in two different scientific fields.",
    "Albert Einstein changed how people understood space, time, light, and gravity.",
    "Leonardo da Vinci was not only a painter, but also studied anatomy, engineering, flight, water systems, and machines.",
    "Ada Lovelace is often remembered as one of the first computer programmers, even though she lived long before modern computers existed.",
    "Nelson Mandela spent 27 years in prison before becoming president of South Africa and a global symbol of resistance and reconciliation.",
    "Beethoven continued composing music even after he began losing his hearing.",
    "Amelia Earhart became one of the most famous pilots in history because she challenged expectations about what women could do in aviation.",
    "Nikola Tesla imagined wireless communication, remote control, and electrical systems when many of these ideas sounded impossible.",
    "Ibn al-Haytham made important contributions to optics by studying how light and vision work.",
    "Malala Yousafzai became the youngest Nobel Peace Prize winner for her activism supporting girls education.",
    "Isaac Newton studied gravity, motion, light, mathematics, and astronomy, and his ideas shaped science for centuries.",
    "Cleopatra lived closer in time to the invention of the smartphone than to the building of the Great Pyramid of Giza.",
    "Charles Darwin developed the theory of evolution by natural selection after years of observing animals, fossils, and nature.",
    "Katherine Johnson helped calculate important spaceflight paths for NASA.",
    "Martin Luther King Jr. was only 39 years old when he died, but his speeches and civil rights work changed history around the world.",
]


def print_wrapped_text(text, width=70):
    lines = textwrap.wrap(text, width=width)

    for line in lines:
        print(line)


def show_loading_fact():
    fact = random.choice(DID_YOU_KNOW_FACTS)

    print()
    print(CYAN + "=" * 72 + RESET)
    print(YELLOW + BOLD + "🧠 BEFORE THE GAME STARTS..." + RESET)
    print(CYAN + "=" * 72 + RESET)
    print()
    print(GREEN + BOLD + "Did you know?" + RESET)
    print()
    print_wrapped_text(fact)
    print()
    print(MAGENTA + "Your quiz is loading. Check if you already knew this..." + RESET)
    print(CYAN + "=" * 72 + RESET)
    print()