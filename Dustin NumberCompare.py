#Dustin Smith
#Number Compare

#Get ints
def getnum():
    while True:
        try:
            num = input("Input an integer: ")
            if int(num) == float(num):
                return num
        except ValueError:
            print("Invalid input")

#Compare ints
def max(num1,num2):
    if num1>num2:
        return str(num1) + " is greater than " + str(num2)
    elif num1<num2:
        return str(num2) + " is greater than " + str(num1)
    else:
        return str(num2) + " and " + str(num1) + " are equal"

#Main function
def main():
    num1 = getnum()
    num2 = getnum()

    print(max(num1,num2))

main()