#Dustin Smith
#Final Project 1
#This is a program that prompts the user to guess a 
#number between 1 and 1000 and tells them if they are too low, too high, or correct

#import random
import random

#create main function
def main():
    #create various variables
    timesGuess = 0
    rightAnswer = random.randint(1,1000)
    userGuess = int(input("Please guess an integer between 1 and 1000: "))
    #guessing loop
    while userGuess != rightAnswer:
        if userGuess < rightAnswer:
            print(userGuess,"is too low.")
        else:
            print(userGuess,"is too high.")
        userGuess = int(input("Please guess an integer between 1 and 1000: "))
        timesGuess += 1
    #says correct answer, number of guesses, and asks if user wants to play again
    print(userGuess,"is correct! You got it right after", timesGuess,"guesses.")
    playAgain = input("Play again? Y or N: ")
    if playAgain == 'Y' or playAgain == 'y':
        main()
    else:
        print('Goodbye')
        #call main
main()