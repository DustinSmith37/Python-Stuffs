#Dustin Smith
#Project 3d
#This checks if the current year is a leap year

#Get inputs
year = int(input("What is the current year? "))

#Check to see if its a leap year and print
if year % 4 == 0:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
