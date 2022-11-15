# write a code that will automatically translate an input from a user to ENGLISH.
# And if that input from user does not exixt in your ditionary, 
# simply return "input" does not exixt in the dictionary.
language = input("Select language you would like to translate into:")
language = language.lower()

word = input("What word would you like to translate?  ")
word = word.lower() 


english_to_french_dictionary={
"prune" : "plum",
"love": "aimer",
"handsome": "beau",
"work": "travailler",
"movie": "film",
"africa": "afrique"
}

if language == "french":
    if word in english_to_french_dictionary:
        print(english_to_french_dictionary.get(word))
    else:
        print(f"The word {word} does not exist in the dictionary.")