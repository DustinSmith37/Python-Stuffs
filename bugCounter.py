#Dustin Smith
#Bug Collector
#Displays bugs caught over 5 days
bugsTotal = 0
bugsTemp = 0
for days in range(5):
    bugsTemp = input("Please input bugs caught today: ")
    validInput = False
    while validInput != True:
        try:
            bugsTemp = int(bugsTemp)
            if bugsTemp < 0:
                int("a")
            validInput = True
        except ValueError:
            bugsTemp = input("Invalid entry, please input bugs caught today: ")
    bugsTotal = bugsTotal + bugsTemp
print("The bug total is:", bugsTotal)    
