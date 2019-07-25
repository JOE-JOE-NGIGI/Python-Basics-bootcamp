firstname = "Joe"
secondname = "Ngingi"

print(firstname + " " + secondname)
print(firstname,secondname)

"""operations on strings"""
"""Case manipulation"""

print (firstname.upper())
print (firstname.lower())
print(firstname.title())

"""Count number of times a character appears"""
print(secondname.lower())
print(secondname.count("n"))

"""print nummber of characters in a string"""
print(firstname.__len__())

"""split a string"""
print(secondname.split("n"))

print(type("John Doe".split(" ")))

"""printing indices"""
print(secondname[-6])

"""splitting indices"""
print(secondname[0:3])
print(secondname[3:])
print(secondname[-4:])


#strings- alphanumeric and special characters
#integers-
#modulus

rem =366%2

fl1=3.45
print(type(fl1))

#Boolean
bo = True
print(type(bo))

#String to int conversion
print(type(str(rem)))

decl=3.75454545454545
print(int(decl))
print(decl)

bo = 4>7
print(type(bo))

dec2 = round(decl,2)
print(dec2)