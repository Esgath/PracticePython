"""
Write a program (using functions!) that asks the user for a long string
containing multiple words. Print back to the user the same string, except with
the words in backwards order. For example, say I type the string:

  My name is Michele

Then I would see the string:

  Michele is name My

shown back to me.
"""
def backward_order():
    user = str(input("Please input string, it can contain multiple words.\n"))
    user_list = user.split(" ")
    backward_list = user_list[::-1]
    result = " ".join(backward_list)
    print("Given string but in backwards order: \n" + result)

backward_order()
