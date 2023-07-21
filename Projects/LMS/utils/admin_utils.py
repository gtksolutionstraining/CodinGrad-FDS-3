from utils.display_utils import display_admin_menu
from utils.input_utils import take_input
from utils.student_utils import add_student
from utils.teachers_utils import add_teacher
from utils.book_utils import add_book

def check_authentication(LMS,user,password):
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

def admin_entry(LMS,flag):
    while flag:
        display_admin_menu()
        admin_choice = take_input()
        if admin_choice == 1:
            add_student(LMS)
        elif admin_choice == 2:
            add_teacher(LMS)
        elif admin_choice == 3:
            add_book(LMS)
        elif admin_choice == 4:
            flag = False
            print("Logging Out..!")
        else:
            print("Please enter 1/2/3/4")