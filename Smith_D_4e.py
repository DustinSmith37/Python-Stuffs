#Dustin Smith
#Project 4e
#This calculates ocean rising for the next 10 years

#set variables for loop
years = 10
risingOcean = 1.6
totalRise = risingOcean

#establish loop and output
for i in range(years):
    if i == 9:
        chartSpace = "\t"
    else:
        chartSpace = "\t\t"
    print("Year", i+1, chartSpace, format(totalRise, '.1f'), "mm ocean rise")
    totalRise = totalRise + risingOcean