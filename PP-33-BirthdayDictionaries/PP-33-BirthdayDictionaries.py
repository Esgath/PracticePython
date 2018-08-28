"""
For this exercise, we will keep track of when our friend’s birthdays are,
and be able to find that information based on their name. Create a dictionary
(in your file) of names and birthdays. When you run your program it should ask
the user to enter a name, and return the birthday of that person back to them.
The interaction should look something like this:

>>> Welcome to the birthday dictionary. We know the birthdays of:
Albert Einstein
Benjamin Franklin
Ada Lovelace
>>> Who's birthday do you want to look up?
Benjamin Franklin
>>> Benjamin Franklin's birthday is 01/17/1706.
"""
def name_date():
    dict = {}
    dict_new = {}
    with open('birthday.txt', 'r') as file:
        for i in file:
            name = i.strip('\n').split(" ")
            dict[' '.join(name[0:2])] = name[2]

    print("Welcome to the birthday dictionary. We know the birthdays of:\n")
    for k in dict:
        print(k)
    user = input("Whose birthday do you want to know?\n")
    print("{}'s birthday is {}.".format(user, dict[user]))

name_date()
