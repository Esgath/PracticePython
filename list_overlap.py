"""
Take two lists, say for example these two:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements
that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.
"""
# My solution:

def list_overlap(a,b):
    result = []
    if len(a) == 0 or len(b) == 0:
        return 0
    shorter = min(a,b)
    longer = max(a,b)

    if len(shorter) != 0 and len(longer) != 0:
        for i in range(len(shorter)):
            if shorter[i] in longer:
                if shorter[i] in result:
                    print(str(shorter[i]) + ' '+ 'is already in the list.')
                    decide = int(input('Nonetheless if u want to add it press 1.'))
                    if decide == 1:
                        result.append(shorter[i])
                        print(str(result) + '(Current state of list.)')
                    elif decide != 1:
                        print("Wrong number. Skipping the number.")
                        continue
                else:
                    result.append(shorter[i])

    print(str(result) + ("Final state of list."))
