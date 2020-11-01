# Exercise 13
# Fibonacci

def userInput(strText = 'How many Fibonacci numbers should I generate?: '):
    return int(input(strText))

num = userInput()

def nextFibonacci(a = 1, b = 1):
    c = a + b
    return (b, c)

a = 1
b = 1

for number in range(num):
    print(a)
    (a, b) = nextFibonacci(a, b)

# Made by Simoniezi
# Discord: Simoniezi#7138