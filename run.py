import gspread
from google.oauth2.service_account import Credentials
import random
import emoji
import os
import time
from functools import reduce
import numpy as np
import math

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("tech_quiz")

score_sheet = SHEET.worksheet("score")


def show_text_art(file):
    """
    Display text art
    """
    file = open(file)
    get_art = file.read()
    file.close()
    return get_art


# --------------------Check Score---------------------------


class ScoreBoard:
    """
    Creates an instance of score
    """

    def __init__(self, scores):
        self.scores = scores

    def refresh_data(self):
        """
        Refresh data from spread sheet
        """
        self.scores

    def display_latest_five(self):
        """
        Get the latest five scores
        """
        last_five = self.scores[-5:]
        # Reference
        # https://stackoverflow.com/questions/17485747/how-to-convert-a-nested-list-into-a-one-dimensional-list-in-python
        global five_in_list
        five_in_list = reduce(lambda x, y: x + y, last_five)
        counts = 1
        for num in five_in_list:
            print(f"{counts}: {num}")
            counts += 1

    def display_average(self):
        """
        Display average score calculated by last five scores
        """
        list_int = [eval(num) for num in five_in_list]
        sum_scores = sum(list_int)
        average = sum_scores / 5
        average = math.floor(average)
        print("\nAverage score calculated by last five scores is\n")
        print("----------")
        print(f"    {average}")
        print("----------")


def check_score():
    """
    Scoreboard related functions are called and display
    """
    os.system("clear")
    art = show_text_art("assets/text-art/score.txt")
    print(art)
    print("-----------------------------------\n")
    score_data = score_sheet.get_all_values()
    score = ScoreBoard(score_data)
    score.refresh_data()
    score.display_latest_five()
    score.display_average()
    input("\nEnter to home\n")
    home()


# -----------------------Add Quiz-----------------------------


def ask_add_question():
    """
    Users can create a new quiz
    """
    os.system("clear")
    print("Add quiz")
    art = show_text_art("assets/text-art/add-quiz.txt")
    print(art)
    global enter_question
    global enter_answer
    global enter_description
    global mode

    # Ask user to pick easy mode or hard mode to add a question
    count = 0
    while count == 0:
        print("Choose a quiz mode")
        mode_choice = input("1. Easy or 2. Hard 3. Home\n")
        if mode_choice == "1":
            mode = "easy"
            count += 1
        elif mode_choice == "2":
            mode = "hard"
            count += 1
        elif mode_choice == "3":
            os.system("clear")
            home()
        else:
            time.sleep(1)
            print("Please enter a number between 1 or 2\n")
            time.sleep(2)
            os.system("clear")

    # ask to add a new question
    os.system("clear")
    enter_question = input("Please enter a question here\n")
    time.sleep(1)
    print("Success!")
    time.sleep(1)
    os.system("clear")

    # ask to add an answer to the question
    answer_count = 0
    while answer_count == 0:
        print("Pick 1.TRUE or 2.FALSE for the answer\n")
        enter_answer = input("Enter a number here\n")
        if enter_answer == "1":
            time.sleep(1)
            print("Success!")
            time.sleep(1)
            answer_count += 1
        elif enter_answer == "2":
            time.sleep(1)
            print("Success!")
            time.sleep(1)
            answer_count += 1
        else:
            time.sleep(1)
            print("Please enter a number between 1 and 2\n")
            time.sleep(1)
            os.system("clear")

    # ask to add description for the question
    os.system("clear")
    enter_description = input("Add description of the question\n")
    time.sleep(1)
    print("Success!")
    time.sleep(1)
    os.system("clear")


class Question:
    def __init__(self, enter_question, enter_answer, enter_description):
        """
        Creates an instance of score
        """
        self.question = enter_question
        self.answer = enter_answer
        self.description = enter_description

    def user_input_quiz(self):
        """
        Display quiz that user input
        """
        time.sleep(1)
        user_question = f"Question: {self.question}\n"
        user_answer = f"Answer: {self.answer}\n"
        user_description = f"description: {self.description}\n"
        return user_question + user_answer + user_description

    def add_to_spreadsheet(self, mode):
        """
        Add the quiz to the google spread sheet
        """
        score_sheet = SHEET.worksheet(mode)
        score_sheet.append_row([self.question, self.answer, self.description])


def confirmation_add_quiz():
    """
    Ask users if they want to add a new quiz they made
    """
    count = 0
    while count == 0:
        print("Are you ok to add this question ?\n")
        print("1.Yes 2.No")
        answer = input("Please enter a number here\n")
        if answer == "1":
            time.sleep(1)
            print("Your question is added!!")
            count = +1
        elif answer == "2":
            ask_add_question()
        else:
            print("Please Enter a number 1 or 2")


def ask_more_question():
    """
    Ask users if there is more questions to add
    """
    count = 0
    while count == 0:
        os.system("clear")
        print("Do you want to add more question ?")
        answer = input("1.Yes 2.Home\n")
        if answer == "1":
            ask_add_question()
            count += 1
            add_question()
        elif answer == "2":
            os.system("clear")
            home()
            count += 1
        else:
            print("Please Enter a number 1 or 2")


