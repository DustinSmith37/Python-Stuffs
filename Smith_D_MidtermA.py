#Dustin Smith
#Midterm Project A
#This program calculates tips for the meal based off price.

#Create tip values
PercentTip15 = 0.15
PercentTip18 = 0.18
PercentTip20 = 0.20

#take user input
dinnerBill = float(input("What was the cost of your meal? "))

#calculate tips
tip15 = dinnerBill * PercentTip15
tip18 = dinnerBill * PercentTip18
tip20 = dinnerBill * PercentTip20

tipTotal15 = dinnerBill + tip15
tipTotal18 = dinnerBill + tip18
tipTotal20 = dinnerBill + tip20
#display results
print("15% tip is $", format(tip15,'.2f'), "and the total is $", format(tipTotal15,'.2f'),\
      "\n18% tip is $", format(tip18,'.2f'), "and the total is $", format(tipTotal18,'.2f'),\
      "\n20% tip is $", format(tip20,'.2f'),  "and the total is $", format(tipTotal20,'.2f'))

