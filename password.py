'''
nci programme: BSHDS 
program: password with features
author: Renato Gusani
studentID: x19411076
date: 28/02/2020

'''
import re # Regular Expression Syntax specifies a set of strings that matches it, must import to use re.search commands.

while True:
  
  user_input = input("Input a new password : ") # prompts user for password
  is_valid = False 
  if (len(user_input)<6 or len(user_input)>16): # if password is smaller than 6 or bigger than 16 
    
    print("Password is too weak, Password must be 6 and 16 characters long") # displays error with password length not being between 6-16 characters long
    continue
  elif not re.search("[A-Z]",user_input): # search characters uppercase A to Z in password
    
    print("Password is too weak, password must have at least 1 uppercase character between A to Z") # displays error with password length
    continue
  elif not re.search("[a-z]",user_input): # search characters lowercase a to z in password
    
    print("Password is too weak, password must have at least 1 lowercase character a to z") # displays error with missing lowercase characters in password 
    continue
  elif not re.search("[1-9]",user_input): # search numbers 1 to 9 in password
    
    print("Password is too weak, password msut contain one number between 1 to 9") # displays error with missing numbers 1 to 9 in password 
    continue
  elif not re.search("[~!@#$%^&*]",user_input): # search characters ~!@#$%^&* in password
    
    print("Password is too weak, password msut contain one character from [~!@#$%^&*]") # displays error with password characters such as missing ~!@#$%^&*
    continue
  elif re.search("[\s]",user_input):
    
    print("Password is too weak, password must NOT contain any space")
    continue
  else:
  
    is_valid = True
    break

if(is_valid): # if all searches come back valid 
  print("Password is strong enough! Password set.") # prints success message
 