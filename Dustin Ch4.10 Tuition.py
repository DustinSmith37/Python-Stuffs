#Dustin Smith
#Problem 10 "Tuition increase"
#Calculates increase of cost over semesters

startingTuition = 8000
print("Year\t     Semester\t\tTuition Cost\n---------------------------------------------")
newTuition = 8000

for years in range(5):
    newTuition *= 1.03
    print(' ',years+1,"\t\t1", '\t\t$', format(newTuition, '.2f'),"\n ", years+1, "\t\t2", '\t\t$', format(newTuition, '.2f'))
