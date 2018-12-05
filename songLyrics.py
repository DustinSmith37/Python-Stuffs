#create text file
outfile = open('sandwich.txt', 'w')
outfile.write('This is not a song\n')
outfile.write('Its a sandwich\n')
outfile.write('What would make you think otherwise?')
outfile.close()
#read text file and output
readfile = open('sandwich.txt', 'r')
song = readfile.read()
print(song)
readfile.close()