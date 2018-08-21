"""
Given two .txt files that have lists of numbers in them, find the numbers that
are overlapping. One .txt file has a list of all prime numbers under 1000, and
the other .txt file has a list of happy numbers up to 1000.
"""
def overlap_file():
    list_prime = []
    list_happy = []
    overlap = []
    with open('prime.txt', 'r') as prime:
        line_prime = prime.readline()
        while line_prime:
            line_prime = line_prime.strip()
            list_prime.append(line_prime)
            line_prime = prime.readline()
        print("Prime numbers: " + str(list_prime) + '\n')

    with open('happy.txt', 'r') as happy:
        line_happy = happy.readline()
        while line_happy:
            line_happy = line_happy.strip()
            list_happy.append(line_happy)
            line_happy = happy.readline()
        print("Happy numbers: " + str(list_happy) + '\n')

    for i in list_happy:
        if i in list_prime:
            overlap.append(i)
    print("Ones that overlap: " + str(overlap))

overlap_file()
