'''
nci programme: BSHDS 
program: prints triangle with user input
author: Renato Gusani
studentID: x19411076
date: 29/02/2020

'''
height = int(input("how tall would you like the triangle to be? : "))
for i in range(height,0,-1):
    print(i* ' ' + (height+1-i) * '*') # prints * as a left angle triangle