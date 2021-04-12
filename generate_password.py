###importing the random module 
###importing the module time

import random
import time

#using text1 as the variable to store lowercase letter
text1 = 'abcdefghijklmnopqrstuvwxyz'

#using text2 as the variable to store uppercase letter
text2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#using num as the variable to store number from 0-9
num = '0123456789'

#using special as the variable to store special symbols
special = '#$%'

#print ('please enter (YES) for strong password and (NO) for weak password')

#using user_input to collect response from the user
print ('           ')
#user_input = input('Do you want a strong or a weak password?: ')

# changing user response to uppercase 
#user_input = user_input.upper()

class GeneratePassword:
    """Password generator"""
    # def __init__(self, Strength_of_password):
    #    self.Strength_of_password = Strength_of_password.lower()

    def Strong_password():
        a = ''.join(random.sample(text1,4)) #making use of join to remove commas(,) between the password
        b = ''.join(random.sample(text2,2))
        c = ''.join(random.sample(num,3))
        d = ''.join(random.sample(special,2))
        print ('            ')
        print ('please wait while your password is being generated')
        time.sleep(2.0)
        password = a+b+c+d
        print ('Your password is',password)

    def Weak_password():
        a = ''.join(random.sample(text1,4))
        b = ''.join(random.sample(text2,3))
        print ('            ')
        print ('please wait while your password is being generated')
        time.sleep(1.5)
        password = a+b
        print ('Your password is',password)

GeneratePassword.__init__()





