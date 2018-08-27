"""
This exercise is Part 2 of 3 of the Hangman exercise series. The other exercises
 are: Part 1 and Part 3.

Let’s continue building Hangman. In the game of Hangman, a clue word is given
by the program that the player has to guess, letter by letter. The player
guesses one letter at a time until the entire word has been guessed.
(In the actual game, the player can only guess 6 letters incorrectly before
losing).

Let’s say the word the player has to guess is “EVAPORATE”. For this exercise,
write the logic that asks a player to guess a letter and displays letters in
he clue word that were guessed correctly. For now, let the player guess an
infinite number of times until they get the entire word. As a bonus, keep
track of the letters the player guessed and display a different message if
the player tries to guess that letter again. Remember to stop the game when
all the letters have been guessed correctly! Don’t worry about choosing a
word randomly or keeping track of the number of guesses the player has
remaining - we will deal with those in a future exercise.

An example interaction can look like this:

>>> Welcome to Hangman!
_ _ _ _ _ _ _ _ _
>>> Guess your letter: S
Incorrect!
>>> Guess your letter: E
E _ _ _ _ _ _ _ E
...
"""


import random


def pick_word():
    list = []
    with open('dictionary.txt', 'r') as dictionary:
        for i in dictionary:
            single = i.strip()
            list.append(single)
        return random.choice(list)


def user_guess():
    word = pick_word()

    # Turns word into list:
    word_list = list(word)
    print(word_list)
    check = []
    check_store = []
    check_wrong = []
    print(' _'* len(word_list))

    while len(check_store) != len(word_list):
        user = input("\nGuess a letter: ").upper()

        # Add good guesses to a list and check_store if they dont repeat
        if user in check_store:
            print("This letter is already guessed.\n")

            # SHOW PROGRESS:
            for i in word_list:
                if i in check_store:
                    print(' '+i,end='')
                elif i not in check_store:
                    print(" _",end='')

        elif user not in check_store:
            if user in word_list:
                check =[user for i in range(word_list.count(user))]
                # Had to extend this one because check
                # doesn't store the value in next cicle.
                check_store.extend(check)
                print("Good job.\n")

                # SHOW PROGRESS:
                for i in word_list:
                    if i in check_store:
                        print(' '+i,end='')
                    elif i not in check_store:
                        print(" _",end='')

            # Takes wrong and put them to list
            # If not in list prints wrong guess
            else:
                if user not in check_wrong:
                    check_wrong.append(user)
                    print("Wrong guess.\n")

                    # SHOW PROGRESS:
                    for i in word_list:
                        if i in check_store:
                            print(' '+i,end='')
                        elif i not in check_store:
                            print(" _",end='')

                elif user in check_wrong:
                    print("You have already tried this letter.\n")

                    # SHOW PROGRESS:
                    for i in word_list:
                        if i in check_store:
                            print(' '+i,end='')
                        elif i not in check_store:
                            print(" _",end='')


user_guess()
