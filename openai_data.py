"""OpenAI question-generation skeleton for Wiki Survival."""

import json
import wiki_data
import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


def generate_questions(articles: list[Article]) -> list[dict]:
    """Generate one four-choice question for each of five articles.

    Every generated question should contain four possible answers and exactly
    one correct answer.
    """

    openai_client = OpenAI()
    selected_model = os.getenv("OPENAI_MODEL","gpt-5-nano")

    instructions = (
        "You are a quiz-question generator for a terminal Python game called Wiki Survival. "
        "Your task is to create multiple-choice trivia questions from the provided Wikipedia article data. "
        "Create exactly one question for each article. "
        "Use only the article title and summary. "
        "Do not invent facts. "
        "Do not mention 'according to the summary' or 'according to the article'. "
        "Each question must have exactly 4 answer choices. "
        "The correct_answer must be exactly one of the choices. Randomize the order of the answer choices. so the answer is not always the first choice. "
        "Return ONLY valid JSON. "
        "Do not use markdown. "
        "Do not wrap the JSON in ```json. "
        "Do not add explanation before or after the JSON. "
        "Return this exact JSON shape: "
        "{"
        "\"questions\": ["
        "{"
        "\"source_title\": \"Article title here\", "
        "\"question\": \"Question text here?\", "
        "\"choices\": [\"choice A\", \"choice B\", \"choice C\", \"choice D\"], "
        "\"correct_answer\": \"one exact choice from choices\""
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



    return json.loads(response.output_text)["questions"]

#print(str(generate_questions(wiki_data.get_wikipedia_articles("",5,7))))