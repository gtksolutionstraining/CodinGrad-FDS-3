def take_two_inputs():
    input1 = int(input("Enter input1: "))
    input2 = int(input("Enter input2: "))
    return input1, input2

def add(input1, input2):
    addition  =  input1 + input2
    return addition

def sub(input1, input2):
    return input1 -  input2

def mult(input1, input2):
    return input1 * input2

def div(input1, input2):
    return input1 / input2

def display_menu():
    print("\nUSER MENU\n:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

def calculator():
    status = True
    while status:
        display_menu()
        try:
            choice = int(input("Please Enter your choice: "))
            if choice == 5:
                print("Thank you for using! Exiting")
                status = False
            else:
                if choice == 1:
                    input1, input2 = take_two_inputs()
                    addition = add(input1,input2)
                    print(f"Your Addition is:{addition}")
                elif choice == 2:
                    input1, input2 = take_two_inputs()
                    subtraction = sub(input1, input2)
                    print(f"Your Subtraction is:{subtraction}")
                elif choice == 3:
                    input1, input2 = take_two_inputs()
                    multiplication = mult(input1, input2)
                    print(f"Your Multiplication is:{multiplication}")
                elif choice == 4:
                    input1, input2 = take_two_inputs()
                    division = div(input1, input2)
                    print(f"Your Divisions is:{division}")
                else:
                    print("Please enter any number among 1,2,3,4,5 !")
        except Exception as e:
            print("Please enter number only!")