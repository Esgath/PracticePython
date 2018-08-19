"""
Write a function that takes an ordered list of numbers
(a list where the elements are in order from smallest to largest)
and another number. The function decides whether or not the given
number is inside the list and returns (then prints) an appropriate boolean.
Extras:
    Use binary search.
"""

def search(a,b):
    result = a
    if len(result) ==0:
        print("Empty list.")
    while len(result) > 0:
        if len(result) % 2 == 0:
            if result[int((len(result))/2)] == b:
                print("The number is in the list.")
                break
            elif result[int((len(result))/2)] > b:
                result = result[:int((len(result))/2)]
                print('searching...' + str(result))
            elif result[int((len(result))/2)] < b:
                result = result[int(((len(result))/2)+1):]
                print('searching...' + str(result))
            if len(result) == 0:
                print("The number isn't in the list")
        elif len(result) % 2 != 0:
            if result[int((len(result))/2)] == b:
                print("The number is in the list.")
                break
            elif result[int((len(result))/2)] > b:
                result = result[:int((len(result))/2)]
                print('searching...' + str(result))
            elif result[int((len(result))/2)] < b:
                result = result[(int((len(result))/2))+1:]
                print('searching...' + str(result))
            if len(result) == 0:
                print("The number isn't in the list")


def main_search():
    new_list = []
    print("Welcome. This programm can check if a given number "\
    "is in a given list of numbers.")
    a = input("What's the list?(format e.g.:22 33 44 55 642 2)\n")
    new_list = [int(s) for s in a.split(' ')]
    print(sorted(new_list))
    new_list = sorted(new_list)
    b = int(input("What's the number?\n"))
    search(new_list,b)


if "__main__" == __name__:
    main_search()
