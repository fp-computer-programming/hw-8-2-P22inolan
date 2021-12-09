# Author: IBN (AMDG)

def letter_count(word, letter):
    total = 0
    for x in word:
        if letter == x:
            total += 1
    return total


print(letter_count("cat", "t") == 1)
print(letter_count("apple", "p") == 2)
print(letter_count("supercalifragilisticexpialidocious", "i") == 7)
