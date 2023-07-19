from utils.dept_utils import get_dept_choice
from utils.dept_utils import add_in_dept
from config import LMS
from utils.input_utils import take_input
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

def list_books(dept,year,sem):
    books = LMS['BOOKS'][dept][year][sem]
    if len(books) == 0:
        print("No Books added please visit after sometime.")
        return
    print("LISTING BOOKS")
    i = 1
    for book in books:
        print(f"{i}.BOOK_NAME: {book['BOOK_NAME']}, BOOK_ID: {book['BOOK_ID']}")
        i = i+1

def get_books(dept,year,sem):
    books = LMS['BOOKS'][dept][year][sem]
    flag = True
    while flag:
        list_books(dept,year,sem)
        book_choice = take_input()
        if book_choice in list(range(1,len(books)+1)):
            print("Take your book")
            del LMS['BOOKS'][dept][year][sem][book_choice-1]
            return True
        else:
            print("Please select one of the book listed above")

def return_book():
    add_book()
