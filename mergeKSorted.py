#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 22:42:24 2018

@author: shashankgupta
"""

from heap import Heap
import math

def mergeKSorted(arr,n,k):
    temp = []
    arr_index = []
    next_arr_index = []
    for i in range(k):
        temp.append(arr[i][0])
        arr_index.append(i)
        next_arr_index.append(1)
    
    mh = Heap(temp)
    mh.convertToHeap()
    
    output = []
    for i in range(n*k):
        root = mh.getMin()
        output.append(root)
        
        if next_arr_index[arr_index.index(root)] < n:
            root = arr[arr_index.index(root)][next_arr_index[arr_index.index(root)]]
            next_arr_index[arr_index.index(root)] += 1
        else:
            root = math.inf
            
        mh.replaceMin(root)

def main():
    arr = [[1,2,3,4],
           [2,3,4,5],
           [6,7,8,9]]
    mergeKSorted(arr,3,3)
    
if __name__ == "__main__":
    main()