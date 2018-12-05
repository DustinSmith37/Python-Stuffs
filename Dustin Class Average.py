#Dustin Smith
#Class Average
#Gets class average using class amounts, students amounts, and grades

#import input checker
import inputChecker

#calculates the average grade for the class
def output_average(totalGrade, numberOfStudents, x):
    average = totalGrade/numberOfStudents
    print("\nThe class average for class number", x+1, "is", format(average, '.2f'))

#takes class number input, student number input, and grade, and calls average function
def loop_function():
    numberOfClasses = inputChecker.IntPos("How many classes do you have? ")
    for x in range(numberOfClasses):
        totalGrade = 0
        numberOfStudents = inputChecker.IntPos("How many students are in class " + str(x+1) + "? ")
        for i in range(numberOfStudents):
            totalGrade = totalGrade + inputChecker.FloatPos("What is the grade for student " + str(i+1) + "? ")
        output_average(totalGrade, numberOfStudents, x)

#its the main function, it just calls loop_function
def main():
    loop_function()

main()