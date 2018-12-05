#Dustin Smith
#Project 4a
#Takes customers names and addresses in loops

#Establish library of names and addresses
listOfNames = []
listOfAddresses = []

#input loop
repeat = 'yes'
while repeat == 'yes':
    listOfNames.append(input("Input customers name: "))
    listOfAddresses.append(input("Input customers address: "))
    repeat = input("Would you like to repeat? Type 'yes' to continue: ")

#output loop for each customer set
for names in listOfNames:
    customer = listOfNames.index(names)
    print("Customer name: ", listOfNames[customer], "\
    Customer address: ", listOfAddresses[customer], "\n")