#------------------------------------------------------------
# MODULE:   ABC_Printer
# PURPOSE:  This module contains functions
#           to print letters of alphabet in STAR FONT.
#------------------------------------------------------------

#letter A printer
def print_A():
    for num in range(5):
        if num == 0:
            print('  *  ')
        elif num == 1:
            print(' * * ')
        elif num == 2:
            print('*****')
        elif num == 3 or num == 4:
            print('*   *')


#letter B printer
def print_B ():
    for i in range (1, 6):
        if i == 1 or i == 3 or i == 5:
            print("****")
        if i == 2 or i == 4:
            print("*   *")

#letter C printer
def print_C():
    for i in range(5):
        if i == 0 or i == 4:
            print(" ****")
          
        if 1 <= i <= 3:
            print("*")

#letter D printer
def print_D():
   for num in range(5):
       if num == 0 or num == 4:
           print("****")
       elif num == 2 or num == 3 or num == 1:
           print("*    *")

#letter E printer
def print_E():
    for counter in range(5):
        if counter == 0 or counter == 4:
            print("* * * *")
        elif counter == 1 or counter == 3:
            print("*")
        elif counter == 2:
            print("* * *")


#letter F printer
def print_F():
   for i in range(5):
        if i == 0:
           print("*****")
        elif i == 2:
            print("***")
        elif i == 1 or i == 3 or i == 4:
            print("*")


#letter G printer
def print_G():
    for i in range(5):
        if i == 0 or i == 4:
            print("*****")
        elif i == 1:
            print("*")
        elif i == 2:
            print("*  **")
        elif i == 3:
            print("*   *")

#Letter H printer
def print_H():
    for i in range(5):
        if i == 2:
            print('*****')
        else:
            print('*   *')

#Letter I printer
def print_I ():
    for i in range (1,6):
        if i == 1 or i == 5:
            print("*****")
        if i == 2 or i == 3 or i == 4:
            print("  *  ")

#letter J printer
def print_J():
    for i in range(5):
        if i == 0:
            print(" *****")
        elif i == 1 or i == 2:
            print("   *")
        elif i == 3:
            print("*  *")
        elif i == 4:
            print(" **")

#letter K printer
def print_K():
   for num in range(5):
       if num == 0 or num == 4:
           print("*   *")
       elif num == 1 or num == 3:
           print("*  *")
       elif num == 2:
           print("***")

#letter L printer
def print_L():
    for col in range (4) :
        print('*')
    for col in range (5) :
        print('*',end='' )

#letter M printer
def print_M ():
    for i in range (1,6):
        if i == 1  or  i ==4  or  i == 5 :
            print('*       *')
        elif i == 2:
            print('* *   * *')
        elif i == 3:
            print('*   *   *')

#letter N printer
def print_N():
    for i in range(5):
        if i == 0:
            print("*    *")
        elif i == 1:
            print("* *  *")
        elif i == 2:
            print("*  * *")
        elif i == 3:
            print("*   **")
        elif i == 4:
            print("*    *")

#letter O printer
def print_O():
    for col in range (4) :
        print('*',end='')
    print('*')
    for col in range (0):
        print('*',end='')
    for col in range (3) :
        print('*','  *')
    for col in range (5) :
        print('*',end='' )

#letter P printer
def print_P():
   for i in range(5):
        if i == 0 or i == 2:
           print("****")
        elif i == 1:
            print("*    *")
        elif i == 3 or i == 4:
            print("*")

#letter Q printer
def print_Q():
   for num in range(5):
       if num == 0 or num == 3:
           print(" * * * ")
       elif num == 1:
           print("*     *")
       elif num == 2:
           print("*   * *")
       elif num == 4:
           print("      *")


#letter R printer
def print_R():
    for i in range(5):
        if i == 0 or i == 2:
            print("****")
        elif i == 1 or i == 4:
            print("*   *")
        elif i == 3:
            print("*  *")


#letter S printer
def print_S():
    for i in range(5):
        if i == 0 or i == 2 or i == 4:
            print("*****")
        if i == 1:
            print("*")
        if i == 3:
            print("    *")

#letter T printer
def print_T():
    for i in range(5):
        if i == 0:
            print("*****")
        elif i == 1 or i == 2 or i == 3 or i == 4:
            print("  *")

#letter U printer
def print_U():
    for i in range(5):
        if i == 0 or i == 1 or i == 2 or i == 3:
            print("*    *")
        elif i == 4:
            print(" ****")

#letter V printer
def print_V():
    for i in range(5):
        if i == 0 or i == 1 or i == 2:
            print("*   *")
        elif i == 3:
            print(" * *")
        elif i == 4:
            print("  *")
                
#letter W printer
def print_W():
    for i in range(5):
        if i == 0 or i == 1:
            print("*     *")
        elif i == 4:
            print(" *   *")
        elif i == 3:
            print("* * * *")
        elif i == 2:
            print("*  *  *")



#letter X printer
def print_X():
    for i in range(5):
        if i == 0 or i == 4:
            print("*   *")
        elif i == 1 or i == 3:
            print(" * *")
        elif i == 2:
            print("  *")

#letter Y printer
def print_Y():
    for i in range(5):
        if i == 0:
            print("*   *")
        elif i == 1:
            print(" * *")
        elif i == 2 or i == 3 or i == 4:
            print("  *")

#letter Z printer
def print_Z():
    for num in range(5):
        if num == 0 or num == 4:
            print('* * * *')
        elif num == 1:
            print('     *')
        elif num == 2:
            print('   *')
        elif num == 3:
            print(' *')





