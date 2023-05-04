# define a function with 3 parameteres 

def mutate_string(string, position ,character):
#convert string to be a list for indexing
    list_string=list(string)

    #customize value of character to position of changeable value of index
    list_string[position] = character

#convert list to a string again
    output = ''.join(list_string)
    return output


str = 'abracadabra'
position = 5
character = 'k'

print (mutate_string(str , position, character))



def mutated_string (string, position, character):
    if 0 <= position < len(string):
        return  string[:position] + character+ string[position+1:]
    
str = 'abracadabra'
position = 5
character = 'k'
 

print (mutated_string(str , position, character))
