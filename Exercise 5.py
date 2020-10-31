# Exercise 5
# List Overlap

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for number in a and b:
    if number in a and b:
        c.append(number)

print(c)

# Extra 1

num1 = random.sample(range(1, 50), 10)
num2 = random.sample(range(1, 50), 10)

# Just sorting the numbers in num1 and num2 so they don't just scramble around
num1.sort()
num2.sort()

print(num1)
print(num2)


# Made by Simoniezi
# Discord: Simoniezi#7138