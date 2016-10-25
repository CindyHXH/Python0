"""
This is to check whether the input number is odd or even
And handle exceptions to the input is not integer

Coding by Xiaohui
"""

Check = None
while type(Check) !=  type(1):
    try:
       number = raw_input('input: ')
       Check =  int(number) % 2
       if Check == 1:
          print "Your number " + number + " is Odd number"
       else:
          print "Your number " + number + " is Even number"
    except:
       pass


