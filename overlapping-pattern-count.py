# Every letter in a word if represented by 0 if it's a vowel (taking vowels as: 'a', 'e', 'i', 'o', 'u', 'y')
# and every other letter as 1. Then find the number of times a given pattern is repeated in a given word.
# Example:
# word = "amazing"
# pattern = "010"
# return: 2

import regex as re


def pattern_counter(text, sub):
    vowels = ["a", "e", "i", "o", "u", "y"]
    temp = ""

    for e in text:
        if e in vowels:
            temp += str(0)
        else:
            temp += str(1)

    return len(re.findall(sub, temp, overlapped=True))


word = "amazinegy"
pattern = "010"
count = pattern_counter(word, pattern)

print(pattern, "is repeated", count, "times in", word)
