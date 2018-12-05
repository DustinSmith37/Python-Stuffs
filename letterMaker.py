#Dustin Smith
#Letter Maker
#Makes a letter out of *

#Create functions
def letterD():
    for num in range(5):
        if num == 0 or num == 4:
            print("****")
        elif num == 2 or num == 3 or num == 1:
            print("*    *")

def letterQ():
    for num in range(5):
        if num == 0 or num == 3:
            print(" * * * ")
        elif num == 1:
            print("*     *")
        elif num == 2:
            print("*   * *")
        elif num == 4:
            print("      *")
#Call functions
letterD()
letterQ()
