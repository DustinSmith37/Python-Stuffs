#Dustin Smith
#Project 2c
#This program tells you the percent of each color of binder from the total

#Get users inputs of colors of binders of each school
white = float(input("How many white binders are there? "))
black = float(input("How many black binders are there? "))
blue = float(input("How many blue binders are there? "))

#Calculate percents of each color
totalBinder = white + black + blue
percentWhite = (white/totalBinder)*100
percentBlue = (blue/totalBinder)*100
percentBlack = (black/totalBinder)*100

#Print results
print("The binders are:\n", format(percentWhite, '.1f'), "% White\n", format(percentBlue, '.1f'), "% Blue\n", format(percentBlack, '.1f'), "% Black")
