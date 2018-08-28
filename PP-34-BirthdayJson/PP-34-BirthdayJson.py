import json


def name_date():
    validInput = True
    while validInput:
        with open('birthjson.json', 'r') as file:
            dict = json.load(file)
        print("Welcome to the birthday dictionary. We know the birthdays of:\n")
        for k in dict:
            print(k)

        user = input("Whose birthday do you want to know?\n")
        print("{}'s birthday is {}.".format(user, dict[user]))

        # ADD SOMETHING TO DICT:
        user_add = input("Do you want to add someones birthday date?(Y/N)\n").upper()

        if user_add == 'Y':
            name = input("What's the name?\n")
            birth_day = input("Birthday date: ")
            dict[name] = birth_day
            with open('birthjson.json', 'w') as file:
                json.dump(dict, file)
        elif user_add == 'N':
            break


name_date()
