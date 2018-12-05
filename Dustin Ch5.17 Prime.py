#Dustin Smith
#Chapter 5.17
#This checks if a number is prime or not

#import input checker
import inputChecker

#this loops to check all possible factors of the number
def is_prime(userNumber):
    divisor = 2
    if userNumber == 0 or userNumber == 1 or userNumber == 2: return True
    for i in range(userNumber - 2):
        currentDivisorCheck = divisor_checker(divisor, userNumber)
        if currentDivisorCheck == True:
            return False
        else:
            divisor = divisor + 1
    return True


#this function checkes to see if the number can be divided by the current divisor
def divisor_checker(divisor, userNumber):
    if userNumber % divisor == 0:
        return True
    else:
        return False

#this is the main function and outputs if the number is prime or not
def main():
    userNumber = inputChecker.IntPos("Input a postive integer to check if its prime: ")
    isPrime = is_prime(userNumber)
    if isPrime == True:
        print(userNumber, "is prime!")
    else:
        print(userNumber, "is not prime!")

#call main
main()