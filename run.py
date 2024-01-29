# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials
import random
import emoji
import os
import time

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json") 
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET =GSPREAD_CLIENT.open("tech_quiz")

# quiz = SHEET.worksheet("easy")
# data = quiz.get_all_values()
# print(data)
def pick_quiz_mode():
    """
    Give users to select an easy play mode or hard pay mode
    """
    print("\nWould you like to play EASY mode or HARD mode ? \n")
    print(emoji.emojize(":hatching_chick: 1. EASY"))
    print(emoji.emojize(":chicken: 2. Hard"))

    count = 0
    while count <= 0:
        play_mode = input("Please enter a number 1 or 2 : ")

        if play_mode == "1":
            get_game_data("easy")
            count =+ 1
        elif play_mode == "2":
            get_game_data("hard")
            count += 1
        else:
            print("Input is only valid 1 or 2")
        

def add_quiz():
    print("Add quiz")

def check_score():
    print("Check score")

def select_menu():
    """
    menu selection 
    """
    count = 0
    while count <= 0:
        num_selection = input("Please enter a number between 1 and 3 : ")           
        if num_selection  == "1":
            count += 1
            pick_quiz_mode()
        elif num_selection == "2":
            add_quiz()
            count += 1  
        elif num_selection == "3":
            check_score()
            count += 1
        else:
            print("Input is only valid number between 1 and 3 : ")
            
def show_text_art(file):
    """
    Display text art
    """
    file =open(file)
    get_art = file.read()
    file.close()
    return get_art

def home(): 
    """
    Shows a landing terminal for users to select an option
    """
    art = show_text_art("assets/text-art/techquiz.txt")
    print(art)
    print(emoji.emojize(" :star: Welcome to the Tech Quiz :star: \n"))
    print("This is a study tool for understanding technical knowledge\n")
    print("Please select a number")
    print(emoji.emojize(":triangular_flag: 1  Start Quiz"))
    print(emoji.emojize(":pencil:  2  Add own quiz and answers"))
    print(emoji.emojize(":laptop: 3  Check your score\n"))
    select_menu() 
    

def get_game_data(game_mode):
    """
    Get quiz and answer from spreadsheet 
    """
    print(f"Start {game_mode} mode game! \n") 
    easy_quiz_data =SHEET.worksheet("easy")
    hard_quiz_data =SHEET.worksheet("hard")
    if game_mode == "easy":
        quiz_data = easy_quiz_data.get_all_values()
    else:
        quiz_data = hard_quiz_data.get_all_values() 
    global quiz_material
    quiz_material = quiz_data
    game_start()

def game_start():
    """
    Game starts and display questions and correct answers
    """ 
    os.system("cls") 
    art = show_text_art("assets/text-art/start.txt")
    print(art)
    random_question_num =random.sample(quiz_material,5)
    game_count = 0
    score = 0   
    if game_count <= 5:          
        for x in random_question_num:
            game_count += 1
            print(f"\nQuestion {game_count}\n")
            print(x[0])
            print("\n1.True or 2.False?\n")
            # Reference
            # https://stackoverflow.com/questions/59692444/how-do-create-while-loop-input-for-accept-only-1-or-2-as-input-in-python
            user_answer=0
            try:
                while user_answer not in range(1,3):
                    user_answer = int(input("Pleas Enter a number\n"))
            except:
                print("Enter a number 1 or 2\n")
                user_answer = int(input("Pleas Enter a number\n"))
            
            correct_answer = int(x[1])   
            if user_answer == correct_answer:
                print(emoji.emojize("\n Your answer is correct! :check_mark_button: \n"))
                time.sleep(2)
                score += 20
            else:
                print(emoji.emojize("\n Your answer was wrong :cross_mark:\n"))
                time.sleep(2)
    
    print(emoji.emojize(f":light_bulb: Your score is {score} :light_bulb:\n"))
    time.sleep(2)
    continue_or_home()
    
def continue_or_home():
    """
    User can choose to play again or go back home after completing the game
    """
    print("Do you want to play again?\n")
    user_choice=0
    
    try:
        while user_choice not in range(1,3):
            user_choice = int(input("1. Yes 2. No\n"))
    except:
        print("Enter a number 1 or 2\n")
        user_choice = int(input("1. Yes 2. No\n"))
        
    if user_choice == 1:
        game_start()
    else:
        os.system("cls") 
        home()

home()