import json
import calendar
import time



def name_someone():
    # READ FILE:
    with open('birthjson.json', 'r') as file:
        dict = json.load(file)

    print("Welcome to the birthday dictionary. We know the birthdays of:\n")
    for k in dict:
        print(k)
    name = input("Whose birthday you want to know?\n")
    print("{}'s birthday is {}".format(name, dict[name]))
    time.sleep(2)

def name_add():
    # READ FILE:
    with open('birthjson.json', 'r') as file:
        dict = json.load(file)

    name = input("What's the name?\n")
    birth_day = input("Birthday date: ")
    print("{}'s birthday is {}".format(name, birth_day))
    dict[name] = birth_day

    # SAVE FILE:
    with open('birthjson.json', 'w') as file:
        json.dump(dict, file)
    time.sleep(2)


def name_count():
    dict_new = {}
    with open('birthjson.json', 'r') as file:
        dict = json.load(file)
    # Create new dictionary
    for k in dict:
        date = dict[k]
        if date[3] == '0':
            month = int(date[4])
        elif date[3] != '0':
            month = int(date[3:5])
        month_name = calendar.month_name[month]
        dict_new[month_name] = 0
    # Add 1 to key's value
    for k in dict:
        date = dict[k]
        if date[3] == '0':
            month = int(date[4])
        elif date[3] != '0':
            month = int(date[3:5])
        month_name = calendar.month_name[month]
        dict_new[month_name] +=1
    print(dict_new)

def name_menu():
    validInput = True
    while validInput:
        print("------------")
        print("----Menu----")
        print("1.I want to know someones birthday.")
        print("2.I want to add someones birthday.")
        print("3.How many people have a birthday in each month.")
        print("------------")
        menu = input("------------\n")
        if menu == '1':
            name_someone()
        elif menu == '2':
            name_add()
        elif menu == '3':
            name_count()

name_menu()
