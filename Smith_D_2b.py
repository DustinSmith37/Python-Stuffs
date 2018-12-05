#Dustin Smith
#Project 2b
#This program calculates sales tax an item

#Ask user for cost of item(s)
initialCost = float(input("What is the cost of the item(s)? "))

#Calculates the additional tax costs of state and county, and calculates total
stateTax = initialCost * 0.05
countyTax = initialCost * 0.025
totalCost = initialCost + stateTax + countyTax

#Prints the results
print("Item(s) cost: $", format(initialCost, '.2f'), "\nState tax: $", format(stateTax, '.2f'), "\nCounty tax: $", format(countyTax, '.2f'), "\nTotal cost: $", format(totalCost, '.2f'), "\nThank you, come again!")
