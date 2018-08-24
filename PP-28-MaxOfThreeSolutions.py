"""
Implement a function that takes as input three variables, and returns the
largest of the three. Do this without using the Python max() function!

The goal of this exercise is to think about some internals that Python normally
takes care of for us. All you need is some variables and if statements!
"""
def find():
    result = 0
    n1 = int(input("Number one: "))
    n2 = int(input("Number two: "))
    n3 = int(input("Number three: "))
    if n3>=n2:
        result = n3
        if n1>=n3:
            result = n1
    elif n2>=n3:
        result = n2
        if n1>=n2:
            result = n1

    print(result)
find()
