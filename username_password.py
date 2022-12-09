###### A program that prompts users for their user name and password. If the out put is incorrect 5 times. The accoutn gets locked.######

# Database of users and associated passwords
database = [{"username" : "Oliver", "password" : "qui3tHoney53"},
            {"username" : "Zuby", "password" : "$lowRay67"},
            {"username" : "Anna", "password" : "lushBra!n42"},
            {"username" : "Levi", "password" : "$limFlock92"}
            ]

# The initializing variables are username and password
username = ' '
password = ' '


# Prompt  the users to nter their information
enter_username = ''
enter_password = ''


# Set the maximum number of times a user s allowed to enter their information.
n = 5
access_granted = bool()


# Cycle through the loop to check if the information matches.
while enter_username != username or enter_password != password:
    enter_username = input("Please enter your username: ")
    enter_password = input("Please enter your password: ")
    # If information entered is incorrect, decrease the number of tries by 1
    n -= 1
    # Check if information eneterd macthes what is in database
    for i in database:
        username = i["username"]
        password = i["password"]
        # if credentials correct, grant access and stop
        if enter_username == username and enter_password == password:
            access_granted = True
            print("Access granted")
            break
    # if number of tries less than 5 and bigger than zero, and access not granted, print "Incorrect credentials. Please try again."
    if   5 > n > 0 and access_granted == False:
        print("Incorrect credentials. Please try again.")
    # if number of tries is equel to zero, and access is not granted, lock account
    elif n == 0 and access_granted == False:
        print("Account locked")
        break