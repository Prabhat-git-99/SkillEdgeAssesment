###########################################
# Author: Prabhat Kumar Singh
# Language: Python
# Problem Statement: Problem(6) Find the longest substring in alphabetical order.
# Input: 1. First Line number of Query
#        2. Second Line Enter String
#        3. Third Line is Output
# Contact: prabhat9kumar9singh9@gmail.com 
###########################################

def longestAlpha(string):
    result = ""
    max =""
    for i in range(len(string) -1):

        # check consecutive element if they are in order or not
        if(string[i] <= string[i+1] ):
            # if they are in order append into result variable
            result = result + string[i]
            # when reach to the end, append last element to result
            if(i==len(string) -2):
                result = result + string[i+1]
        
        # if consecutive elements are not in order
        else:
            result  = result + string[i]        
            # if length of result(prev stored seq) is greater than max seq(initially empty) then make max equals result
            if(len(result) > len(max)):
                max = result
            result = ""        

    if(len(string) == 1):
        result = string
    return result

if __name__ == '__main__':
    query = input("Enter number of Query: ")
    for i in range(int(query)):
        string = input("Enter String: ")
        result = longestAlpha(string)
        print('Longest sequence is: '+result)
    
