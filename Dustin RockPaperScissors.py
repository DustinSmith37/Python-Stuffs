#Dustin Smith
#Rock paper scissors game

#Import random module for generations
import random

#introduce user
print("Welcome to the rock paper scissors bot! Have fun!")

#input checker
def inputChecker(inputTopic):
    while True:
        try:
            userInput = input(inputTopic).lower()
            if userInput != 'rock' and userInput != 'paper' and userInput != 'scissors':
                int('a')
            return userInput
        except ValueError:
            print("Invalid input")

#generate computers choice
def computerChoice():
    global computerMove
    computerMove = random.randrange(1,3)

#check repeat input
def inputCheckerRepeat(inputTopic):
    while True:
        try:
            userInput = input(inputTopic).upper()
            if userInput != 'Y' and userInput != 'N':
                int('a')
            return userInput
        except ValueError:
            print("Invalid input")

#checks winner
def victoryChecker(userChoice, computerMove):
    if userChoice == "rock" and computerMove == 3:
        print("\nWe both picked rock and tie!")
    elif userChoice == "rock" and computerMove == 2:
        print("\nI picked paper and you picked rock, paper beats rock, I win!")
    elif userChoice == "rock" and computerMove == 1:
        print("\nI picked scissors and you picked rock, rock beats scissors, you win!")
    elif userChoice == "paper" and computerMove == 3:
        print("\nI picked rock and you picked paper, paper beats rock, you win!")
    elif userChoice == "paper" and computerMove == 2:
        print("\nWe both picked paper and tie!")
    elif userChoice == "paper" and computerMove == 1:
        print("\nI picked scissors and you picked paper, scissors beats paper, I win!")
    elif userChoice == "scissors" and computerMove == 3:
        print("\nI picked rock and you picked scissors, rock beats scissors, I win!")
    elif userChoice == "scissors" and computerMove == 2:
        print("\nI picked paper and you picked scissors, scissors beats paper, you win!")
    elif userChoice == "scissors" and computerMove == 1:
        print("\nWe both picked scissors and tie!")

#game loop
repeat = 'Y'
while repeat == 'Y':
    userChoice = inputChecker("\nRock, paper, or scissors? ")
    computerChoice()
    victoryChecker(userChoice, computerMove)
    repeat = inputCheckerRepeat("Would you like to play again? Y or N? ")