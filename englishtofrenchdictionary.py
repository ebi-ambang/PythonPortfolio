#####A more robust form of the english to french dictionary#######
#The current dictionay
english_to_french_dictionary={
"prune" : "plum",
"love": "aimer",
"handsome": "beau",
"work": "travailler",
"movie": "film",
"africa": "afrique"
}

#Defining the function for the words to be translated
def french(word):
    #If the word is in the dictionary display it on the screen 
    if word in english_to_french_dictionary:
        print(english_to_french_dictionary.get(word))
    #If word is not in the dictionary display the follwing:
    else:
        print(f"The word {word} does not exist in the dictionary.")

#Run a loop so that you can continually translate words without interuption
while True:
    #Enter the word you would like to be translated
    translated_word = input("What word would you like to translate?  ").lower()
    #call on the function to translate the word
    french(translated_word)
    #Ask if they would like another word to be translated to keep going
    more_translations = input("Check another word? / If no, type 'n', If yes, hit enter\n").lower()
    # if answer is no
    if more_translations == 'n':
        # break out of the while loop
        break




