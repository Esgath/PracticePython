# Description(http://codingbat.com/prob/p190859):
"""
We want make a package of goal kilos of chocolate.
We have small bars (1 kilo each) and big bars (5 kilos each).
Return the number of small bars to use, assuming we always use big
bars before small bars. Return -1 if it can't be done.
"""
# My solution
def make_chocolate(small, big, goal):
    count = 0
    if (big * 5) >= goal and goal % 5 == 0:
        return 0
    elif int(goal / 5) <= big:
        count += big*5
        if goal % 5 <= small:
            return goal % 5
        else:
            return -1
    elif int(goal / 5) > big:
        count += big*5
        if small >= goal - count:
            return goal - count
        else:
            return -1
