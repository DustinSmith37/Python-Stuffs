#Dustin Smith
#Project 2a
#This program asks the square feet of a tract of land and converts it into acres.

#This gets the input for the sqaure feet
squareFeet = float(input("How many square feet is the tract?"))

#This converts square feet to acres
acres= squareFeet / 43560

#This displays the solved value (formatted to 3 decimals for ease of use
print("Your tract is", format(acres, '.3f'), "acres!")
