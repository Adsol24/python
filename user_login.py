def register_user(username, password, user_list):
    user_list.append({"username": username, "password": password})

def login_user(username, password, user_list):
    for user in user_list:
        if user["username"] == username and user["password"] == password:
            return True
    return False

def main():
    users = []

    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            username = input("Enter username: ")
            password = input("Enter password: ")
            register_user(username, password, users)
            print("User registered successfully!\n")
        elif choice == 2:
            username = input("Enter username: ")
            password = input("Enter password: ")
            if login_user(username, password, users):
                print("Login successful!\n")
            else:
                print("Invalid username or password.\n")
        elif choice == 3:
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
