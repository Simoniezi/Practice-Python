# Exercise 10
# List Overlap Comprehensions

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for number in a and b:
    if number in a and b:
        c.append(number)

print(c)

num1 = random.sample(range(100), 5)
num2 = random.sample(range(100), 5)

num1.sort()
num2.sort()

print(num1,'\n',num2)

# Made by Simoniezi
# Discord: Simoniezi#7138