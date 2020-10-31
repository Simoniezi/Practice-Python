# Exercise 4
# Divisors

userInput = int(input('Please choose a number to divide: '))

rangeList = range(1, userInput + 1)

numList = []

for number in rangeList:
    if userInput % number == 0:
        numList.append(number)

print(numList)

# Made by Simoniezi
# Discord: Simoniezi#7138