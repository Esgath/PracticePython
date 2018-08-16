"""
Write a program (function!) that takes a list and returns a new list that
contains all the elements of the first list minus all the duplicates.
Extras:
Write two different functions to do this - one using a loop and constructing
a list, and another using sets.Go back and do Exercise 5 using sets, and write
the solution for that in a different function.
"""
# My solution:

def list_overlap(a,b):
    result = []
    a = set(a)
    b = set(b)
    if len(a) == 0 or len(b) == 0:
        print(result)
    elif len(a) != 0 and len(b) != 0:
        result = [i for i in a if i in b]
    print(result)

list_overlap([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
