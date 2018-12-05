#Dustin Smith
#Letter Shifter
#Shifts a string by a certain amount

#create variables
validString = False
validShift = False
newString = ''
newLetter = ''
alphabet = ['a','b','c','d','e','e','f','g','h','i','j',\
            'k','l','m','n','o','p','q','r','s','t','u',\
            'v','w','x','y','z','A','B','C','D','E','F',\
            'G','H','I','J','K','L','M','N','O','P','Q',\
            'R','S','T','U','V','W','X','Y','Z']

#take and convert input
originalString = input("Input a sentence, all characters allowed: ")
while validString != True:
    if bool(originalString.strip()) == False:
        originalString = input("Don't input nothing! Input a sentence, all characters allowed: ")
    else:
        validString = True

shift = input("How many letters back would you like to shift?")
while validShift != True:
        try:
            shift = int(shift)
            validShift = True
        except ValueError:
            shift = input("Invalid input, whole number please: ")

#transforms and adds to new string
for letter in originalString:
    if letter in alphabet:
        counter = alphabet.index(letter)
        for i in range(shift):
            counter -= 1
            if counter == 26:
                counter = 51
            elif counter < 0:
                counter = 26
        newLetter = alphabet[counter]
        newString += newLetter
    else:
        newString += letter
#display output
print(newString)        
