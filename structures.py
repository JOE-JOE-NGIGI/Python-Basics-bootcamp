"""Variables that hold multiple variables"""
#List,tuple,Dictionary
person = ["John","Doe",30,65.54,"Mombasa",True]
#print(person[0])
#print(person[4])
#print(person[3])
print(person[0:5])
print(person[-4:-2])

"""Tuple has smaller memory than list"""
person_t = ("John","Doe",30,65.54,"Mombasa",True)
print(person_t[0:5])

"""Prints from index 0 in intervals of the second int. If the second int is negative,it will reverse"""
taskList = [0,1,2,3,4,5,6,7,8,9,10]
print(taskList[0::3])

"""List operations"""
person.reverse()
print(person)

print(len(person))
person.append("Joe")
print(person)

person.remove("Joe")
print(person)

#person.pop(3)"""To remove an index from a tuple"""
print(person)

"""Dictionary - Structure which holds variables in key:value  pairs"""
person_dict={"firsName" : "John","SurName" : "Doe","Weight" : 65.54, "Location": "Mombasa","ActiveUser":True}
print(person_dict["SurName"],person_dict["Location"])