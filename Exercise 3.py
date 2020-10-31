# Exercise 3
# List less than ten

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newList = []

# If more than one line
#for element in a:
#    if element < 5:
#        newList.append(element)

# Single line, I believe
[newList.append(element) for element in a if element < 5]
print('\nThis is all the numbers below 5: ', newList)

userList = []
userInput = int(input('\nPlease enter a number and I\'ll show you a new list!: '))

# If more than one line
#for elements in a:
#    if elements < userInput:
#        userList.append(elements)

# Single line, I believe
[userList.append(element) for element in a if element < userInput]
print('\nThe userlist is: ', userList)


# Made by Simoniezi
# Discord: Simoniezi#7138