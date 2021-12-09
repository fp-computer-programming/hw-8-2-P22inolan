# Author: IBN (AMDG)

def sum_no_odds(num):
    total = 0
    for x in num:
        if x % 2 == 0:
            total += x
        elif x % 2 != 0:
            return total
    return total



print(sum_no_odds([2, 4, 6, 8, 9]) == 20)
print(sum_no_odds([13, 12, 10]) == 0)
print(sum_no_odds([14, 16, 32]) == 62)