"""
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too
low, too high, or exactly right. (Hint: remember to use the user input lessons
from the very first exercise)

Extras:
Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends,
print this out.

"""
import random
def guess():
    count_correct = 0
    count_incorrect = 0
    validInput = True
    while validInput:
        try:
            user = input("Guess the number between 1 and 9.\
                (type 'exit' if u want to exit)\n")
            random_num = random.randint(1,9)
            if user == 'exit':
                print("\nEXIT\n")
                break
            elif int(user) == random_num:
                print("|You guessed right.|\n")
                count_correct += 1
            elif int(user) <0 or int(user) >9:
                print("|Your guess should be between 1 and 9.|\n")
            elif int(user) != random_num:
                print("|Your guess was wrong.|\n")
                count_incorrect +=1
        except ValueError:
            print("|ValueError|Try again.(You have to input a number.|)\n")
            continue

    print("Correct: " + str(count_correct))
    print("Incorrect: " + str(count_incorrect))
guess()
