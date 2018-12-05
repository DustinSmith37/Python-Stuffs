#Dustin Smith
#numeric data
#processes numeric data from a file

#creates and writes file
openfile = open('numbers.txt', 'w')
openfile.write('9\n20\n30\n5')
openfile.close()

#reads and calculates from file
readfile = open('numbers.txt', 'r')
total = 0
numbers = 0
for line in readfile:
    total += int(line)
    numbers += 1

average = total/numbers
readfile.close()

appendfile = open('numbers.txt', 'a')
appendfile.write('\nSum of numbers: '+str(total))
appendfile.write('\nNumber of numbers: '+str(numbers))
appendfile.write('\nAverage of the numbers: '+str(format(average, '.2f')))
appendfile.close()
