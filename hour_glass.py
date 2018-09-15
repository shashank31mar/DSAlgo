#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 18:36:42 2018

@author: shashankgupta
"""

import math
import os
import random
import re
import sys

def calculate_sum(arr,row_start,row_end,col_start,col_end):
    window_sum = 0
    for i in range(row_start,row_end):
        for j in range(col_start,col_end):
            if i== row_start+1 and (j==col_start or j==col_start+2):
                pass
            else:
                window_sum += arr[i][j]
    return window_sum
    
# Complete the array2D function below.
def array2D(arr):
    window = 3
    stride = 1
    rows = len(arr)
    cols = len(arr[0])
    max_sum = -math.inf
    print("rows:{}, cols:{}".format(rows,cols))
    for i in range(0,rows-window+1,stride):
        for j in range(0,cols-window+1,stride):
            #if j+window <= cols and i+window <= rows:
            print("row_start:{}, row_end:{}, col_start:{}, col_end:{}".format(i,i+window,j,j+window))
            max_sum = max(calculate_sum(arr,i,i+window,j,j+window),max_sum)        
    return max_sum

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = [[1,1,1,0,0,0],
           [0,1,0,0,0,0],
           [1,1,1,0,0,0],
           [0,9,2,-4,-4,0],
           [0,0,0,-2,0,0],
           [0,0,-1,-2,-4,0]]

    #for _ in range(6):
    #    arr.append(list(map(int, input().rstrip().split())))

    result = array2D(arr)
    print(result)