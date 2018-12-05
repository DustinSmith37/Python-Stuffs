import ABC_Printer
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l",\
"m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def inputChecker(inputTopic,alphabet):
    while True:
        try:
            userInput = input(inputTopic).lower()
            userInput = userInput.replace(" ","")
            if userInput.isalpha() == False:
                int('a')
            return userInput
        except ValueError:
            print("Invalid input")
string = inputChecker("Input your string:", alphabet)

for letter in string:
    if letter == alphabet[0]:
        ABC_Printer.print_A()
        print()
    elif letter == alphabet[1]:
        ABC_Printer.print_B()
        print()
    elif letter == alphabet[2]:
        ABC_Printer.print_C()
        print()
    elif letter == alphabet[3]:
        ABC_Printer.print_D()
        print()
    elif letter == alphabet[4]:
        ABC_Printer.print_E()
        print()
    elif letter == alphabet[5]:
        ABC_Printer.print_F()
        print()
    elif letter == alphabet[6]:
        ABC_Printer.print_G()
        print()
    elif letter == alphabet[7]:
        ABC_Printer.print_H()
        print()
    elif letter == alphabet[8]:
        ABC_Printer.print_I()
        print()
    elif letter == alphabet[9]:
        ABC_Printer.print_J()
        print()
    elif letter == alphabet[10]:
        ABC_Printer.print_K()
        print()
    elif letter == alphabet[11]:
        ABC_Printer.print_L()
        print()
        print()
    elif letter == alphabet[12]:
        ABC_Printer.print_M()
        print()
    elif letter == alphabet[13]:
        ABC_Printer.print_N()
        print()
    elif letter == alphabet[14]:
        ABC_Printer.print_O()
        print()
        print()
    elif letter == alphabet[15]:
        ABC_Printer.print_P()
        print()
    elif letter == alphabet[16]:
        ABC_Printer.print_Q()
        print()
    elif letter == alphabet[17]:
        ABC_Printer.print_R()
        print()
    elif letter == alphabet[18]:
        ABC_Printer.print_S()
        print()
    elif letter == alphabet[19]:
        ABC_Printer.print_T()
        print()
    elif letter == alphabet[20]:
        ABC_Printer.print_U()
        print()
    elif letter == alphabet[21]:
        ABC_Printer.print_V()
        print()
    elif letter == alphabet[22]:
        ABC_Printer.print_W()
        print()
    elif letter == alphabet[23]:
        ABC_Printer.print_X()
        print()
    elif letter == alphabet[24]:
        ABC_Printer.print_Y()
        print()
    elif letter == alphabet[25]:
        ABC_Printer.print_Z()
        print()
