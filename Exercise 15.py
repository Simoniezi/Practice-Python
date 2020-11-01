# Exercise 15
# Reverse Word Order

userInput = str(input('Write a short sentence: '))

def reverseWord():
    userText = userInput.split()
    print(' '.join(userText[::-1]))

reverseWord()

# Made by Simoniezi
# Discord: Simoniezi#7138