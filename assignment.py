taskList = [23, "Jane", ["Lesson 23", 560, {"currency":"KES"}], 29870, (76, "John")]

print(type(taskList))

"""Print KES"""
print(taskList[2][2]["currency"])

"""Print 560"""
print(taskList[2][1])
"""Use a function to determine length of taskList"""
print(len(taskList))

"""change 987 to 789 using an inbuilt function
taskList.pop(3)
taskList.insert(3,789)
print(taskList)"""

print(int(str(taskList[3])[::-4]))


"""Change the name John to Jane
taskList[4][1].replace("John", "Jane")
print(taskList)"""
