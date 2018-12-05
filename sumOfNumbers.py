#Dustin Smith
#Sum of Numbers
#Adds all postive numbers together until a negative is input
totalNum = 0
number = 0
while number >= 0:
    number = input("Enter postive numbers to add them or a "\
                   "negative to stop the program: ")
    validInput = False
    while validInput != True:
        try:
            number = float(number)
            validInput = True
        except ValueError:
            number = input("try failed, postive or negative number please: ")
    if number < 0:
        break
    totalNum = totalNum + number

print("The total is",totalNum)
