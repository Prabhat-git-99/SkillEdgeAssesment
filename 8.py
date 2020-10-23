###########################################
# Author: Prabhat Kumar Singh
# Language: Python
# Problem Statement: Problem(7) The goal of this exercise is to convert a string to a new string where each character in the new string
#       is &quot;(&quot; if that character appears only once in the original string, or &quot;)&quot; if that character appears more
#       than once in the original string.
# Input: 1. First Line number of Query
#        2. Second Line Enter String
#        3. Third Line is Output
# Contact: prabhat9kumar9singh9@gmail.com 
###########################################


from collections import Counter

def newString(string):

    # make dictionary of letter to find repetationd
    dicti = dict(Counter(string))
    result = ''
    for i in string:
        if i in dicti:
            # if value is greater than 1, append ')' which shows repeatation
            if dicti[i] > 1:
                result += ')'
            else:
                result += '('
    return result


if __name__ == '__main__':
    query = input("Enter number of Query: ")
    for i in range(int(query)):
        string = input("Enter String: ")
        result = newString(string.lower())
        print(result)