# Exercise 9
# Guessing Game One

import random

randomNum = random.randint(1, 9)
numOfGuess = 1

while True:
    print('Type exit to stop!')
    userInput = int(input('Choose a number between 1 and 9; they can be used too: '))

    if userInput == 'exit':
        break
    else:
        pass
    
    if randomNum == userInput:
        print('''
        
        You guessed it right in ''', + numOfGuess)
        break
    elif randomNum > userInput:
        print('''
        Too low!''')
        numOfGuess += 1
    elif randomNum < userInput:
        print('''
        Too big!''')
        numOfGuess += 1
    else:
        print('''
        
        Unknown.''')

# Made by Simoniezi
# Discord: Simoniezi#7138