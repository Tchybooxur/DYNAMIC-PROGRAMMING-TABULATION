# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 18:44:33 2023

@author: CHIBUZOR

Alvin's (coderbyte on YouTube) Tabulation recipe:
    . Visualise the problem as a table
    . Size the table based on the input
    . Initialise the table with default values
    . Seed the trivial answer into the table
    . Iterate through the table
    . Fill further position based on the current position
    
    
QUESTION:
(CanSum Tabulation)
Write a funtion `canSum(targetSum, numbers)` that takes in a targetSum and an array
of numbers as arguments.

The function should return a boolean indicating whether or not it is possible to
generate the targetSum using numbers from the array.

You may use an element of the array as many times as needed.

You may assume that all input numbers are nonnegative.  


Test:

print(canSum(7, [2, 3])) # True
print(canSum(7, [5, 3, 4, 7])) # True
print(canSum(7, [2, 4])) # False
print(canSum(8, [2, 3, 5])) # True
print(canSum(300, [7, 14])) # False


"""

def canSum(targetSum, numbers):
    
    table = [False for x in range(targetSum+1)]
    table[0] = True
    
    for i in range(targetSum+1):
        if (table[i] == True):
            for num in numbers:
                if (i+num <= targetSum): table[i+num] = True
    
    return table[targetSum]
    

print(canSum(7, [2, 3])) # True
print(canSum(7, [5, 3, 4, 7])) # True
print(canSum(7, [2, 4])) # False
print(canSum(8, [2, 3, 5])) # True
print(canSum(300, [7, 14])) # False















