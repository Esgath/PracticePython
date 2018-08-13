# Solution:
def divisor():
    """
    Asks the user for a number and then prints
    out a list of all the divisors of that number.
    """
    result = []
    number = int(input("What is the number?"))
    x = range(1,number+1)
    for i in x:
        if number % i == 0:
            result.append(i)
    print(result)

divisor()
