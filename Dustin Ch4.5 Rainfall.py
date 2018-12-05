#Dustin Smith
#Average Rainfall
#Gets rainfall totals/averages

#create variables
validYears = False

#get user input for years
userYears = input("How many years are covered? ")
totalRainfall = 0
while validYears != True:
        try:
            userYears = int(userYears)
            if userYears <= 0:
                int("a")
            validYears = True
        except ValueError:
            userYears = input("Invalid input. How many years are covered? ")

#Create looping asker
for years in range(userYears):
    print("\nRainfall for year", years +1)
    
    for months in range(12):
        validMonthsRainfall = False
        
        #take input for rainfall and validate
        print("Please input inches of rainfall for month #", months+1)
        userMonthsRainfall = input("Rainfall:")
        while validMonthsRainfall != True:
            try:
                userMonthsRainfall = float(userMonthsRainfall)
                if userMonthsRainfall < 0:
                    int("a")
                validMonthsRainfall = True
            except ValueError:
                userMonthsRainfall = input("Invalid input. Input rainfall in inches: ")
        totalRainfall += userMonthsRainfall

#Print results
print(totalRainfall, "inches total \nAverage rainfall:", format(totalRainfall/(userYears*12), '.2f'), "inches per month")
