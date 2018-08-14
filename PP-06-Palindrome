"""
Ask the user for a string and print out whether this string is a palindrome or
not. (A palindrome is a string that reads the same forwards and backwards.)
"""
# My solution:


def palindrome(word):
    result = ''
    word = word.lower()
    if type(word) == str:
        for i in word:
            if i == word[len(word) - (word.index(i)+1)]:
                result += i
        if result == word and word != '':
            print("It's a palindrome.")
        elif result != word:
            print("It's not a palindrome.")
        elif word == '':
            print("You need to input a word.")
    else:
        print("It must be a string.")


palindrome("Delled")        # It's a palindrome.
palindrome("sasalulek")     # It's not a palindrome.
palindrome("")              # You need to input a word.
