import login

def home():
    print("Home page")
    print("Login to view menu options...")
    option = input("1. Login\n2. Register\n3. Exit\n")
    switch = {
        "1": login.login(),
        #"2": register.register,
        "3": exit
    }
    switch[option]
