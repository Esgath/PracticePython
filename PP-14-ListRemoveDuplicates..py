"""
Write a program (function!) that takes a list and returns a new list that
contains all the elements of the first list minus all the duplicates.
Extras:
Write two different functions to do this - one using a loop and constructing
a list, and another using sets.Go back and do Exercise 5 using sets, and write
the solution for that in a different function.

"""
def del_duplicate(a):
    a = set(a)
    return a

def set_list(a):
    new_set = del_duplicate(a)
    print(new_set)
    result = []
    result = [i for i in new_set if i not in result] 
    print(result)

set_list([2, 4, 5, 5, 5, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 9])
