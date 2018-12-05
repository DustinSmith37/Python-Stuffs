#Dustin Smith
#Object fall over time function
#Takes user input of seconds passed and displays the distance fallen

#Get user input and create rate of fall value
seconds = float(input("How many seconds has the object fallen? "))
rateOfFall = 4.9

#create function to calculate the distance fallen
def distanceFallen(seconds, rateOfFall):
    metersFallen = rateOfFall * seconds ** 2
    return metersFallen

metersFallen = distanceFallen(seconds, rateOfFall)
print(format(metersFallen,'.2f'),"is the distance in meters the object has fallen")