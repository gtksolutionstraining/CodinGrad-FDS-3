from utils.dept_utils import get_dept_choice
from utils.dept_utils import add_in_dept

def add_book():
    book_name = input("Enter Book Name: ")
    book_id = input("Enter Book ID: ")
    dept_choice = get_dept_choice()
    if dept_choice == 1:
        add_in_dept("CSE",book_name,book_id)
    elif dept_choice == 2:
        add_in_dept("CIVIL",book_name,book_id)
    elif dept_choice == 3:
        add_in_dept("MECH",book_name,book_id)
    elif dept_choice == 4:
        add_in_dept("EEE",book_name,book_id)
    elif dept_choice == 5:
        add_in_dept("ECE",book_name,book_id)