"""
In this exercise, we will finish building Hangman. In the game of Hangman,
the player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms) before
they lose the game.

In Part 1, we loaded a random word list and picked a word from it. In Part 2,
we wrote the logic for guessing the letter and displaying that information to
the user. In this exercise, we have to put it all together and add logic for
handling guesses.

Copy your code from Parts 1 and 2 into a new file as a starting point.
Now add the following features:

    Only let the user guess 6 times, and tell the user how many guesses they
    have left.Keep track of the letters the user guessed. If the user guesses
    a letter they already guessed, don’t penalize them - let them guess again.

Optional additions:

    When the player wins or loses, let them start a new game.
    Rather than telling the user "You have 4 incorrect guesses left", display
    some picture art for the Hangman. This is challenging - do the other parts
    of the exercise first!

Your solution will be a lot cleaner if you make use of functions to help you!
"""
import random


def pick_word():
    list = []
    with open('dictionary.txt', 'r') as dictionary:
        for i in dictionary:
            single = i.strip()
            list.append(single)
        return random.choice(list)


def hang_man(failed):
    if failed == 0:
        print(" _________     \n")
        print("|         |    \n")
        print("|             \n")
        print("|          \n")
        print("|          \n")
        print("|              \n")
        print("|              \n")
    elif failed == 1:
        print(" _________     \n")
        print("|         |    \n")
        print("|         0    \n")
        print("|          \n")
        print("|          \n")
        print("|              \n")
        print("|              \n")
    elif failed == 2:
        print(" _________     \n")
        print("|         |    \n")
        print("|         0    \n")
        print("|         |  \n")
        print("|          \n")
        print("|              \n")
        print("|              \n")
    elif failed == 3:
        print(" _________     \n")
        print("|         |    \n")
        print("|         0    \n")
        print("|        /|  \n")
        print("|           \n")
        print("|              \n")
        print("|              \n")
    elif failed == 4:
        print(" _________     \n")
        print("|         |    \n")
        print("|         0    \n")
        print("|        /|\  \n")
        print("|          \n")
        print("|              \n")
        print("|              \n")
    elif failed == 5:
        print(" _________     \n")
        print("|         |    \n")
        print("|         0    \n")
        print("|        /|\  \n")
        print("|        /   \n")
        print("|              \n")
        print("|              \n")
    elif failed == 6:
        print(" _________     \n")
        print("|         |    \n")
        print("|         0    \n")
        print("|        /|\  \n")
        print("|        / \  \n")
        print("|              \n")
        print("|              \n")


def user_guess():
    word = pick_word()

    # Turns word into list:
    word_list = list(word)
    failed = 0
    check = []
    check_store = []
    check_wrong = []
    print(' _'* len(word_list))

    while len(check_store) != len(word_list):

        print("\nYou have " + str(6-failed) +' chances left')
        hang_man(failed)
        if failed == 6:
            break

        user = input("\n<Guess a letter>: ").upper()

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
                    failed += 1

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
    end = input("Do you want to play again ? Y/N\n").upper()
    if end == 'Y':
        user_guess()
    elif end == 'N':
        return word


user_guess()
