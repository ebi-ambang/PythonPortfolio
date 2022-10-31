
# Program to calculate the sum of two numbers. The program will ask for two numbers (integer or float) and then calculate the sum of those two numbers
from pydoc import cli

year_of_birth = int(input("year you were born:\n"))
client_age = int(input("your age:\n"))

current_year = int(year_of_birth) + int(client_age)

#Displays the current year which is the sum of the two numbers above 
print(f"Current year is: {current_year}") 



#  Program that will ask for a user's body weight in pounds and converts it to kilograms
body_weight_Ibs = int(input("enter your body weight in Ibs:\n"))
equivalent_in_kg = int(body_weight_Ibs) * 0.453592

#prints the equivalent in kg with only 3 decimal places
print(f"equivalent body weight in kg is: {equivalent_in_kg:.5}")


#Program that will display the accountID from this AWS arn - arn:aws:iam::123456789012:user/Development/product_1234/*

aws_account_id = "arn:aws:iam::123456789012:user/Development/product_1234/*"
print(f"The account id is: {aws_account_id[13:25]}") 

#Playing around with reversing a word
fun_word = "hannah"
print(f"the name of the day is: {fun_word.title()}, and the reverse of the name is also: {fun_word[::-1].title()}")