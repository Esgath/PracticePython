"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays
(using input), compare them, print out a message of congratulations to the
winner, and ask if the players want to start a new game)
Remember the rules:
    Rock beats scissors
    Scissors beats paper
    Paper beats rock
"""

import time

def main():
    validInput = True
    while validInput:
        try:
            print("---------" + "\n\nWelcome in rock paper scissors game." +
            "\n\n---------")
            print("\nMenu:" + "\n1.Play game.(2 players)" + "\n2.Exit")
            decide_menu = int(input("What's your decision?"))
            if decide_menu == 1:
                print("PLAY GAME")
                first = int(input("\n(First player) 1.Rock 2.Paper" \
                    " 3.Scissors\n"))
                second = int(input("\n(Second player) 1.Rock 2.Paper" \
                    " 3.Scissors\n"))
                print("wait...")
                time.sleep(1)
                rock_paper_scissors(first,second)
                again = input("Do you want to play again?(no/yes)\n").lower()
                if again == 'yes':
                    continue
                elif again == 'no':
                    break
                else:
                    print("Invalid Input")
                    break
            elif decide_menu == 2:
                print("EXIT")
                break
        except:
            print("Something is off...")

def rock_paper_scissors(first, second):
    if first == 1:
        if second == 1:
            print("It's a draw.")
        elif second == 2:
            print("Player number 2 wins.")
        elif second == 3:
            print("Player number 1 wins.")
    elif first == 2:
        if second == 2:
            print("It's a draw.")
        elif second == 3:
            print("Player number 2 wins.")
        elif second == 1:
            print("Player number 1 wins.")
    elif first == 3:
        if second == 3:
            print("It's a draw.")
        elif second == 1:
            print("Player number 2 wins.")
        elif second == 2:
            print("Player number 1 wins.")

main()
