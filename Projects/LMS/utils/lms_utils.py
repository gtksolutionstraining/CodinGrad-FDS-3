from utils.display_utils import (
    display_menu,
    display_student_menu
)
from utils.input_utils import (
    take_input, 
    take_user_password,
    take_name_roll_numer
)
from utils.admin_utils import (
    check_authentication,
    admin_entry
)
from utils.student_utils import (
    is_student_exists,
    student_entry
)
from libs import json

def lms_entry():
    print("\nEntering into LMS...!\n")
    file = open("assets/LMS.json","r")
    LMS = json.load(file)
    file.close()
    status = True
    while status:
        print("================")
        print("DISPLAYING LMS MENU")
        print("=================")
        display_menu()
        choice = take_input()
        if choice == 1:
            print("Hello Admin...!")
            user,password = take_user_password()
            flag = check_authentication(LMS,user,password)
            if flag:
                admin_entry(LMS,flag)
            else:
                print("Login Failure.. Please try again.")    
        elif choice == 2:
            print("Hello Student...!")
            student_name, roll_number = take_name_roll_numer()
            student_flag = is_student_exists(LMS,student_name,roll_number)
            if student_flag:
                student_entry(LMS)
            else:
                print("Student Login Failure... Please try again.")
        elif choice == 3:
            print("Teacher MENU will be Coming Soon!")
        elif choice == 4:
            file = open("assets/LMS.json","w")
            file.write(str(LMS).replace('\'','\"'))
            file.close()
            status =  False
            print("Thanks for using LMS.")
        else:
            print("Please enter 1/2/3/4")

