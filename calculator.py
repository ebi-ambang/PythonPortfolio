####The following is a basic calculator####

# Define a function that exponentiates two numbers
def exponent(x, y):
    return x ** y
# define a function that divides two numbers
def divide(x, y):
    return x / y
# define a function that multiplies two numbers
def multiply(x, y):
    return x * y
# define a function that adds two numbers
def add(x, y):
    return x + y
# define a function that subtracts two numbers
def subtract(x, y):
    return x - y
# define a function that returns the remainder when 2 numbers are divided
def modulo(x, y):
    return x % y


# display on the screen
print("\nThisis a basic calculator which has the the following operations: \n")
print(" ** Exponent")
print(" / Division")
print(" * Muliplication")
print(" + Addition")
print(" - Subtraction")
print(" % Modulo")

# make a list with the possible operations
operators = ['**','*','/','+','-','%']

while True:
    # ask user what operation they want to perform
    select = input("Select an operation **, *, /, +, -, %\n")
    # chack if the operation user selected is in the possible operations
    # if the operation is in the list of possible operations
    if select in operators:
        # ask user for two numbers
        a = float(input("Enter a number/can be integer or floating point/: "))
        b = float(input("Enter another number/can be integer or floating point/: "))
        # according to the operation user selected, call the corresponding function and display the output
        if select == '**':
            print(exponent(a, b))
        elif select == '*':
            print(multiply(a, b))
        elif select == '/':
            print(divide(a, b))
        elif select == '+':
            print(add(a, b))
        elif select == '-':
            print(subtract(a, b))
        elif select == '%':
            print(modulo(a, b))
        
        # ask user if they want to do another calculation
        another = input("Perform another calculation? / If no type 'n', If yes, hit enter\n").lower()
        # if answer is no, break out of the whole loop
        if another == 'n':
            break
    # if the operation user selected is NOT in the list of possible operations print "Invalid input."
    else:
        print("Invalid input.")
# when out of the while loop, print "Thank you!"
print("Thank you!")