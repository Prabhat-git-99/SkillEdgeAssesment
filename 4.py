###########################################
# Author: Prabhat Kumar Singh
# Language: Python
# Problem Statement: Problem(4) Create a function that change the words of a sentence to CamelCase.
# Input: 1. First Line number of Query
#        2. Second Line Enter Word
#        3. Third Line is Output
# Contact: prabhat9kumar9singh9@gmail.com 
###########################################

def camelCase(string):

    # split string into array
    # only capitalize first letter of each word and copy into one variable

    string = string.split()
    newStr = ''
    for word in string:
        newStr += word[0].upper()
        newStr += word[1:]
    return newStr

if __name__ == "__main__":
    query = input("Enter number of query: ")
    for i in range(int(query)):
        string = input("Enter string: ")
        result = camelCase(string)
        print('Camecase: '+result)