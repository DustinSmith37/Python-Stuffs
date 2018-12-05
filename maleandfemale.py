#Dustin Smith
#Male and Female ratio
#This program tells you the percent male and female of a class

#Get users inputs of class's males and females
males = float(input("How many males?"))
females = float(input("How many females?"))

#Calculate percents of males and females
totalClass = males + females
percentMales = (males/totalClass)*100
percentFemales = (females/totalClass)*100

#Print results
print("The class is ",format(percentMales, '.1f'),"% male, and ",format(percentFemales, '.1f'),"% female.")
