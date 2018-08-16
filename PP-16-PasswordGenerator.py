"""
Write a password generator in Python. Be creative with how you generate
passwords - strong passwords have a mix of lowercase letters, uppercase letters,
numbers, and symbols. The passwords should be random, generating a new password
every time the user asks for a new password. Include your run-time code in a
main method.
Extra:
Ask the user how strong they want their password to be. For weak passwords,
pick a word or two from a list.
"""
import string
import random


def weak():
    result = []
    list_weak = ['1234', 'password', 'strong', 'weak']
    for i in range(random.randint(1,2)):
        result += list_weak[random.randint(0,3)]
    return ''.join(result)

def strong():
    result = []
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=',
    '+']
    alpha = list(string.ascii_letters)
    numbers = string.digits
    leng = random.randint(2,3)
    for i in range(leng):
        randomise = random.randint(2,3)
        if randomise ==2:
            result += random.choice(symbols)
            result += random.choice(numbers)
            result += random.choice(symbols)
            result += random.choice(alpha)
            result += random.choice(numbers)
            result += random.choice(alpha)
        elif randomise ==3:
            result += random.choice(symbols)
            result += random.choice(numbers)
            result += random.choice(symbols)
            result += random.choice(numbers)
            result += random.choice(alpha)
            result += random.choice(symbols)
            result += random.choice(alpha)
            result += random.choice(numbers)
            result += random.choice(alpha)
    return ''.join(result)


def password_generator():
    user = int(input(
        "---------------\n" +
        "Main Menu:\n" +
        "1.Generate strong password\n" +
        "2.Generate weak password\n" +
        "---------------\n"))
    if user == 1:
        print(strong())
    elif user == 2:
        print(weak())


password_generator()
