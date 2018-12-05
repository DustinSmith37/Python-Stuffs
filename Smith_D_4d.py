#Dustin Smith
#Project 4d
#This averages lap times

#take input for number of laps
laps = int(input("How many laps did the car drive? "))

#set total time
totalTime = 0
#establish loop based on number of laps
for i in range(laps):
    currentLap = float(input("How many seconds long was lap "+str(i+1)+": "))
    totalTime = totalTime + currentLap

#calculate average
average = totalTime / laps

#output
print(format(average, '.2f'), "is the average length in seconds of the laps")
