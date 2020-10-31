# Exercise 6
# String Lists

# Defining isPalindrome to check if the entered word is 
def isPalindrome(a):
    return a == a[::-1] # [::-1] makes it read the the word backwards

a = str(input('Enter a word: ')).casefold() # .casefold() to make it not matter if it is lower- or uppercase.
word = isPalindrome(a)

if word:
    print('The word you entered is a palindrome.')
else:
    print('The word you entered is not a palindrome.')

# Made by Simoniezi
# Discord: Simoniezi#7138