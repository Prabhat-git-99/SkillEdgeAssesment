###########################################
# Author: Prabhat Kumar Singh
# Language: Python
# Problem Statement: Problem(7) Given a string representing a simple fraction x/y, your function must return a string representing the
#                                  corresponding mixed fraction in the following format:
# Input: 1. First Line number of Query
#        2. Second Line Enter String (Ex 5/9, -5/9)
#        3. Third Line is Output
# Contact: prabhat9kumar9singh9@gmail.com 
###########################################

def findHcf(num1, num2):
    while num2:
        num1, num2 = num2, num1%num2
    return num1

def mixedFraction(num, deno):

    # find hcf to simplify fraction
    if num >= deno:
        hcf = findHcf(deno, num)
    else:
        hcf = findHcf(num, deno)

    # simplify numerator and denominator    
    num = num//hcf
    deno = deno//hcf
    
    # find quotient and remainder
    quot = num//deno
    rem = num%deno
    if rem == 0:
        string = f"{quot}"
    else:
        string = f"{quot} {rem}/{deno}"
    return string


if __name__ == "__main__":
    query = input("Enter number of Query: ")
    for i in range(int(query)):
        string = input('Enter M/N: ').split('/')
        num = string[0]
        deno = string[1]
        if int(deno) == 0:
            print('Enter non-zero element!')
            break
        if int(num) < 0:
            num = abs(int(num))
            result = mixedFraction(int(num), int(deno))
            print('-'+result)
        else:
            result = mixedFraction(int(num), int(deno))
            print(result)