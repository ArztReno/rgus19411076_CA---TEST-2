'''
nci programme: BSHDS 
program: divisible by 7 and multiple of 5 from 1200 to 2900
author: Renato Gusani
studentID: x19411076
date: 04/03/2020

'''

nl=[]
for x in range(1200, 2900): # range from 1200 to 2900
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print (','.join(nl))