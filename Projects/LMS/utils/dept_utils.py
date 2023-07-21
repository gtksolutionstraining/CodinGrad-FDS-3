from utils.year_sem_utils import (
    get_year_choice,
    add_in_yr
)
from utils.display_utils import display_dept
from utils.input_utils import take_input
from config import DEPT

def get_dept():
    flag = True
    while flag:
        display_dept()
        dept_choice = take_input()
        if dept_choice in [1,2,3,4,5]:
            return DEPT[dept_choice]
        else:
            print("Please select 1,2,3,4,5")

def get_dept_choice():
    flag = True
    while flag:
        display_dept()
        dept_choice = take_input()
        if dept_choice in [1,2,3,4,5,6]:
            return dept_choice
        else:
            print("Please select 1,2,3,4,5")

def add_in_dept(LMS,dept,book_name,book_id):
    year_choice = get_year_choice()
    if year_choice == 1:
        add_in_yr(LMS,dept,"1ST_YEAR",book_name,book_id)
    elif year_choice == 2:
        add_in_yr(LMS,dept,"2ND_YEAR",book_name,book_id)
    elif year_choice == 3:
        add_in_yr(LMS,dept,"3RD_YEAR",book_name,book_id)
    elif year_choice == 4:
        add_in_yr(LMS,dept,"4TH_YEAR",book_name,book_id)