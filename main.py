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
            #DATA
            data = {}

        # Check if username already exists
        if username in data:
            print("Username already exists. Please choose a different username.")
            return

        #write the password and username
        data[username] = {"password": password}
        file.seek(0)
        json.dump(data, file)

    print("Registration successful.")

def login():
    #INPUTS
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    #OPEN TE FILE
    with open(user_file, "r") as file:
        data = json.load(file)
        
        #PASSWORD RIGHT
        if username in data and data[username]["password"] == password:
            print("Login successful.")
            return {username: data[username]}

    #IF NOT
    print("Invalid username or password.")
    return None

# Game logic
#CLASSES
class Game:
    def __init__(self, user):
        self.user = user

    #CHOICE
    def choose(self):
        #what you choose
        choice = input("{} enter your choice (rock, paper, or scissors): ".format(self.user)).lower()

        #if not one of the options
        while choice not in choices:
            print("Invalid choice. Please try again.")

            #Ask again
            choice = input("{} enter your choice (rock, paper, or scissors): ".format(self.user)).lower()
        return choice

    def play(self):
        #welcome the user
        print("Welcome {}!".format(self.user))

        #choices
        choice1 = self.choose()
        choice2 = random.choice(choices)

        #who chose what
        print("{} chooses {}.".format(self.user, choice1))
        print("{} chooses {}.".format("Computer", choice2))
        
        #who beat who?
        result = self.check_winner(choice1, choice2)
        print(result)

    #WHAT BEATS WHAT???
    def check_winner(self, choice1, choice2):

        #TIE
        if choice1 == choice2:
            return "It's a tie!"
        #WIN FOR USER
        elif (choice1 == "rock" and choice2 == "scissors") or (choice1 == "paper" and choice2 == "rock") or (choice1 == "scissors" and choice2 == "paper"):
            return "{} wins!".format(self.user)
        #WIN FOR COMPUTER
        else:
            return "Computer wins!"

# Main program flow
def main():

    #WELCOME
    print("Welcome to Rock, Paper, Scissors!")
    logged_in = False
    user = None

    #loop
    while True:
        if not logged_in:

            #menu
            print("\nMenu:")
            print("1. Register")
            print("2. Login")
            print("3. Quit")

            #input
            choice = input("Enter your choice: ")

            #choices for the options
            if choice == "1":
                register()
            elif choice == "2":
                user = login()
                if user:
                    logged_in = True
            elif choice == "3":
                print("Goodbye!")
                break

            #if not
            else:
                print("Invalid choice. Please try again.")
        #retype it
        else:
            print("\nMenu:")
            print("1. Play")
            print("2. Logout")
            
            #input
            choice = input("Enter your choice: ")

            #play the game
            if choice == "1":
                game = Game(list(user.keys())[0])
                game.play()
            
            #log out
            elif choice == "2":
                logged_in = False
                print("Logged out.")
            
            #if option not picked
            else:
                print("Invalid choice. Please try again.")

# Start the program
if __name__ == "__main__":
    main()