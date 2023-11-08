# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 11:52:11 2023

@author: CHIBUZOR
"""

# FIBONACCI PROBLEM: (SOLUTION USING TABULATION)


def fibonacciTab(n):

    if (n == 0):
        return 0
    # if (n == 1): return 1

    table = [0 for x in range(n+1)]
    table[1] = 1

    for i in range(n+1):

        if(i+1 <= n):
            table[i+1] += table[i]
        if(i+2 <= n):
            table[i+2] += table[i]

    return table[n]


print(fibonacciTab(0))
print(fibonacciTab(1))
print(fibonacciTab(2))
print(fibonacciTab(3))
print(fibonacciTab(4))
print(fibonacciTab(5))
print(fibonacciTab(10))
print(fibonacciTab(5000))
