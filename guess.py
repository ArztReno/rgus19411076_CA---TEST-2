'''
nci programme: BSHDS 
program: guess a number between 1 to 100
author: Renato Gusani
studentID: x19411076
date: 06/03/2020

'''

import random # pick a random number from below
the_number = random.randint(1, 100) # the number is between 1 and 100
while True:
    print('Guess a number between 1 and 100: ')
    user_guess = input()
    x = int(user_guess) # x is user's input (guess)
    if x == the_number: # correctly guessed
        print('you gussed the number!') # prints winning message
        break
    elif x < the_number: # if guess is smaller than the number
               print('the number is bigger than that') # prints hint
    elif x > the_number: # if guess is bigger than the number
               print('the number is smaller than that') # prints hint

print('if you gussed less than 5 times you won the game!')