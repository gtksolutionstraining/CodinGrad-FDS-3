from config import DEPT
from utils.display_utils import(
    display_student_menu,
)
from utils.input_utils import(
    take_input
)
from utils.dept_utils import(
    get_dept
)
from utils.year_sem_utils import(
    get_year,
    get_sem
)
from utils.book_utils import(
    list_books,get_books,return_book
)
def add_student(LMS):
    name = input("Enter Student name")
    roll_number = input("Enter Roll Number")
    LMS['STUDENTS'][name] = roll_number

def is_student_exists(LMS,name, roll_number):
    for student_name in LMS['STUDENTS'].keys():
        if student_name == name:
            if LMS['STUDENTS'][student_name] == roll_number:
                print("Student Authentication successfull...!")
                return True
    print("Student not found!")
    return False


def get_student_info():
    dept = get_dept()
    year = get_year()
    sem = get_sem()
    return dept,year,sem

def student_entry(LMS):
    flag = True
    while flag:
        display_student_menu()
        student_choice = take_input()
        if student_choice == 1:
            dept,year,sem = get_student_info()
            list_books(LMS,dept,year,sem)
        elif student_choice == 2:
            dept,year,sem = get_student_info()
            get_books(LMS,dept,year,sem)
        elif student_choice == 3:
            return_book(LMS)
        elif student_choice == 4:
            print("Logging Out!")
            flag = False
        else:
            print("Please select 1/2/3/4")