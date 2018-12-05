a1,a2,a3 = ' ',' ',' '
b1,b2,b3 = ' ',' ',' '
c1,c2,c3 = ' ',' ',' '
def inputChecker(inputTopic):
    while True:
        try:
            userInput = input(inputTopic).lower()
            if userInput == 'a1' or userInput == 'a2' or userInput == 'a3'\
            or userInput == 'b1' or userInput == 'b2' or userInput == 'b3'\
            or userInput == 'c1' or userInput == 'c2' or userInput == 'c3':
                return userInput
            else:
                int('a')
        except ValueError:
            print("Invalid input")
playerMove = inputChecker("What is your first move? ")
def playerBoard(playerMove):
    if playerMove == 'a1':
        global a1
        a1 = 'X'
    elif playerMove == 'a2':
        global a2
        a2 = 'X'
    elif playerMove == 'a3':
        global a3
        a3 = 'X'
    elif playerMove == 'b1':
        global b1
        b1 = 'X'
    elif playerMove == 'b2':
        global b2
        b2 = 'X'
    elif playerMove == 'b3':
        global b3
        b3 = 'X'
    elif playerMove == 'c1':
        global c1
        c1 = 'X'
    elif playerMove == 'c2':
        global c2
        c2 = 'X'
    elif playerMove == 'c3':
        global c3
        c3 = 'X'
playerBoard(playerMove)
print(playerMove)
print("  A   B   C\n1",a1,"|",b1,"|",c1,"\n ---|---|---\n2",a2,"|",b2,"|",c2,"\n ---|---|---\n3",a3,"|",b3,"|",c3)
