# This program says hello and ask for my name

print('Hello World!')
print('What is your name?') # ask for your name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is: ')
print(len(myName))
print('What is your age') # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')

# Test Code
print('Enter your password:')
password = input()
if password == 'George Khem':
    print('That is correct!')
else:
    print('Try again sucka!')

# While Example
spam = 0
while spam < 5:
    print('Geter')
    spam = spam + 1

spam = 0
while spam < 5:
    print('Geter')
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is ' + str(spam))

# For Loop
print('My name is')
for i in range(3):
    print('Geter' + str(i))

total = 0
for num in range(100):
    total = total + num
    print(total)

#built in functions

import random, sys, os, math
from random import *
import sys
sys.exit()

#Writing Your own functions

    
