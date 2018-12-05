#Dustin Smith
#Project 3a
#Takes user input and tells them their age bracket

#get user input
age = float(input("Please input your age: "))

#process their age and output
if age < 18:
    print("You are", age, "and are a minor.")
elif age >= 18 and age < 65:
    print("You are", age, "and are an adult.")
else:
    print("You are", age, "and are a senior citizen.")
