# wiki-survive

Wiki Survival is a terminal-based Python experience that tests a player's knowledge through dynamically generated trivia. Starting with a pool of three lives, the participant selects a subject from the available categories. The application then retrieves pertinent data from Wikipedia and utilizes OpenAI to formulate a specific set of multiple-choice queries. Successful responses increase the total score, whereas incorrect selections result in the loss of a life. Victory is achieved by navigating through every question while maintaining at least one life; the game concludes immediately if all lives are exhausted.

## Walkthrough - step-by-step of game progress:
- Setup - the game begins with a simple setup stage in which a prompt is presented to the user to provide their name. 
- Following this initial setup, the user is presented with an explanation of the game, and the game begins. 
- The beginning of the round is announced, and the user chooses the topics they are interested in.
- We pull a fixed amount of articles from wikipedia related to the user’s selected topics.
- We send the articles to openAI to generate the questions and answers
- The user is presented with the questions and multiple choice answers to select from
- We check if the answer is correct. If it is we, present the user with the next questions and answers to selecte from. Else if the answer is wrong the user looses a live and we move on to the next question (but we show them the answer to the previous )
- This logic (steps 6-7) continues until the player answers all the questions.
- If the player answers all questions without losing all their lives. Then they won the game. Else if they lose all their lives before answering all questions then they lose.
- Once the game is over we show the user the total points they got for the questions answered and how many lives they have left and an option to play again
