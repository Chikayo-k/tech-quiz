# Tech Quiz

![Responsive image](assets/image/am-i-responsive.png)
GitHub https://github.com/Chikayo-k/tech-quiz

## Project Goals

The goal of this project is to create a simple and interactive Python game where users can test their programming skills and knowledge.

## Target Audience

- Students studying in the Software Development and Engineering
- Professionals looking to up skills in new technology stacks
- Teachers as a means to help students learn the basics of programming

## User Goals

- Students looking to learn programming knowledge
- Teachers as a learning tool in the classroom
- Professionals looking to learn new knowledge and up-skill
- Short focused quiz to help build programming knowledge
- Provides users with different levels of difficulty
- Provides users with the option to create their own quizzes

## User Stories

Game

1. As a user I want to build my knowledge around programming terms and topics
2. As a user I want to see the menu so I can select an option
3. As a user I want to be able to track my attempts
4. As a user I want to be able to have different levels of difficulty to help me progress.
5. As a user I want to be able to build my own quizzes to learn new things
6. As a user I want a simple experience when answering questions.
7. As a user I want instant visual feedback when answering questions.
8. As a user I want to see my score at the end of each round.

Scoreboard

9. As a user I want to see my scores
10. As a user I want to see my average score

Adding Questions

11. As a user I want to add new questions
12. As a user I want to choose the level where the questions will go
13. As a user I want easy navigation when adding questions
14. As a user I want to see a success message to let me know that a question has been added to the quiz

## Features To Achieve These Goals

Game

1. Provide a technical quiz game
2. Provide users with a menu.
3. Provide users with a scorer board to track the attempts
4. Provide different levels of difficulty
5. Provide users the option to add their questions and add them to the existing quizzes
6. Provide a simple and quick way of answering questions
7. Provide visual feedback in the form of emojis.
8. Provide the user with their score at the end of each set of questions

Scoreboard

9. Provide the last 5 scores.
10. Provide the user with an average score from the last 5 attempts

Adding Questions

11. Provide the user with the option to add new questions to the quiz
12. Provide the user the option where to add the questions in the easy or hard quizzes
13. Provide the user simple way to add questions
14. Provide the user with a message so they know the questions has been added successfully.

## Features

### Home Screen

- Has a welcome message to users what the application is for.
- Display the home screen menu
- Gives the user 3 options to choose from
- The three options are to start the game, Check their score or add questions to create their own quiz.

Using text art and emojis the user can get the feeling it is a game. The welcome screen shows the user what kind of quiz this is and what they can expect.  
The game was designed so that users can enjoy the quiz with minimal input. Using only the number pad they can choose from 3 different options.

![Home image](assets/image/fetures/home.png)

### Start Quiz

- Easy mode
- Hard mode

The user can select from either easy or hard depending on their skill level. The questions will be pulled from an external spreadsheet using the google spreadsheet API. Which contains sets of questions for each.

![Play mode image](assets/image/fetures/play-mode.png)

- Display text art
- The questions will display on the screen and ask the user to enter either true or false by choosing either 1 or 2.

Using text art the user can see this is the start of the game.
This is again to simplify the user's experience by only having 2 options to choose from.

![Start image](assets/image/fetures/start.png)

- When the user selects a correct answer they will see a short message with a green tick to let them know it's right
- When the user selects an incorrect answer they will see a short message with a red x to let them know it's wrong
- Provides the user with a short description of the answer.
- Enter to next question

This will allow the user to see if they are making progress in the quiz by showing either a green tick or a red x and provide them with clear and quick feedback.
From the short description, the user can learn a bit more about the topic.
The enter next question will let the user stay and read the description for as long as they want.

Collect  
![Question-Collect image](assets/image/fetures/question.png)

Wrong  
![Wrong image](assets/image/fetures/wrong.png)

- Text art to show the user they are on the score section
- Show the score at the end of the game
- Ask the user if they would like to play again

This will let the user see the progress they are making at the end of each game. It uses the number pad to simplify the selection for the users. By adding in text art and emojis it gives the user the feel of a game.

![Score image](assets/image/fetures/score.png)

### Add Quiz

- Text art to show the user they are on the add quiz section
- Ask the user what mode of the quiz they want to add a question to or go back to the home screen.

Users will see that this is the add quiz section by looking at the text art.
Users will have the option to add questions to either the easy or hard mode.
Having a home button increases user's accessibility in the game

![Add quiz image](assets/image/fetures/add-quiz.png)

Display the “Please enter a question here” shows clearly what needs to be entered here.
The lead message shows on the screen which provides easy navigation for users

![Lead message 1](assets/image/fetures/lead1.png)

Once a user has entered a question they will need to set the answer to be true or false. This is done by simply selecting either 1 or 2

![Lead message 2](assets/image/fetures/lead2.png)

Description can be added. This is users choice.

![Lead message 3](assets/image/fetures/lead3.png)

When a question's answer and description have been successfully set it will display a success message. Which user can see the input feedback?

![Confirmation image](assets/image/fetures/confirmation.png)

After adding a question the user will be asked if they would like to add another question that lets the user add as many questions as they want.

![Lead message 4](assets/image/fetures/lead4.png)

### Scoreboard

- Text art shows this is the score section.
- This will display the last five score attempts the user has made.
- The scores are ordered from oldest to newest with the oldest attempt being no 1 and the last attempt being no 5.
- There is an average score calculated by the last five scores.
- User can return home by entering the enter key.

Users will see this is the score section from the text art.  
Users will be able to track the attempts they have made and see how they are doing.  
User will be able to see their scores in a list from the oldest down to the newest.  
Users can see the average which can help give them an idea of how they are doing on the quizzes.  
Users can simply navigate to the home screen by hitting the enter key.

![Scoreboard](assets/image/fetures/scoreboard.png)

## Data Model

A Google Sheet was used to store the game data.
There are three worksheets for easy game mode, hard game mode and the score to store.

![Google sheets](assets/image/google-sheets.png)

## Technologies

- Python 3
- Google spreadsheet API
- Heroku - backend deployment
- GitHub - version and source control

## Testing / Bugs

### Python Linter

White space, and blank lines issues are solved by using [Python formatter](https://codebeautify.org/python-formatter-beautifier).

![Linter test 1](assets/image/testing/linter-test1.png)

The E501 error came up because the code was being too long.
I fixed the error by adjusting the word of the length.

![Linter test 2](assets/image/testing/linter-test2.png)

There was an error in using bare except.

![Bare expect issue](assets/image/testing/bare-expect.png)

To fix it, catch the errors with Valid error “as” e.
This solved the issue when testing.

![Bare expect fixed](assets/image/testing/bare-expext-fixed.png)

The bare expect issue was fixed but when the user does not type numbers more than twice the error shows up and the game will be stopped. Finally, this was resolved by using the if elif statement.

![fixed error](assets/image/testing/error-fixed.png)

All the errors are fixed. Now there is no error.

![Python Linter test (NO error)](assets/image/testing/test-no-error.png)

## Browser Test

The application is deployed using Heroku as part of testing the deployed version of the application It was checked on Google Chrome, Edge, and Firefox and all worked and functioned as expected.
