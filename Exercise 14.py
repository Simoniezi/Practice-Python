# Exercise 14
# List Remove Duplicates

import random

# I decided to make 2 random lists, because it was easier to remove duplicates, when you have to lists that have different integeres.
ranList1 = random.sample(range(1, 50), 10)
ranList2 = random.sample(range(1, 50), 10)
noDup = []

ranList1.sort()
ranList2.sort()

print('List number 1', ranList1)
print('List number 2', ranList2)


def removeDuplicates(ranList1):
    for num in ranList2:
        if num not in noDup:
            noDup.append(num)

    print('List with no duplicates', noDup)

removeDuplicates(ranList1)

#noDup = set(ranList1)
#noDup = list(ranList1)
#noDup = set(ranList2)
#noDup = list(ranList2)
#
#noDup.sort()
#print('List with no duplicates', noDup)

# Made by Simoniezii
# Discord: Simoniezi#7138