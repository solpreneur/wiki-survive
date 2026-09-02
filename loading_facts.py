import random
DID_YOU_KNOW_FACTS = [
    "Did you know that octopuses have three hearts, blue blood, and can squeeze through tiny spaces because they have no bones?",
    "Did you know that elephants can recognize themselves in mirrors, which is a sign of advanced self-awareness?",
    "Did you know that crows can remember human faces and may even warn other crows about people they see as dangerous?",
    "Did you know that honeybees communicate by dancing, using movements to show other bees where food can be found?",
    "Did you know that dolphins have unique whistle sounds that work a little bit like names for identifying each other?",
    "Did you know that penguins can jump out of the water like rockets to escape predators and land on ice?",
    "Did you know that some turtles can live for more than 100 years, making them among the longest-living animals on Earth?",
    "Did you know that axolotls can regrow body parts, including legs, tails, and even parts of their heart and brain?",
    "Did you know that the mantis shrimp can punch so fast that the water around its claw briefly creates tiny bubbles of heat and light?",
    "Did you know that whales sing complex songs underwater, and some whale songs can travel for very long distances through the ocean?",
    "Did you know that a group of flamingos is called a flamboyance, which sounds almost as colorful as the birds look?",
    "Did you know that ants can build huge underground cities with tunnels, storage rooms, and special areas for the queen and young ants?",
    "Did you know that cats can rotate their ears separately, which helps them detect sounds from different directions very quickly?",
    "Did you know that dogs have a sense of smell so powerful that they can be trained to detect diseases, explosives, and missing people?",
    "Did you know that giraffes have the same number of neck bones as humans, but each bone is much longer?",
    "Did you know that Marie Curie was the first person to win two Nobel Prizes, and she won them in two different scientific fields?",
    "Did you know that Albert Einstein did not become famous only because of one idea, but because he changed how people understood space, time, light, and gravity?",
    "Did you know that Leonardo da Vinci was not only a painter, but also studied anatomy, engineering, flight, weapons, water systems, and machines?",
    "Did you know that Ada Lovelace is often remembered as one of the first computer programmers, even though she lived long before modern computers existed?",
    "Did you know that Nelson Mandela spent 27 years in prison before becoming president of South Africa and a global symbol of resistance and reconciliation?",
    "Did you know that Beethoven continued composing music even after he began losing his hearing, creating some of his greatest works while almost completely deaf?",
    "Did you know that Amelia Earhart became one of the most famous pilots in history because she challenged expectations about what women could do in aviation?",
    "Did you know that Nikola Tesla imagined wireless communication, remote control, and electrical systems at a time when many of these ideas sounded impossible?",
    "Did you know that Ibn al-Haytham made important contributions to optics and the scientific method by studying how light and vision work?",
    "Did you know that Malala Yousafzai became the youngest Nobel Peace Prize winner for her activism supporting girls education?",
    "Did you know that Isaac Newton studied gravity, motion, light, mathematics, and astronomy, and his ideas shaped science for centuries?",
    "Did you know that Cleopatra lived closer in time to the invention of the smartphone than to the building of the Great Pyramid of Giza?",
    "Did you know that Charles Darwin developed the theory of evolution by natural selection after years of observing animals, fossils, and nature?",
    "Did you know that Katherine Johnson helped calculate important spaceflight paths for NASA, and her math supported missions that sent astronauts into space?",
    "Did you know that Martin Luther King Jr. was only 39 years old when he died, but his speeches and civil rights work changed history around the world?",
]
def get_random_fact():
    return random.choice(DID_YOU_KNOW_FACTS)
def show_loading_fact():
    fact = get_random_fact()

    print("=" * 50)
    print("DID YOU KNOW?")
    print("=" * 50)
    print()
    print(fact)
    print()
    print("Generating your Wiki Survival questions...")
    print("=" * 50, flush=True)