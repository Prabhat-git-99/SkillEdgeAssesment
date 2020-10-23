###########################################
# Author: Prabhat Kumar Singh
# Language: Python
# Problem Statement: Problem(5) Write a function that takes an array and return an array of the sum of parts of the array
# Input: 1. First Line number of Query
#        2. Second Line Enter Array
#        3. Third Line is Output
# Contact: prabhat9kumar9singh9@gmail.com 
###########################################

def sumInPattern(array):
    total = 0
    result = [0]
    # loop through array, add elements from last to total and append into result
    for i in range(len(array)):
        total += array[-i-1]
        result.append(total)
    # return elements in reverse order
    return result[::-1]

if __name__ == "__main__":
    query = input("Enter number of query: ")
    for i in range(int(query)):
        array = list(map(int, input('Enter array: ').split()))
        result = sumInPattern(array)
        print(result)