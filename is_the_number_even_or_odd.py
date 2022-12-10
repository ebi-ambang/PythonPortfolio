#####Program to determine if a number is even or odd#####

# defing function even_or_odd_number that checks if a number is even or odd and displays it on the screen
def even_or_odd_number(n):
    if n % 2 == 0:
        print(n," is an EVEN number")
    else:
        print(n," is an ODD number")

# Main body of the prgram where the code starts running
while True:  
    # ask user to enter a number between 1 and 100
    # function 'input' returns string, so we cast it into integer with int() function, so that we can compare it with another integer 
    number = int(input("Please enter a number between 1-100: \n"))
    # if number is less than 0 or greater than 100, print "Invalid input"
    if number < 0 or number > 100:
        print("Invalid input")
    # if number between 1 and 100, call even_or_odd_number function
    else:
        even_or_odd_number(number)
    # ask user if they want to do another number and make the input lowercase
    more_numbers = input("Check another number? / If no, type 'n', If yes, hit enter\n").lower()
    # if answer is no
    if more_numbers == 'n':
        # break out of the while loop
        break