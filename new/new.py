USERNAME = ""
PASSWORD = ""

def check_username(username):
    if username.lower() == "jspievak":
        return True
    else:
        return False

def check_password(password):
    if password == "    ":
        return True
    else:
        return False

def __main__():
    print("Please login below.")
    USERNAME = input("Username: ")
    while not check_username(USERNAME):
        print("Invalid username! Please try again.")
        USERNAME = input("Username: ")
    PASSWORD = input("Password: ")
    while not check_password(PASSWORD):
        print("Invalid password! Please try again.")
        PASSWORD = input("Password: ")
    print("Welcome, " + USERNAME + "!")

__main__()
