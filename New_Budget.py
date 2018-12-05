#Dustin Smith
#Budget Analysis 2.0
#Collects user budget and displays amounts remaining

#import input checker
import inputChecker

#get expenses from user
def get_expenses():
    expenses = inputChecker.FloatPos("\nInput your expense, input 0 to end: ")
    return expenses

#compares amount spent to budget and subtracts it
def analyze_spending(budget):
    expense = 'placeholder'
    counter = 1
    while expense != 0:
        expense = get_expenses()
        budget = budget - expense
        counter += 1
        print(format(budget, '.2f'), "dollars remaining.")
        if budget < 0: 
            print("Warning! Going over budget!")
        else:
            print("You are still under budget.")
    return budget
#main function
def main():
    budget = inputChecker.FloatPos("What is your budget? ")
    finalBudget = analyze_spending(budget)
    print("\nFinal amount remaining:", format(finalBudget, '.2f'), "dollars")
    
main()
