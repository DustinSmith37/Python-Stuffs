#Dustin Smith
#Project 5b
#This uses a function to calculate the assessed value and the property tax

#create main function to output variables
def main():
    actualValue = float(input("Input the actual value of the property: "))
    assessedValue = assessed_value_converter(actualValue)
    propertyTax = property_tax_converter(assessedValue)
    print("$" + str(format(assessedValue,'.2f')),"is the assessed value of the property\
    and $" + str(format(propertyTax,'.2f')), "is the property tax of it.")

#create assessed value function
def assessed_value_converter(actualValue):
    percentAssessedValue = .60
    assessedValue = actualValue * percentAssessedValue
    return assessedValue

#create property tax value
def property_tax_converter(assessedValue):
    percentPropertyTax = .0072
    propertyTax = assessedValue * percentPropertyTax
    return propertyTax

#call main
main()