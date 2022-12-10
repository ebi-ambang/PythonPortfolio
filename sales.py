#####A basic calulator that will sum up items ordered at a restaurant and print it on a receipt (text file)#####
#Items that were ordered
items = {"mac&cheese" : 15,
         "lobster" : 50,
         "steak" : 45,
         "mash potatoes" : 10,
         "salad" : 15,
         "crab cakes": 40,
         "brocolini" : 15
         }
#Sum all the items for the dinner order
sum_of_dinner = str(sum(items.values()))

def receipt(text):
    with open('receipt.txt', 'a') as f:
        f.write(text)
#Introduction tot the receipt
total = "The sum total of today's dinner is:$"

#calling on the funtion to print the receipt an total
receipt(total) 
receipt(sum_of_dinner)