USERNAME = ""
PASSWORD = ""

logins = {"jspievak": "    ", "kimmy": "1111"}
def check_username(username):
    return username.lower() in logins.keys()

def check_password(password):
    return password == str(logins[USERNAME])

def login():
    print("Please login below.")
    USERNAME = input("Username: ").lower()
    while not USERNAME in logins:
        print("Invalid username! Please try again.")
        USERNAME = input("Username: ")
    PASSWORD = input("Password: ")
    while not PASSWORD == logins[USERNAME]:
        print("Invalid password! Please try again.")
        PASSWORD = input("Password: ")
    print("Welcome, " + USERNAME + "!")
