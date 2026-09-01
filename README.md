# wiki-survive

Wiki Survival is a console-based Python quiz game where The player starts with 3 lives and chooses a topic from a predefined list. The game fetches related Wikipedia articles and sends the content to OpenAI, which generates a fixed number of multiple-choice questions with answers. Each correct answer earns points, while each wrong answer costs one life. The player wins by completing all questions before losing all 3 lives; otherwise, the game ends

## Walkthrough - step-by-step of game progress:
1) Setup - the game begins with a simple setup stage in which a prompt is presented to the user to provide their name. 
2) Following this initial setup, the user is presented with an explanation of the game, and the game begins. 
3) The user chooses the topics they are interested in and the beginning of the round is announced.
4) We pull a 7  articles from wikipedia related to the user’s selected topics.
5) We send the articles to openAI to generate 5 questions and 4 multiple choice answers (of which only 1 is correct)
6) The user is presented with a question and multiple choice answers to select from correct one.
7) We check if the selected answer is correct. If it is, we present the user with the next question and answer. Else if the answer is wrong the user looses a live and we move on to the next question (but we show them the answer to the previous )
8) This logic (steps 6-7) continues until the player answers all the questions.
9) If the player answers all questions without losing all their lives. Then they won the game. Else if they lose all their lives before answering all questions then they lose the game.
10) Once the game is over we show the user the total points they got for the questions answered and how many lives they have left and an option to play the game again.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/solpreneur/wiki-survive.git
cd wiki-survive
```

### 2. Start the application

```bash
python3 main.py
```