def add_question():
    """
    Add question related functions are called to display
    """
    question = Question(enter_question, enter_answer, enter_description)
    print(question.user_input_quiz())
    confirmation_add_quiz()
    question.add_to_spreadsheet(mode)
    ask_more_question()


# ------------------------- Game ------------------------------


def home():
    """
    Shows a landing terminal for users to select an option
    """
    os.system("clear")
    art = show_text_art("assets/text-art/techquiz.txt")
    print(art)
    print(emoji.emojize(" :star:Welcome to the Tech Quiz:star: \n"))
    print("This is a study tool for learning technical knowledge\n")
    print("----------  Menu  ----------\n")
    print(emoji.emojize(":triangular_flag: ---1 Start Quiz"))
    print(emoji.emojize(":pencil: ---2 Add your own quiz and answers"))
    print(emoji.emojize(":laptop: ---3 Check your score\n"))
    select_menu()


def pick_quiz_mode():
    """
    Difficulty selection
    """
    os.system("clear")
    print("\n----------  Play Mode ----------\n")
    print("\nWould you like to play EASY mode or HARD mode ? \n")
    print(emoji.emojize(":hatching_chick: 1. Easy"))
    print(emoji.emojize(":chicken: 2. Hard\n"))

    count = 0
    while count <= 0:
        play_mode = input("Please enter a number 1 or 2 :\n")

        if play_mode == "1":
            get_game_data("easy")
            count = +1
        elif play_mode == "2":
            get_game_data("hard")
            count += 1
        else:
            print("Invalid input please select 1 or 2\n")
    game_start()


def select_menu():
    """
    menu selection
    """
    count = 0
    while count <= 0:
        num_selection = input("Please enter a number between 1 and 3 :\n")
        if num_selection == "1":
            count += 1
            pick_quiz_mode()
        elif num_selection == "2":
            ask_add_question()
            add_question()
            count += 1
        elif num_selection == "3":
            check_score()
            count += 1
        else:
            print("Invalid input please select between 1 and 3 : ")


def get_game_data(game_mode):
    """
    Get quiz questions and answers from spreadsheet
    """
    print(f"Start {game_mode} mode! \n")
    easy_quiz_data = SHEET.worksheet("easy")
    hard_quiz_data = SHEET.worksheet("hard")
    if game_mode == "easy":
        quiz_data = easy_quiz_data.get_all_values()
    else:
        quiz_data = hard_quiz_data.get_all_values()
    global quiz_material
    quiz_material = quiz_data


def game_start():
    """
    Game starts and display questions and correct answers
    """
    os.system("clear")
    art = show_text_art("assets/text-art/start.txt")
    print(art)
    random_question_num = random.sample(quiz_material, 5)
    game_count = 0
    score = 0
    if game_count <= 5:
        for x in random_question_num:
            game_count += 1
            print(f"\nQuestion {game_count}\n")
            print(x[0])
            print("\n1.True or 2.False?\n")
            user_answer = 0
            try_count = 0
            user_answer = input("Please enter a number 1 or 2:\n")
            while try_count == 0:
                if user_answer == "1":
                    user_answer = 1
                    try_count += 1
                elif user_answer == "2":
                    user_answer = 2
                    try_count += 1
                else:
                    user_answer = input("Please enter a number 1 or 2:\n")

            correct_answer = int(x[1])
            if user_answer == correct_answer:
                time.sleep(1)
                print(emoji.emojize("\n Correct! :check_mark_button: \n"))
                time.sleep(1)
                print(x[2])
                score += 20
                time.sleep(1)
                input("\nHit enter to continue\n")
                os.system("clear")
            else:
                time.sleep(1)
                print(emoji.emojize("\n Wrong :cross_mark:\n"))
                time.sleep(1)
                print(x[2])
                time.sleep(1)
                input("\nHit enter to continue\n")
                os.system("clear")

    art = show_text_art("assets/text-art/score.txt")
    print(art)
    print(emoji.emojize(f":light_bulb: Your score is {score}:light_bulb:\n"))
    score_sheet.append_row([score])
    time.sleep(2)
    continue_or_home()


def continue_or_home():
    """
    User can choose to play again or
    go back to the starting page after completing the game
    """
    print("Do you want to play again?\n")
    user_choice = 0
    count = 0
    user_choice = input("1. Yes 2. No\n")

    while count == 0:
        if user_choice == "1":
            user_choice = 1
            count += 1
        elif user_choice == "2":
            user_choice = 2
            count += 1
        else:
            print("Please enter a number 1 or 2")
            user_choice = input("1. Yes 2. No\n")

    if user_choice == 1:
        game_start()
    else:
        os.system("clear")
        home()


if __name__ == "__main__":
    try:
        home()
    except KeyboardInterrupt:
        os.system("clear")
        home()
