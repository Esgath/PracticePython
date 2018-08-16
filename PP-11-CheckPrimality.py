"""
Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no
divisors.). You can (and should!) use your answer to Exercise 4 to help you.
Take this oportunity to practice using functions, described below.
"""

def figure_prime():
    """Figures out if given number is prime or not"""
    count = 0
    num = int(input("What's the number?"))
    for i in range(1,num):
        if num % i == 0:
            count +=1
        else:
            count += 0
    if count == 1:
        print("The number is prime.")
    else:
        print("The number is not prime.")
figure_prime()
