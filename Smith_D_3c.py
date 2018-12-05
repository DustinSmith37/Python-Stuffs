#Dustin Smith
#Project 3c
#Takes inputs of horse race times and declares winner

#Gather inputs
horse1 = float(input("Please input the time of the first horse: "))
horse2 = float(input("Please input the time of the second horse: "))
horse3 = float(input("Please input the time of the third horse: "))

#Process to find winner
if horse1 < horse2 and horse1 < horse3:
    print("The winner is the first horse with a time of", horse1, "seconds.")
elif horse2 < horse1 and horse2 < horse3:
    print("The winner is the second horse with a time of", horse2, "seconds.")
elif horse3 < horse1 and horse3 < horse2:
    print("The winner is the third horse with a time of", horse3, "seconds.")
elif horse1 == horse2 and horse1 < horse3 and horse2 < horse3:
    print("The winner is a tie of the first and second horses with a time of", horse1, "seconds.")
elif horse1 == horse3 and horse1 < horse2 and horse3 < horse2:
    print("The winner is a tie of the first and third horses with a time of", horse1, "seconds.")
elif horse3 == horse2 and horse3 < horse1 and horse2 < horse1:
    print("The winner is a tie of the second and third horses with a time of", horse2, "seconds.")
elif horse1 == horse2 and horse1 == horse3 and horse2==horse3:
    print("It was a three way tie with all horses finishing in", horse1,"seconds.")
