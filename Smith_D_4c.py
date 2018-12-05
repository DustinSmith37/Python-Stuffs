#Dustin Smith
#Project 4c
#This averages 5 test grades

#establish variables
totalTestGrade = 0
numberOfTests = 5

#establish for loop for input
for i in range(numberOfTests):
    test = float(input("Please input the grade for test number "+str(i+1)+": "))
    totalTestGrade = totalTestGrade + test

#calculate average
average = totalTestGrade / numberOfTests

#output the data
print("The average grade of these 5 tests grades is", format(average, '.2f'))