import functions as fn

print (fn.addNumbers(12,5))


"""
First find the total marks by adding 5 subjects
find the average from the total 
calculate grade
"""
def findTotal(a,b,c,d,e):
    total = a+b+c+d+e
    return total
def findAverage(total):
    return total/5
def findGrade(avg):

    if avg < 50:
        return "fail"
    else :
        return "pass"

total = (findTotal(45,67,34,78,65))
average = findAverage(total)
grade = findGrade(average)

print("Total is " +str(total))
print("Average is " +str(average))
print("Grade is" +grade)