#Dustin Smith
#Roulette Wheel Colors
#Takes a pocket number and gives its color

#Set arrays for each color
green = [0]
red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
black = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]

#take user input and checks if it is valid
pocket = int(float(input("Whats the pocket number? Valid range is 0-36. ")))

while pocket not in green and pocket not in red and pocket not in black:
    print("That is not a valid pocket number.")
    pocket = int(float(input("Please input a valid pocket number: ")))
    
#check input and print the color output
if pocket in green:
    print("The pocket is green!")
elif pocket in red:
    print("The pocket is red!")
elif pocket in black:
    print("The pocket is black!")
