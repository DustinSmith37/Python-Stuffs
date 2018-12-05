#Dustin Smith
#Budget Analysis

#import input checker
import inputChecker

#calculator function
def calculator(budget):
    expense = 'placeholder'
    counter = 1
    while expense != 0:
        expense = inputChecker.FloatPos("\nPlease input expense number " + str(counter) + ", input 0 to end: ")
        budget = budget - expense
        counter += 1
        print(format(budget, '.2f'), "dollars remaining.")
        if budget < 0: print("Warning! Going over budget!")
    return budget
#main function
def main():
    budget = inputChecker.FloatPos("What is your budget? ")
    budget = calculator(budget)
    print("\nFinal amount remaining:", format(budget, '.2f'), "dollars")
    
main()
