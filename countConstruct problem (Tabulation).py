# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 20:36:11 2023

@author: CHIBUZOR

Write a funtion `countConstruct(target, wordBank)` that accepts a target string and an array
of strings as arguments.

The function should return the number of ways that the `target` can be constructed
by concatenating elements of the `wordBank` array.

You may reuse elements of `wordBank` as many times as needed.

Test cases:
    print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"])) # 2
    print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # 1
    print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # 0
    print(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))  # 4
    print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", 
                       ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))  # 0

"""


def countConstruct(target, wordBank):
    table = [1 if x == 0 else 0 for x in range(len(target)+1)]

    for i in range(len(target)+1):
        for word in wordBank:
            # if the word matches the character starting at position i
            if (target[i:i+len(word)] == word):
                table[i+len(word)] += table[i]

    return table[len(target)]


print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))  # 2
print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # 1
print(countConstruct("skateboard", [
      "bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # 0
print(countConstruct("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))  # 4
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
                     ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))  # 0
