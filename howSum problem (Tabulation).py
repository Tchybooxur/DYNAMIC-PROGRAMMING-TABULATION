# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 19:20:43 2023

@author: CHIBUZOR

QUESTION:
Write a funtion `howSum(targetSum, numbers)` that takes in a targetSum and an array
of numbers as arguments.

The function should return an array containing any combination of elements
that add up to exactly the targetSum. If there is no combination that adds up
 to the targetSum, then return null. 

If there are multiple combintions possible, you may return any single one.

You may use an element of the array as many times as needed.

You may assume that all input numbers are nonnegative.


Test cases:
    print(howSum(7, [2, 3]))  # [3, 2, 2]
    print(howSum(7, [5, 3, 4, 7]))  # [4, 3]
    print(howSum(7, [2, 4]))  # None
    print(howSum(8, [2, 3, 5]))  # [2, 2, 2, 2]
    print(howSum(300, [7, 14]))  # None
"""

def howSum(targetSum, numbers):
    
    table = [None for x in range(targetSum+1)]
    table[0] = []
    
    for i in range(targetSum+1):
        if (table[i] != None):
            for num in numbers:
                if (i+num <= targetSum): table[i+num] = [*table[i], num]
    return table[targetSum]


print(howSum(7, [2, 3]))  # [3, 2, 2]
print(howSum(7, [5, 3, 4, 7]))  # [4, 3]
print(howSum(7, [2, 4]))  # None
print(howSum(8, [2, 3, 5]))  # [2, 2, 2, 2]
print(howSum(300, [7, 14]))  # None    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    