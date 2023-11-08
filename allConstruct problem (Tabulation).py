# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 22:34:02 2023

@author: CHIBUZOR

Write a funtion `allConstruct(target, wordBank)` that accepts a target string and an array
of strings as arguments.

The function should return a 2D array containing all of the ways that the `target` 
can be constructed by concatenating elements of the `wordBank` array. Each element of the 
2D array should represent one combination that constructs the `target`.

You may reuse elements of `wordBank` as many times as needed.

Test cases:
    print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"])) 
    # [
    #    ["purp", "le"],
    #    ["p", "ur", "p", "le"],
    # ]
    
    print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"])) 
    # [
    #    ["ab", "cd", "ef"],
    #    ["ab", "c", "def"],
    #    ["abc", "def"],
    #    ["abcd", "ef"]
    # ]
    
    print(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) 
    # []
    
    print(allConstruct("aaaaaaaaaaaaaaaaaaaaaaaaaaaz", ["a", "aa", "aaa", "aaaa", "aaaaa"])) 
    # []
    
"""


def allConstruct(target, wordBank):
    # create table
    table = [[[]] if x == 0 else [] for x in range(len(target) + 1)]

    # traverse table and wordBank algorithmically
    for i in range(len(target) + 1):
        for word in wordBank:
            if (target[i:i+len(word)] == word):
                # add word behind array element
                # remember table[i] is an array
                newCombo = list(
                    map(lambda subarray: [*subarray, word], table[i]))
                table[i+len(word)] += newCombo
    return table[len(target)]


print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
# [
#    ["purp", "le"],
#    ["p", "ur", "p", "le"],
# ]

print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
# [
#    ["ab", "cd", "ef"],
#    ["ab", "c", "def"],
#    ["abc", "def"],
#    ["abcd", "ef"]
# ]

print(allConstruct("skateboard", [
      "bo", "rd", "ate", "t", "ska", "sk", "boar"]))
# []

print(allConstruct("aaaaaaaaaaz",
      ["a", "aa", "aaa", "aaaa", "aaaaa"]))
# []
