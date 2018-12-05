#Dustin Smith
#Problem 11
#Random math problems

#import random
import random

#question counter
question = 1

#input check
def inputCheckerInt(inputTopic):
    while True:
        try:
            userInput = int(input(inputTopic))
            return userInput
        except ValueError:
            print("Invalid input")

#repeat input check
def inputCheckerRepeat(inputTopic):
    while True:
        try:
            userInput = input(inputTopic).upper()
            if userInput != 'Y' and userInput != 'N':
                int('a')
            return userInput
        except ValueError:
            print("Invalid input")

#math function
def mathMaker():
    number1 = random.randint(1,1000)
    number2 = random.randint(1,1000)
    correctAnswer = number1 + number2
    while True:
        userAnswer = inputCheckerInt("What is "+str(number1) + " + "\
         + str(number2) + ":")
        if userAnswer == correctAnswer:
            print("Well done!")
            break
        else:
            print("Incorrect answer. Please try again.")  
    global question
    question = question + 1

#question loop
repeat = 'Y'
while True:
    if repeat == 'Y':
        print("Question "+ str(question) + ": ")
        mathMaker()
        repeat = inputCheckerRepeat("Would you like to continue? y or n: ")
    else:
        break

