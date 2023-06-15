import random
import json

# Choices list
choices = ["rock", "paper", "scissors"]

# User data stored in a JSON file
user_file = "UserInf.json"

# User login and registration
def register():
    # User and password input
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    # Open the file and load the data
    with open(user_file, "r+") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            # Empty list if file is empty
            data = []

        # Check if username already exists
        if any(user['username'] == username for user in data):
            print("Username already exists. Please choose a different username.")
            return

        # Append new user data to the list
        data.append({"username": username, "password": password, "points": 0})

        # Write the updated data to the file
        file.seek(0)
        json.dump(data, file)

    print("Registration successful.")

def login():
    # User inputs
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Open the file and load the data (read)
    with open(user_file, "r") as file:
        data = json.load(file)

        # Check if username and password match
        for user in data:
            if user["username"] == username and user["password"] == password:
                print("Login successful.")
                return user

    print("Invalid username or password.")
    return None

# Function to update user data in the JSON file
def update_user_data(username, points):
    #"r+" means read and write
    with open(user_file, "r+") as file:
        data = json.load(file)
        for user in data:
            #if statement
            if user['username'] == username:
                user['points'] = points
                file.seek(0)
                json.dump(data, file)
                break

# Game Class
class Game:
    def __init__(self, user):
        self.user = user

    #choice inputs
    def choose(self):
        choice = input("{} enter your choice (rock, paper, or scissors): ".format(self.user['username'])).lower()
        while choice not in choices:
            print("Invalid choice. Please try again.")
            choice = input("{} enter your choice (rock, paper, or scissors): ".format(self.user['username'])).lower()
        return choice

    #welcome user
    def play(self):
        print("Welcome {}!".format(self.user['username']))

        #user choice
        choice1 = self.choose()
        #computer choice
        choice2 = random.choice(choices)

        #print both choices
        print("{} chooses {}.".format(self.user['username'], choice1))
        print("{} chooses {}.".format("Computer", choice2))

        #win check
        result = self.check_winner(choice1, choice2)
        print(result)

        if self.user['username'] in result:
            #add points
            self.user['points'] += 1

        # Update the user data in the JSON file
        update_user_data(self.user['username'], self.user['points'])

    #check what wins against what
    def check_winner(self, choice1, choice2):
        if choice1 == choice2:
            return "It's a tie!"
        elif (choice1 == "rock" and choice2 == "scissors") or (choice1 == "paper" and choice2 == "rock") or (choice1 == "scissors" and choice2 == "paper"):
            return "{} wins!".format(self.user['username'])
        else:
            return "Computer wins!"

# Main program
def main():
    print("Welcome to Rock, Paper, Scissors!")
    logged_in = False
    user = None

    #menu
    while True:
        if not logged_in:
            print("\nMenu:")
            print("1. Register")
            print("2. Login")
            print("3. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                register()
            elif choice == "2":
                user = login()
                if user:
                    logged_in = True
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            print("\nMenu:")
            print("1. Play")
            print("2. User Points")
            print("3. Logout")

            choice = input("Enter your choice: ")

            if choice == "1":
                game = Game(user)
                game.play()
            elif choice == "2":
                print("Your Points: {}".format(user['points']))
            elif choice == "3":
                logged_in = False
                print("Logged out.")
            else:
                print("Invalid choice. Please try again.")

# Start the program
if __name__ == "__main__":
    main()