# Exercise 2
# Odd or Even

num = input('Enter a number: ')
num = int(num)
check = input('Give me a number to divide by: ')
check = int(check)

if num % 4 == 0:
    print(num, "is a multiple of 4")
elif num % 2 == 0:
    print(num, 'is an even number')
else:
    print(num, 'is an odd number')

if num % check == 0:
    print(num, 'divides evenly by', check)
else:
    print(num, 'does not divide evenly by', check)

# Made by Simoniezi
# Discord: Simoniezi#7138