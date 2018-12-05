#Dustin Smith
#Project 3b
#This calculates prices for software and gives total and discount

#declare variables
costForDiscount = 350
percentDiscount = 0.9
costPerUnit = 48
#Get user input
units = int(input("How many units would you like to purchase? "))

#process cost of units
totalPrice = units * costPerUnit

#check for 10% discount and output
if totalPrice > costForDiscount:
    totalPrice *= percentDiscount
    print("Your total is $", format(totalPrice, '.2f'), "due to your 10% discount for buying over $350 in software!")
else:
    print("Your total is $", format(totalPrice, '.2f'))

print("Thank you for ordering from our company!")
