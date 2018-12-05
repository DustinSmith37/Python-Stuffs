#randomized name list by Dustin and Richie

#Imports random library
import random
counter = 0
#list of students
students = ['Trevor','Jonathan','Nathan','Ollie','Parker','Jaden','Zackey','Victoria','Jacob','Richie','Dustin','Chase']

#randomly lists the names and prints them, 12 at a time
names = random.sample(students, 12)
for counter in range(12):
    print(counter + 1, names[counter])

    
