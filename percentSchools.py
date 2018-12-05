#Dustin Smith
#Percents of schools in class
#This program tells you the percent students from each school of a class

#Get users inputs of class's members of each school
airline = float(input("How many Airline students are in the class?"))
benton = float(input("How many Benton students are in the class?"))
haughton = float(input("How many Haughton students are in the class?"))
parkway = float(input("How many Parkway students are in the class?"))

#Calculate percents of each highschool
totalClass = airline + benton + haughton + parkway
percentAirline = (airline/totalClass)*100
percentBenton = (benton/totalClass)*100
percentHaughton = (haughton/totalClass)*100
percentParkway = (parkway/totalClass)*100

#Print results
print("The class is:\n", format(percentAirline, '.1f'), "% Airline students\n", format(percentBenton, '.1f'), "% Benton students\n", format(percentHaughton, '.1f'), "% Haughton students\n", format(percentParkway, '.1f'), "% Parkway students")
