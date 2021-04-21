'''
nci programme: BSHDS 
program: bmi calculator with features as shown in assignment question table
author: Renato Gusani
studentID: x19411076
date: 29/02/2020

'''
height = float(input("Input height in meters (Example; 1.70): ")) # gets height and assigns it to user input
weight = float(input("Input weight in kg: (Example; 75) ")) # gets weight and assigns it to user input

# this calculates the bmi (as given from the question)
bmi = weight/(height**2) 

print("Your BMI is: {0} and you are: ".format(bmi), end='') # prints bmi according to format

#features of BMI as per the assignment table
if ( bmi < 15):
   print(" Very severely underweight")

elif ( bmi >= 15 and bmi < 16):
   print("Severely underweight")

elif ( bmi >= 16 and bmi < 18.5):
   print("Underweight")

elif ( bmi >= 18.5 and bmi < 25):
   print("Normal(healthy weight)")

elif ( bmi >= 25 and bmi < 30):
   print("Overweight")

elif ( bmi >= 30 and bmi < 35):
   print("Obese class I(Moderately obese)")

elif ( bmi >= 35 and bmi < 40):
   print("Obese class II(Severely obese)")

elif ( bmi >= 40 and bmi < 45):
   print("Obese class III(Very severely obese)")

elif ( bmi >= 45 and bmi < 50):
   print("Obese class IV(Morbidly obese)")

elif ( bmi >= 50 and bmi < 60):
   print("Obese class V(Super obese)")

elif ( bmi >=60):
   print("Obese class VI(Hyper obese)")



