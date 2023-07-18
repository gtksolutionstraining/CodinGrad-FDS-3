from utils.display_utils import display_admin_menu
from utils.input_utils import take_input
from utils.student_utils import add_student
from utils.teachers_utils import add_teacher
from utils.book_utils import add_book
from config import LMS

def check_authentication(user,password):
    admins = LMS['LIB_ADMINS']
    for admin in admins:
        if admin['USER_NAME'] == user:
            if admin['PASSWORD'] == password:
                print("Authentucation Successfull...!")
                return True
            else:
                print("Incorrect Password!")
                for i in range(2):
                    print(f"{2-i} chance(s) left!")
                    password = input("Please enter password: ")
                    if admin['PASSWORD'] == password:
                        print('Authentication Successfull...!')
                        return True
                print("You have entered 3 wrong passwords")
                return False
    print("Username and Password are invalid!")
    return False

def admin_entry(flag):
    while flag:
        display_admin_menu()
        admin_choice = take_input()
        if admin_choice == 1:
            add_student()
        elif admin_choice == 2:
            add_teacher()
        elif admin_choice == 3:
            add_book()
        elif admin_choice == 4:
            flag = False
            print("Logging Out..!")