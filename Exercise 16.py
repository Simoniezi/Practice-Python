# Exercise 16
# Password Generator

import random

def pswGen():
    # Most characters to choose from, therefore the strongest.
    s = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()'

    # A little less characters, therefore the second strongest.
    a = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # The least characters to choose from, therefore the weakest.
    b = 'abcdefghijklmnopqrstuvwxyz0123456789'

    string = str(input('Do you want your password to be weak, medium or strong?: '))


# I chose to give each strength their own password length, to make their strength very clear.
    if string == 'weak':
        weakPassLen = 5

        weakP = ''.join(random.sample(b, weakPassLen))
        print(weakP)
        print(len(weakP))
    
    elif string == 'medium':
        mediumPassLen = 10

        mediumP = ''.join(random.sample(a, mediumPassLen))
        print(mediumP)
        print(len(mediumP))
    
    elif string == 'strong':
        strongPassLen = 20

        strongP = ''.join(random.sample(s, strongPassLen))
        print(strongP)
        print(len(strongP))
    
    else:
        # If anything goes wrong, say you accidentally hit enter without having completed the word
        # We just say that there was an error and then run the code again.
        print('Error!')
        pswGen()

pswGen()

# Made by Simoniezi
# Discord: Simoniezi#7138