"""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.

Coding by Xiaohui
"""

import datetime

now = datetime.datetime.now()
year = now.year
print "Please enter your name and age"
name = raw_input("Name: ")
Answer = None
while Answer is None:
    try:
        age = raw_input("Age: ")
        Answer = 100 - int(age) + year
    except:
        pass

print ("You will be 100 years old in ", Answer)
