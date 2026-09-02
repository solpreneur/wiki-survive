"""OpenAI question-generation skeleton for Wiki Survival."""

import json
import wiki_data
import re
from loading_facts import show_loading_fact
import random
import time
from wiki_data import Article
import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
#articles=[{'title': 'Protorosaurus belli', 'summary': 'Chasmosaurus ( KAZ-moh-SOR-əs) is a genus of ceratopsid dinosaur from the Late Cretaceous Period in North America'}, {'title': 'Kukufeldia', 'summary': 'Barilium is a genus of iguanodontian dinosaur which was first described as a species of Iguanodon (I'}, {'title': 'Choconsaurus', 'summary': 'Choconsaurus ("El Chocón lizard") is an extinct genus of herbivorous sauropod dinosaur belonging to the group Titanosauriformes, which lived in the area of present-day Argentina during the Early Cretaceous'}, {'title': 'Paranthodon', 'summary': 'Paranthodon ( pə-RAN-thə-don) is a genus of stegosaurian dinosaur that lived in what is now South Africa during the Early Cretaceous, between 139 and 131 million years ago'}, {'title': 'Melanorosaurus', 'summary': 'Melanorosaurus (meaning "Black Mountain Lizard", from the Greek melas/μέλας, "black", oros/ὄρος, "mountain" + sauros/σαῦρος, "lizard") is a genus of basal sauropodomorph dinosaur that lived during the Late Triassic period'}]
BAD_QUESTION_PHRASES = [
    r"^according to the summary,?\s*",
    r"^according to the article,?\s*",
    r"^according to the list,?\s*",
    r"^based on the summary,?\s*",
    r"^based on the article,?\s*",
    r"^based on the list,?\s*",
    r"^mentioned in the summary,?\s*",
    r"^mentioned in the article,?\s*",
    r"^mentioned in the list,?\s*",
    r"^the summary says that\s*",
    r"^the article says that\s*",
    r"^the list says that\s*",
]

def clean_question_text(text):
    for phrase in BAD_QUESTION_PHRASES:
        text = re.sub(phrase, "", text, flags=re.IGNORECASE)

    text = text.strip()

    if text:
        text = text[0].upper() + text[1:]

    return text


def clean_questions(questions):
    for question in questions:
        question["question"] = clean_question_text(question["question"])

    return questions

def generate_questions(articles: list[wiki_data.Article]) -> list[dict]:
    """Generate one four-choice question for each of five articles.

    Every generated question should contain four possible answers and exactly
    one correct answer.
    """
    show_loading_fact()
    openai_client = OpenAI()
    selected_model = os.getenv("OPENAI_MODEL","gpt-5-nano")

    instructions = (
        "You are a quiz-question generator for a terminal Python game called Wiki Survival. "
        "Your task is to create multiple-choice trivia questions from the provided Wikipedia article data. "
        "Create exactly one question for each article. "
        "Use only the article title and one-sentence summary. "
        "Do not invent facts. "
        "Write natural quiz questions only. "

        "Very important question rules: "
        "Do not repeat the same question idea. "
        "Each question must test a different fact or detail. "
        "Do not create two questions with the same meaning. "
        "Do not use nearly identical wording between questions. "
        "Never start a question with 'According to the summary'. "
        "Never start a question with 'According to the article'. "
        "Never start a question with 'Based on the summary'. "
        "Never start a question with 'Based on the article'. "
        "Do not use the words 'summary' or 'article' inside the question text. "
        "Very important answer-choice rules: "
        "Each question must have exactly 4 answer choices. "
        "The correct_answer must be exactly one of the choices. Randomize the order of the answer choices. so the answer is not always the first choice. "
        "Write natural quiz questions only. "
        "Very important question rules: "
        "Do not repeat the same question idea. "
        "Each question must test a different fact or detail. "
        "Do not create two questions with the same meaning. "
        "Do not use nearly identical wording between questions. "
        "Never start a question with 'According to the summary'. "
        "Never start a question with 'According to the article'. "
        "Never start a question with 'Based on the summary'. "
        "Never start a question with 'Based on the article'. "
        "Do not use the words 'summary' or 'article' inside the question text. "
        "Very important answer-choice rules: "
        "Each question must have exactly 4 answer choices. "
        "All 4 choices must be unique. "
        "Each choice must be short and clear. "
        "The correct_answer must be exactly one of the choices. "
        "Do not put the correct answer always in the same position. "
        "Shuffle the position of the correct answer"
        "Distribute correct answers across different positions. "
        "For multiple questions, vary the correct answer position as much as possible. "
        "Example: if there are 5 questions, the correct answers should appear in different positions like A, C, B, D, A or similar. "
        "Example: This is a good example shuffle of answers, A,C,B,D,C "
        "Example: This is a bad example shuffle of answers, A,C,A,A,A "
        "Example: This is a good example shuffle of answers, C,D,A,C,B "
        "Example: This is a bad example shuffle of answers, B,B,C,B,C "
        "A must not be the correct answer more than 2 times"
        "B must not be the correct answer more than 2 times"
        "C must not be the correct answer more than 2 times"
        "D must not be the correct answer more than 2 times"
        "Return ONLY valid JSON. "
        "Do not use markdown. "
        "Do not wrap the JSON in ```json. "
        "Do not add explanation before or after the JSON. "

        "Return this exact JSON shape: "
        "{"
        "\"questions\": ["
        "{"
        "\"source_title\": \"Article title here\", "
        "\"question\": \"Natural unique quiz question here?\", "
        "\"choices\": [\"choice A\", \"choice B\", \"choice C\", \"choice D\"], "
        "\"correct_answer\": \"exact text of the correct choice\""
        "}"
        "]"
        "}"
    )

    article_input = (
        "Generate quiz questions from this JSON article data\n"
        + json.dumps(articles, ensure_ascii=False, indent=2)
    )

    response = openai_client.responses.parse(
            model=selected_model,
            instructions=instructions,
            input=article_input,
    )

    data = json.loads(response.output_text)
    questions = data["questions"]
    questions = clean_questions(questions)
    questions = mix_answer_positions(questions)
    return questions

#print(str(generate_questions(articles)))

def mix_answer_positions(questions):
    positions = [0, 1, 2, 3] * 10
    random.shuffle(positions)

    for question, correct_position in zip(questions, positions):
        correct_answer = question["correct_answer"]

        wrong_choices = []

        for choice in question["choices"]:
            if choice != correct_answer:
                wrong_choices.append(choice)

        random.shuffle(wrong_choices)

        new_choices = wrong_choices
        new_choices.insert(correct_position, correct_answer)

        question["choices"] = new_choices

    return questions


