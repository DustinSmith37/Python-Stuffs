#Dustin Smith
#Midterm Project B
#This checks if an inputed value is between 100 and 500

#Create values
minimum = 100
maximum = 500

#Get user input
userNumber = float(input("What number would you like to check? "))

#Checks if number is in range and outputs
if userNumber <= maximum and userNumber >= minimum:
    print("This number is within the valid range.")
elif userNumber > maximum:
    print("This number is above the valid range.")
else:
    print("This number is below the valid range.")
