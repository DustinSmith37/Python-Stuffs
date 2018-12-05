#Dustin Smith
#Midterm Project A
#This program calculates tips for the meal based off price.

#Take inputs
dinnerBill = float(input("What was the cost of your meal? "))

while dinnerBill < 0:
    print("Thats not a valid cost for a meal.")
    dinnerBill = float(input("What was the cost of your meal? "))
    
tipPercentInt = float(input("Would you like to tip 15, 18, or 20 percent? "))

while tipPercentInt != 15 and tipPercentInt != 18 and tipPercentInt != 20:
    print("That is not a valid amount of tip")
    tipPercentInt = float(input("Would you like to tip 15, 18, or 20 percent? "))

#Calculates tip and total
    
tipPercentFloat = tipPercentInt/100
tipAmount = tipPercentFloat * dinnerBill
dinnerTotal = tipAmount + dinnerBill

#display results
if tipPercentInt == 15:
    print("15% tip is $", format(tipAmount,'.2f'), "and the total is $", format(dinnerTotal,'.2f'))
elif tipPercentInt == 18:
    print("18% tip is $", format(tipAmount,'.2f'), "and the total is $", format(dinnerTotal,'.2f'))
elif tipPercentInt == 20:
    print("20% tip is $", format(tipAmount,'.2f'),  "and the total is $", format(dinnerTotal,'.2f'))

