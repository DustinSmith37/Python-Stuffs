#Dustin Smith
#validation loop
#only allows input of 15, 18, and 20, and totals 3 inputs and outputs

#create running total
runningTotal = 0

#input loop and calculation
for i in range(3):
    number = int(input("input 15, 18, or 20"))
    while number != 15 and number != 18 and number != 20:
        print("invalid input")
        number = int(input("input 15, 18, or 20"))
    runningTotal = runningTotal + number

#output
print(runningTotal)

