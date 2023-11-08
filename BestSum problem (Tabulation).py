# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 23:56:02 2023

@author: CHIBUZOR

QUESTION:
    
Write a funtion `bestSum(targetSum, numbers)` that takes in a targetSum and an array
of numbers as arguments.

The function should return an array containing the shortest combination of numbers
that add up to exactly the targetSum. 

If there is any tie for the shortest combination, you may return any one of the shortest.

You may use an element of the array as many times as needed.

You may assume that all input numbers are nonnegative.


Test cases:
    print(bestSum(7, [5, 3, 4, 7]))  # [7]
    print(bestSum(8, [2, 3, 5]))  # [3, 5]
    print(bestSum(8, [1, 4, 5]))  # [4, 4]
    print(bestSum(100, [1, 2, 5, 25]))  # [25, 25, 25, 25]

"""


def bestSum(targetSum, numbers):

    # create our table
    table = [None for x in range(targetSum+1)]
    table[0] = []  # set base case to empty array

    # traverse our table using index numbers up to targetSum + 1
    for i in range((targetSum+1)):
        if (table[i] != None):
            for num in numbers:
                if (i+num <= targetSum):
                    combo = [*table[i], num]
                    # compare length of array in element i to element i+num to keep the
                    # shorter one
                    if ((not table[i+num]) or (len(combo) < len(table[i+num]))):
                        table[i+num] = combo

    return table[targetSum]


print(bestSum(7, [5, 3, 4, 7]))  # [7]
print(bestSum(8, [2, 3, 5]))  # [3, 5]
print(bestSum(8, [1, 4, 5]))  # [4, 4]
print(bestSum(100, [1, 2, 5, 25]))  # [25, 25, 25, 25]
