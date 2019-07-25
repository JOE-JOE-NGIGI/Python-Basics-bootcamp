"""
For Loop repeats a task until the max is reached.
While Loop executes a statement/code/task until a condition is false
"""

"""Create a list that has numbers 1-100"""
valList = []
for val in range(0,10):
    valList.append(val)

print(valList)

"""use a for loop to get inside a list"""
newList = ["John","James","Mary"]
for myval in newList:
    print(myval)
print(myval)

"""Create a list of only even numbers"""
valList2 = []
for val in range(0,10):
    if val%2 == 0:
        valList2.append(val)

print(valList2)

"""Create a list of odd numbers"""
valList3 = []
for val in range(0,10):
    if val%2 != 0:
        valList3.append(val)

print(valList3)



"""While loop"""
i = 0
lst1 = []
while i<=10:
    lst1.append(i)

    i += 1
print(lst1)

"""Access a list using while loop"""
count = 0
newList = ["John","James","Mary"]
while count < len(newList):
    print(newList[count])
    count += 1



