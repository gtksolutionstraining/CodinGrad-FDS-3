from utils.display_utils import display_menu
from utils.input_utils import (
    take_input, 
    take_user_password
)
from utils.admin_utils import (
    check_authentication,
    admin_entry
)

def lms_entry():
    status = True
    while status:
        display_menu()
        choice = take_input()
        if choice == 1:
            print("Hello Admin...!")
            user,password = take_user_password()
            flag = check_authentication(user,password)
            if flag:
                admin_entry(flag)
            else:
                print("Login Failure.. Please try again.")    
        elif choice == 2:
            print("Student MENU will be Coming Soon!")
        elif choice == 3:
            print("Teacher MENU will be Coming Soon!")
        elif choice == 4:
            status =  False
            print("Thanks for using LMS.")
        else:
            print("Please enter 1/2/3/4")

