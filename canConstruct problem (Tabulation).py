# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 13:37:14 2023

@author: CHIBUZOR

QUESTION:
    
Write a funtion `canConstruct(target, wordBank)` that accepts a target string and an array
of strings as arguments.

The function should return a boolean indicating whether or not the `target` can be constructed
by concatenating elements of the `wordBank` array.

You may reuse elements of `wordBank` as many times as needed.

Test cases:
    print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # True
    print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # False
    print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))  # True
    print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", 
                       ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))  # False

"""


def canConstruct(target, wordBank):
    table = [True if x == 0 else False for x in range(len(target) + 1)]

    for i in range(len(target) + 1):
        if (table[i] == True):
            for word in wordBank:
                # if the word matches the character starting at position i
                if (target[i: i + len(word)] == word):
                    table[i + len(word)] = True
    return table[len(target)]


print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # True
print(canConstruct("skateboard", ["bo", "rd",
      "ate", "t", "ska", "sk", "boar"]))  # False
print(canConstruct("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))  # True
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
                   ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))  # False
