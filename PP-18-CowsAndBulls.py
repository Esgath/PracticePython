"""
Create a program that will play the “cows and bulls” game with the user.
The game works like this:
Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
For every digit that the user guessed correctly in the correct place, they have
a “cow”. For every digit the user guessed correctly in the wrong place is a
“bull.” Every time the user makes a guess, tell them how many “cows” and “bulls”
 they have. Once the user guesses the correct number, the game is over.
 Keep track of the number of guesses the user makes throughout teh game and
 tell the user at the end.
"""
import random

def cow_bulls():
    print("Welcome to the Cows and Bulls Game!")
    random_number = random.randint(1000,9999)
    number_user = int(input("Please guess the number(4 digits):\n"))
    cow = 0
    bull = 0
    if number_user > 999 and number_user <=9999:
        random_number = str(random_number)
        number_user = str(number_user)
        for i in range(4):
            if number_user[i] == random_number[i]:
                cow += 1
            else:
                bull += 1
        print("The number is: " + str(random_number) + '\n' +
            "Your number is: " + str(number_user) + '\n' +
            "Cows: " + str(cow) + '\n' +
            "Bulls " + str(bull))

    elif number_user <= 999 or number_user > 9999:
        print("Wrong number(must be 4 digits)")

cow_bulls()
