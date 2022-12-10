##### A program the will copy a file content and replicate it in another file ########
#This function will write some poetry from the Poem "A Poison Tree" by William Blake
def poetry(text):

#Create a file called poetry.txt
    with open('poetry.txt', 'w') as f:
        f.write('\n'.join(text))
        
poem = ['A POISON TREE''-''WILLIAM BLAKE',
        'I was angry with my friend;', 
        'I told my wrath, my wrath did end.', 
        'I was angry with my foe:', 
        'I told it not, my wrath did grow.', 

        'And I waterd it in fears,',
        'Night & morning with my tears:', 
        'And I sunned it with smiles,',
        'And with soft deceitful wiles.', 

        'And it grew both day and night.',
        'Till it bore an apple bright.' ,
        'And my foe beheld it shine,',
        'And he knew that it was mine.', 

        'And into my garden stole, ',
        'When the night had veild the pole;', 
        'In the morning glad I see; ',
        'My foe outstretched beneath the tree.',  ] 

poetry(poem)

#This function will replicate a txt file called poetry into another file called newpoetry
def copy(poetry, newpoetry):
    #Replicate the poem in a new text file
    with open('poetry.txt', 'r') as first, open ('newpoetry.txt', 'w') as second:
        for text in first:
            second.write(text)
#call the function
copy('poetry.txt', 'newpoetry.txt')