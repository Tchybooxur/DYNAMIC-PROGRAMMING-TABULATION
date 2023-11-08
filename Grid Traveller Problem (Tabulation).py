# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 16:40:19 2023

@author: USER
"""


# GRID TRAVELLER PROBLEM: (SOLUTION USING TABULATION) 

"""
Say that you are a traveller on a 2D grid, you begin in the top-left corner and 
your goal is to travel to the bottom-right corner. You may only move down or right.

In how many ways can you travel to the goal on a grid with dimensions m x n?

Write a function `gridTraveler(m, n)` that calculates this.


Test:
    print(gridTraveler(2, 1)) #1  
    print(gridTraveler(4, 8)) #120
    print(gridTraveler(6, 5)) #126
    print(gridTraveler(18, 18)) #2333606220
    print(gridTraveler(200, 100)) #927146368619523911880353071644683518457183055907168050983953992710090597173692000
    print(gridTraveler(2000, 1000)) #6912236333055236403330584541745680459519463626285830466395524714303685330402773
                                    45296626875841166684321169298596942021743648856742525354687064727985040813072833
                                    98309835833162165478546310418372749602271977869999060739950989003993507465756048
                                    34524238805638973331655976521905545464147751233982164358677875585138270874824014
                                    26502077458513642368476027709203449532059445347217464362725558335456245208703796
                                    44808538727712034570489328635808512935971289580030620701185147610444861455935640
                                    18130948927454070252696208610692822805746192653088522128393643172276880497443921
                                    32513907072799305285887434833755230985273561639435828842798413563253288730449798
                                    03270165538466696959974627603413151238223342096461218102109038530276668134602291
                                    13077952944431205473876335494096896933563012184893664076231242966497163799088346
                                    9322961358570138801535936000

"""

import time

start = time.time()

def gridTravelerTab(m, n):   
   
    # construct our array of arrays aka table
    table = [[0 for x in range(n+1)] for y in range(m+1)]
    table[1][1] = 1
    
    for i in range(m+1):
        for j in range(n+1):
            currentItem = table[i][j]
            if (j+1 <= n): table[i][j+1] += currentItem
            if (i+1 <= m): table[i+1][j] += currentItem
    
    return table[i][j] 

print(gridTravelerTab(2, 1))
print(gridTravelerTab(4, 8))
print(gridTravelerTab(6, 5))
print(gridTravelerTab(18, 18))
print(gridTravelerTab(200, 100))
print(gridTravelerTab(2000, 1000))

print("Time consumed: ", time.time() - start) 

