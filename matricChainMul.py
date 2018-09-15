#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 09:55:23 2018

@author: shashankgupta
"""

import math
def matrixChainMultiplication(arr,algo='dp'):
    if algo == 'recur':
        return matrixChainMultiplicationRecurUtil(arr,1,len(arr)-1)
    elif algo == 'dp':
        return matrixChainMultiplicationDp(arr)

def matrixChainMultiplicationDp(arr):
    min_size = [[0 for x in range(len(arr))] for y in range(len(arr))]
    
    #print(min_size)
    n = len(arr)
    for i in range(1,n):
        min_size[i][i] = 0
        
    for L in range(2,n):
        for i in range(1,n-L+1):
            j = i+L-1
            print("i:{}, j:{}".format(i,j))
            
            min_size[i][j] = math.inf
            
            for k in range(i,j):
                cost = min_size[i][k] + min_size[k+1][j] + arr[i-1]*arr[k]*arr[j]
                min_size[i][j] = min(min_size[i][j],cost)
                
    print(min_size)
    return min_size[1][n-1]

def matrixChainMultiplicationRecurUtil(arr,i,j):
    if i == j:
        return 0
    
    min_size = math.inf
    
    for k in range(i,j):
        count = matrixChainMultiplicationRecurUtil(arr,i,k) \
                    + matrixChainMultiplicationRecurUtil(arr,k+1,j) \
                    +(arr[i-1] * arr[k] * arr[j])
        #print(count)
        min_size = min(min_size, count)
    return min_size

def main():
    arr = [10, 20, 30, 40, 30]
    print("min product : {}".format(matrixChainMultiplication(arr)))

if __name__ == "__main__":
    main()