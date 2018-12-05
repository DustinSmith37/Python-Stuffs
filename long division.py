#get inputs
dividend = int(input('What are you dividing? '))
divisor = int(input('What are you dividing by? '))

#calculate division
floatDivide = dividend/divisor
intDivide = dividend//divisor
remainder = dividend%divisor

#display results
print()
print("\tResults:")
print("\t", format(floatDivide, '.2f'))
print(intDivide, "with remainder of", remainder)

