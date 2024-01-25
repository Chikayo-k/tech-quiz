# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials

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

def start_quiz():
    print("Start quiz")

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
            start_quiz()
        elif num_selection == "2":
            add_quiz()
            count += 1  
        elif num_selection == "3":
            check_score()
            count += 1
        else:
            print("Input is only valid number between 1 and 3")
           

def home(): 
    """
    Shows a landing terminal for users to select an option
    """
    print("Welcome to the Tech Quiz\n")
    print("This is a study tool for understanding technical knowledge\n")
    print("Please select a number")
    print("1. Start Quiz")
    print("2. Add own quiz and answers")
    print("3, Check your score\n")
    select_menu()  
        
        


home()