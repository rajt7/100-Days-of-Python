#Addition
def add(num1, num2):
    return num1 + num2


#Subtraction
def sub(num1, num2):
    return num1 - num2


#Multiplication
def mul(num1, num2):
    return num1 * num2


#Division
def div(num1, num2):
    return num1 / num2


#Exponent
def exponent(num1, num2):
    return num1 ** num2


#Driver Code
num1 = float(input('Enter number 1: '))
operations = {'+': add, '-': sub, '*': mul, '/': div, '^': exponent}

#printing all the operations
for symbol in operations:
    print(symbol)

should_continue = True

while should_continue:
    operation_symbol = input('What operation you have to use?: ')
    num2 = float(input('Enter number 2: '))

    #getting the answer
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' if you want to continue with {answer} or type 'n' to exit.: ") == 'y':
        num1 = answer
    else:
        should_continue = False
