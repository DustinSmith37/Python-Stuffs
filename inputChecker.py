#Input checkers functions, made by Dustin Smith
#Free for use by anyone, just do NOT change this program
#May be updated as I learn more
#Copy and paste from def to the end of the indentions

#This function outputs integers
def Int(inputTopic):
    while True:
        try:
            userInput = int(input(inputTopic))
            return userInput
        except ValueError:
            print("Invalid input")

#This one takes a float input
def Float(inputTopic):
    while True:
        try:
            userInput = float(input(inputTopic))
            return userInput
        except ValueError:
            print("Invalid input")

#This one takes postive integer inputs
def IntPos(inputTopic):
    while True:
        try:
            userInput = int(input(inputTopic))
            if userInput < 0:
                int("a")
            return userInput
        except ValueError:
            print("Invalid input")

#This one takes postive float inputs
def FloatPos(inputTopic):
    while True:
        try:
            userInput = float(input(inputTopic))
            if userInput < 0:
                int("a")
            return userInput
        except ValueError:
            print("Invalid input")

#This one makes sure its letters/punctuation/spaces only
def StrOnly(inputTopic):
    while True:
        try:
            userInput = input(inputTopic)
            if any(userInput).isalpha() == False:
                int('a')
            return userInput
        except ValueError:
            print("Invalid input")