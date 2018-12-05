#Dustin Smith
#Final Project B
#Checks if the user input is a prime number

#Ask for input
userNumber = int(input("What whole number would \
you like to check? It must be greater than 1! "))

#checks if a number is prime by using increasing divisors and a counter to keep
#track of if it reaches the number inputed by the user.
divisor = 2
counter = 0
while divisor != userNumber:
    if userNumber % divisor == 0:
        break
    elif userNumber == 1:
        print("Hey, you cant use one!")
        break
    else:
        counter += 1
        divisor += 1
if userNumber == 1:
    print("Of course its prime, its one!")
elif counter == userNumber - 2:
    print(userNumber, "is prime!")
else:
    print(userNumber, "is not prime!")