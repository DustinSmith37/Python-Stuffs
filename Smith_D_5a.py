#Dustin Smith
#Project 5a
#This uses a function to convert kilometers to miles

#take input
numberKilometers = float(input("Input kilometeres to be converted: "))

#create function to convert kilometers to miles
def kilometers_to_miles(numberKilometers):
    KmToMilesConversion = 0.6214
    miles = numberKilometers * KmToMilesConversion
    print(format(miles, '.2f'),"is the number of miles.")

#call function
kilometers_to_miles(numberKilometers)