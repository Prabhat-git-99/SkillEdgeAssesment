###########################################
# Author: Prabhat Kumar Singh
# Language: Python
# Problem Statement: Problem(2) you will be given a string that may have mixed uppercase and lowercase letters and your task is to
#                               convert that string to either lowercase only or uppercase only based on:
#                               if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.
# Input: 1. First Line number of Query
#        2. Enter your word
#        3. Third Line is Output
# Contact: prabhat9kumar9singh9@gmail.com 
###########################################

def changeWord(word):
    upper = 0
    lower = 0
    upperIndex = []
    lowerIndex = []
    length = len(word)

    # Approach is: loop through all letter in word, check if it's lower or upper case & count their number
    # if it's uppercase then store in upperIndex array else in lowerIndex array, 
    # if len(upper)>len(lower) then we need to change only corresponding element which
    # we can acccess through respective Array

    for i in range(length):
        if word[i].isupper() == True:
            upper += 1
            upperIndex.append(i)
        else:
            lowerIndex.append(i)
    lower = length - upper
    # print(upperIndex)

    if lower > upper or lower == upper:
        for i in upperIndex:
            word[i] = chr(ord(word[i]) + 32)
        return word
    else:
        for i in lowerIndex:
            word[i] = chr(ord(word[i]) - 32)
        return word

if __name__ == '__main__':
    query = input('Enter number of query: ')
    for i in range(int(query)):
        word = input("Enter Your Word: ")
        # word = ''.join(word.split())
        result = changeWord(list(word))
        print("Changed word is: "+''.join(result))