# Exercise 11
# Check Primality Functions

def userInput(strText='Please enter a number: '):
    return int(input(strText))


num = userInput()

if num == 1:
    print('The number you have entered is not a prime number!')
elif num == 2:
    print('The number you have entered is a prime number!')
else:
    for number in range(2, num):
        if num % number == 0:
            print('The number you entered is not a prime!')
            break
        else:
            print('The number you entered is a prime!')
            break

# Made by Simoniezi
# Discord: Simoniezi#7138