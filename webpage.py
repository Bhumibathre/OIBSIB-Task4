# Login Authentication System

# Dictionary to store registered users
registered_users = {}

# Function to register a new user
def register():  
    print("Please enter your details to register:")    
    username = input("Enter username: ") 
    password = input("Enter password: ")
    registered_users[username] = password
    print("Registration successful!\n")

# Function to login existing user
def login():
    print("Please enter your login details:")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in registered_users and registered_users[username] == password:
        print("Login successful!\n")
        return True
    else:
        print("Login failed. Please check your username and password.\n")
        return False

# Function to access secured page (example function)
def secured_page():
    print("Welcome to the secured page!")
    print("This is confidential information.\n")

# Main program loop
while True:
    print("Welcome to the Login System")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        register()
    elif choice == '2':
        if login():
            secured_page()
    elif choice == '3':
        print("Thank you for using the Login System. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.\n")
