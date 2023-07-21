from utils.dept_utils import get_dept_choice
from utils.dept_utils import add_in_dept
from utils.input_utils import take_input
def add_book(LMS):
    book_name = input("Enter Book Name: ")
    book_id = input("Enter Book ID: ")
    dept_choice = get_dept_choice()
    if dept_choice == 1:
        add_in_dept(LMS,"CSE",book_name,book_id)
    elif dept_choice == 2:
        add_in_dept(LMS,"CIVIL",book_name,book_id)
    elif dept_choice == 3:
        add_in_dept(LMS,"MECH",book_name,book_id)
    elif dept_choice == 4:
        add_in_dept(LMS,"EEE",book_name,book_id)
    elif dept_choice == 5:
        add_in_dept(LMS,"ECE",book_name,book_id)

def list_books(LMS,dept,year,sem):
    books = LMS['BOOKS'][dept][year][sem]
    if len(books) == 0:
        print("No Books added please visit after sometime.")
        return False
    print("LISTING BOOKS")
    i = 1
    for book in books:
        print(f"{i}.BOOK_NAME: {book['BOOK_NAME']}, BOOK_ID: {book['BOOK_ID']}")
        i = i+1 #Incremental Operation
    return True

def get_books(LMS,dept,year,sem):
    books = LMS['BOOKS'][dept][year][sem]
    flag = True
    while flag:
        books_status =list_books(LMS,dept,year,sem)
        if not books_status:
            return
        book_choice = take_input()
        if book_choice in list(range(1,len(books)+1)):
            print("Take your book")
            del LMS['BOOKS'][dept][year][sem][book_choice-1]
            return True
        else:
            print("Please select one of the book listed above")

def return_book(LMS):
    add_book(LMS)
