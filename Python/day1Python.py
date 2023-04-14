# This is my First Python File
# Author: Brandon Vanek
# Date: 4/13/2023

# print("Beware of Crocs and small dogs!!!") # \n new line
# print("Hello World!")
# print(" ")
# print("Beware of Crocs and small dogs!!!")
# print("Hello World!")
# print(" ")
# print("Beware of Crocs and small dogs!!!")
# print("Hello World!")

# key  value
# AZ = "us-east-1a"

# print(AZ + " and us-east-1b")

# num = 7.012123123123123131231233

# print(num + 7.1121241414124124)

# Data Types
# Strings
# int
# double
# float
# boolean

# Conditionals

# print(AZ == "us-east-1a")
# print(10 == 10)
# print(10 == 9)
# print(" ")
# print("10" != 10)

# == equating values
# differing types affect whether two items are the same
# not just their values

# Operators
# == - comparing values for equivalency
# != - comparing values for non-equivalency
# <
# >
# <=
# >=

# Math
# + - adding values together
# - - subtracting values
# * - multiplying values
# / - dividing values
# % - modulus - gives remainder after dividing two numbers

# print(10 % 3)

# CONJUCTIONS
# and - returns true if BOTH statements are true
# or - returns true if at least one of the statements are true
# not - reverses the value of a boolean expression not(10 == 10)
# print(10 == 10 and "us-east-1a" == "us-east-1a")
# print(10 == "1" or "10" == 10)

# Conditional Statements
# if - decision

# stateOfBeing = "tired"
# dayOfWeek = "monday"

# # if (stateOfBeing == "tired and worn out" and (dayOfWeek == "Thursday" or dayOfWeek == "Friday")):
# #     print("drink coffee")
# # elif (stateOfBeing == "tired"):
# #     print("Must suck to be so tired hahahaha")
# # elif (dayOfWeek == "Monday"):
# #     print("Monday's amiright?")
# # else:
# #     print("have some tea instead")

# if (stateOfBeing == "tired"):
#     print("I am tired")

# if (dayOfWeek.upper() == "Monday".upper()):
#     print("It's a Monday")

# print("Have a nice day!")

# # loop -------
# #  for
# # while



# best for when you know the exact number of times you want to loop
# for character in range(0, monthOfYear):
#     print(x)
# print("done with loop")


#infinite loop
# while numberOfDay < 10:
#     print("looping")

# nameOfDay = "Tuesday"

# i = 0
# print(nameOfDay)
# while nameOfDay != "Tuesday":
#     if (nameOfDay == "T"):
#         nameOfDay += "u"
#         print(nameOfDay)
#     elif (nameOfDay == "Tu"):
#         nameOfDay += "e"
#         print(nameOfDay)
#     elif (nameOfDay == "Tue"):
#         nameOfDay += "s"
#         print(nameOfDay)
#     elif (nameOfDay == "Tues"):
#         nameOfDay += "d"
#         print(nameOfDay)
#     elif (nameOfDay == "Tuesd"):
#         nameOfDay += "a"
#         print(nameOfDay)
#     elif (nameOfDay == "Tuesda"):
#         nameOfDay += "y"
#         print(nameOfDay)
#     else:
#         nameOfDay = "Tuesday"
#         print(nameOfDay)
#         # numberOfDay += 1
#     i += 1
#     print(1)

# print("finished")

#              0, 1 ,2, 3, 4, 5
myFirstList = [1, 2, 3, 4, 5, 6]

# print(len(myFirstList))

# for i in range(len(myFirstList)):
#     print(i)
# print(myFirstList[1])

myFirstList.append("string")

# [1, 2, 3, 4, 5, 6, "string"]
for i in myFirstList:
    print(str(i).upper())

print(myFirstList[0:6])

# tuple - immutable list (cannot be changed)

myFirstTuple = (1, 2, 3, 4, 5, 6)

myFirstList[0] += 1 #you are able to change list data
# myFirstList[0] = 0
print(myFirstList)

tupleMyFirstList = tuple(myFirstList)
print(tupleMyFirstList)
tupleMyFirstList[0] = 0


