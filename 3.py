###########################################
# Author: Prabhat Kumar Singh
# Language: Python
# Problem Statement: Problem(3) Create a function that takes an integer n greather than 1 and returns an array with all of the integer
# Input: 1. First Line number of Query
#        2. Second Line Enter Number
#        3. Third Line is Output
# Contact: prabhat9kumar9singh9@gmail.com 
###########################################

def allDivisors(number):
    divisors = []
    length = 0
    
    # loop till number//2, because greater than half can never be factor for number
    # if number on division gives 0 remainder then it's factor

    for i in range(2,number//2 + 1):
        if number%i == 0:
            divisors.append(i)
            length += 1
    if length > 0:
        return divisors
    
    # if no divisors then it's prime number
    else:
        return f"{number} is prime"

if __name__ == '__main__':
    query = input('Enter number of times to run: ')
    for i in range(int(query)):
        number = input("Enter Number greater than 1: ")
        try: 
            if int(number) > 1:
                result = allDivisors(int(number))
                print(result)
            else:
                print("Please enter number greater than 1")
        except ValueError:
            print("Enter integer value!")
        
