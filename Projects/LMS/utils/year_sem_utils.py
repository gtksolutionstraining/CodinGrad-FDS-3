from utils.display_utils import (
    display_sem,
    display_year
)
from config import YEAR,SEM

from utils.input_utils import take_input
def get_year():
    flag = True
    while flag:
        display_year()
        year_choice = take_input()
        if year_choice in [1,2,3,4]:
            return YEAR[year_choice]
        else:
            print("Please select 1,2,3,4")

def get_year_choice():
    flag = True
    while flag:
        display_year()
        year_choice = take_input()
        if year_choice in [1,2,3,4]:
            return year_choice
        else:
            print("Please select 1,2,3,4")

def get_sem():
    flag = True
    while flag:
        display_sem()
        sem_choice = take_input()
        if sem_choice in [1,2]:
            return SEM[sem_choice]
        else:
            print("Please select 1,2")

def get_sem_choice():
    flag = True
    while flag:
        display_sem()
        sem_choice = take_input()
        if sem_choice in [1,2]:
            return sem_choice
        else:
            print("Please select 1,2")

def add_in_sem(LMS,dept,year,sem,book_name,book_id):
    LMS["BOOKS"][dept][year][sem].append({"BOOK_NAME":book_name,"BOOK_ID":book_id})
    print(f"BOOK {book_name} and Book ID {book_id} is added to {dept} {year} {sem}")

def add_in_yr(LMS,dept,year,book_name,book_id):
    sem_choice = get_sem_choice()
    if sem_choice == 1:
        add_in_sem(LMS,dept,year,"1ST_SEM",book_name,book_id)
    elif sem_choice == 2:
        add_in_sem(LMS,dept,year,"2ND_SEM",book_name,book_id)
    else:
        print("Please enter proper 1/2")