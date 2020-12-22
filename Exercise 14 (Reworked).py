import random

list1 = random.sample(range(1, 100), 25)
list1.sort()

list2 = random.sample(range(1, 100), 25)
list2.sort()

sortedList = []

print('Random list 1:\n', list1)
print('Random list 2:\n', list2)

def noDup():
    for num in list2:
        if num not in sortedList:
            if num in list1:
                continue
            else:
                sortedList.append(num)

    for num in list1:
        if num not in sortedList:
            if num in list2:
                continue
            else:
                if num in sortedList:
                    continue
                else:
                    sortedList.append(num)

    sortedList.sort()
    print('List with no duplicates:\n', sortedList)

noDup()

