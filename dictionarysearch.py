#Program that allows you reference a specific empoyee. 
#This shall print out the last name of the second employee

HR = {"employees":[{"firstName": "John", "lastName": "Doe"},
                  {"firstName": "Anna", "lastName": "Smith"},
                  {"firstName": "Peter", "lastName": "Jones"}],
     "owners":[{"firstName": "Jack", "lastName": "Petter"},
               {"firstName": "Jessy", "lastName": "Petter"}]}

print(HR["employees"][1]["lastName"])