import login
import register
import chat

def home():
    print("Home page")
    print("Login to view menu options...")
    option = input("1. Login\n2. Register\n3. Exit\n")
    switch = {
        "1": login.login,
        "2": register.register,
        "3": exit
    }
    switch[option]()

    print("Menu options:\n1. Enter chat room\n2. Exit")
    option = input("Enter option: ")
    switch = {
        "1": chat.open_chat,
        "2": exit
    }
    switch[option]()
