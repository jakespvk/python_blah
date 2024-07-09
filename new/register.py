import login

def register():
    username = input("Username: ").lower()
    if username in login.logins:
        print("Username already exists...")
        login.login(username)
        return
    password = input("Password: ")
    login.logins[username] = password
