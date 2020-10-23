###########################################
# Author: Prabhat Kumar Singh
# Language: Python
# Problem Statement: Problem(1) Try to create a function to generate such patterns of door mat.
# Input: 1. First Line number of Query
#        2. Second Line Enter M N
#        3. Third Line is Output
# Contact: prabhat9kumar9singh9@gmail.com 
###########################################

def makeDesign(m,n):
    text = 'WELCOME'
    mid = m//2
    dot = 1
    for i in range(m):
        # number of dot(.|.) in each line
        side = n-dot*3
        # if i is smaller than mid , increase dot pattern
        if i < mid:
            print('-'*(side), end='')
            print('. | . '*dot, end='')
            print('-'*side, end='') 
            dot = dot + 2
        # id i==mid then print welcome
        if i == mid:
            print('-'*(n-(len(text))//2), end='')
            print(text, end='')
            print('-'*(n-(len(text))//2 - 1), end='')
            dot = dot - 2
        # if i is smaller than mid , decrease dot pattern
        if i > mid:
            print('-'*(side), end='')
            print('. | . '*dot, end='')
            print('-'*side, end='')
            dot = dot - 2
        print()
        

if __name__ == "__main__":
    query = input('Enter number of query: ')
    for i in range(int(query)):
        # input example ( 7 21 )
        mn = list(map(int, input('Enter M(odd) and N(m*3): ').split()))
        m = mn[0]
        n = mn[1]
        makeDesign(m,n)