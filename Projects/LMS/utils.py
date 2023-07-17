from config import LMS
def display_menu():
    print("\nLMS MENU\n:")
    print("1. ADMIN")
    print("2. STUDENT")
    print("3. TEACHER")
    print("4. Exit")

def take_input():
    status = True
    while status:
        try:
            choice = int(input("\nPlease enter your choice: "))
            status = False
            return choice
        except Exception as e:
            print("Please enter digits only...")
    
def take_user_password():
    user = input("Please enter your user ID:")
    password = input("Please enter your password")
    return user, password

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

def display_admin_menu():
    print("ADMIN MENU:\n")
    print("1. ADD STUDENT")
    print("2. ADD TEACHER")
    print("3. ADD BOOK")
    print("4. Logout")

def display_year():
    print("YEARS")
    print("1st Year")
    print("2nd Year")
    print("3rd Year")
    print("4th Year")

def display_dept():
    print("DEPTS:")
    print("1. CSE")
    print("2. CIVIL")
    print("3. MECH")
    print("4. EEE")
    print("5. ECE")

def display_sem():
    print("SEMESTERS:")
    print("1ST SEM")
    print("2ND SEM")

def lms_entry():
    status = True
    while status:
        display_menu()
        choice = take_input()
        if choice == 1:
            print("Hello Admin...!")
            user,password = take_user_password()
            flag = check_authentication(user,password)
            while flag:
                display_admin_menu()
                admin_choice = take_input()
                if admin_choice == 1:
                    name = input("Entere Student name")
                    roll_number = input("Entere Roll Number")
                    LMS['STUDENTS'][name] = roll_number
                elif admin_choice == 2:
                    teacher_name = input("Enter Teacher Name")
                    teacher_id = input("Enter teacher ID")
                    LMS['TEACHERS'][teacher_name] = teacher_id
                elif admin_choice == 3:
                    book_name = input("Enter Book Name: ")
                    book_id = input("Enter Book ID: ")
                    display_dept()
                    dept_choice = take_input()
                    if dept_choice == 1:
                        display_year()
                        year_choice = take_input()
                        if year_choice == 1:
                            display_sem()
                            sem_choice = take_input()
                            if sem_choice == 1:
                                LMS["BOOKS"]["CSE"]['1ST_YR']['1ST_SEM'].append({"BOOK_NAME":book_name,"BOOK_ID":book_id})
                                print(f"BOOK {book_name} and Book ID {book_id} is added to CSE 1st Year 1st Sem")
                            elif sem_choice == 2:
                                LMS["BOOKS"]["CSE"]['1ST_YR']['2ND_SEM'].append({"BOOK_NAME":book_name,"BOOK_ID":book_id})
                                print(f"BOOK {book_name} and Book ID {book_id} is addedd to CSE 1st Year 2nd Sem")
                            else:
                                print("Please enter proper 1/2")
                        elif year_choice == 2:
                            display_sem()
                            sem_choice = take_input()
                            if sem_choice == 1:
                                LMS["BOOKS"]["CSE"]['2ND_YR']['1ST_SEM'].append({"BOOK_NAME":book_name,"BOOK_ID":book_id})
                                print(f"BOOK {book_name} and Book ID {book_id} is added to CSE 2nd Year 1st Sem")
                            elif sem_choice == 2:
                                LMS["BOOKS"]["CSE"]['2ND_YR']['2ND_SEM'].append({"BOOK_NAME":book_name,"BOOK_ID":book_id})
                                print(f"BOOK {book_name} and Book ID {book_id} is addedd to CSE 2nd Year 2nd Sem")
                            else:
                                print("Please enter proper 1/2")
                elif admin_choice == 4:
                    print("Logging Out.")
                    flag = False
                else:
                    print("Please enter 1/2/3/4")

        elif choice == 2:
            print("Coming Soon!")
        elif choice == 3:
            print("Coming Soon!")
        elif choice == 4:
            status =  False
            print("Thanks for using LMS.")
        else:
            print("Please enter 1/2/3/4")

