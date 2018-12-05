#Dustin Smith
#Dual number checker
#Checks if the input is prime and/or in the fibonacci sequence

#Ask for input
number = int(input("What number would you like to check? No floats or the number one! "))

#current model for checking prime
divisor = 2
counter = 0
while divisor != number:
    if number % divisor == 0:
        break
    elif number == 1:
        print("Hey, you cant use one!")
        break
    else:
        counter += 1
        divisor += 1
if number == 1:
    print("Of course its prime, its one!")
elif counter == number - 2:
    print(number, "is prime!")
else:
    print(number, "is not prime!")
#fibonacci sequence checker
a,b = 0,1
secondCounter = 0
isFibo = False
while b < number+a:
    if number == a or number == b:
        print(number, "is part of the fibonacci sequence!")
        isFibo = True
        break
    else:
        a,b = b, a+b
if number == 1:
    print("You broke everything! Good job. But 1 is part of the fibonacci sequence")    
elif isFibo != True:
    print(number, "is not part of the fibonacci sequence!")
else:
    None
    

