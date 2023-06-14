import random

# Choices list
choices = ["rock", "paper", "scissors"]

# ALL THE USER ITEMS
class Player:
    def __init__(self, name):
        self.name = name
        self.choice = None

    # PLAYER CHOICES
    def choose(self):
        self.choice = input("{} enter your choice (rock, paper, or scissors): ".format(self.name)).lower()
        while self.choice not in choices:
            print("Invalid choice. Please try again.")
            self.choice = input("{} enter your choice (rock, paper, or scissors): ".format(self.name)).lower()

    def get_choice(self):
        return self.choice

# THE COMPUTER PLAYER
class ComputerPlayer(Player):
    def choose(self):
        self.choice = random.choice(choices)

# THE GAME ITSELF
class Game:
    # 2 players and the choices
    def __init__(self):
        self.player1 = None
        self.player2 = ComputerPlayer("Computer")
        # What wins against what?
        self.whatBeatswhat = [("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")]

    # If statement for the win
    def whoWins(self, choice1, choice2):
        # CHOICES YOU CAN DO
        if choice1 == choice2:
            return "It's a tie!"
        elif (choice1, choice2) in self.whatBeatswhat:
            return "{} wins!".format(self.player1.name)
        else:
            return "{} wins!".format(self.player2.name)

    # Player name input
    def setup(self):
        player_name = input("Enter your name: ")
        self.player1 = Player(player_name)

    # Gameplay itself
    def play(self):
        self.setup()
        # CHOICES
        self.player1.choose()
        self.player2.choose()
        choice1 = self.player1.get_choice()
        choice2 = self.player2.get_choice()
        # print choices
        print("{} chooses {}.".format(self.player1.name, choice1))
        print("{} chooses {}.".format(self.player2.name, choice2))
        print(self.whoWins(choice1, choice2))

# start it
game = Game()
game.play()