"""Task 1"""

print("Please type a string:")
string = input()
if string == "Yes" or string == "YES" or string == "yes" :
    print("yes")
else:
    print ("no")

"""Task 2"""
def myInput(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    elif c >= a and c >= b:
        return c

    else:
        return ("error")

print(myInput(50,50,48))

"""Task 3"""
def numList(list):
    firstLast =  [list[0], list[len(list)-1]]
    return firstLast

a = [2, 3, 4, 5, 6]
ret = numList(a)
print(ret)

"""Alternatively
def list_1(list):
    if len(list) == 1:
        return list
    else:
    new_list = []
    new_list.append(list[0])
    new_list.append(list[-1])
    return new_list
"""

"""Task 4"""
print ("Please enter a number:")
num = int(input())

if (num % 2)==0 and (num % 4) != 0:
    print ("Number is even and not a multiple of 4\n")
elif (num % 4)==0 and (num % 2) == 0:
    print ("Number is even and  a multiple of 4\n")
else:
    print ("number is odd \n" )

"""Task 5"""
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tup1 = tup[0:5]
tup2 = tup[5:10]
print (tup1)
print (tup2)



