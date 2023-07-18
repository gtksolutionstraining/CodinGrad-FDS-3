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