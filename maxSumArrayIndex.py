#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 21:03:05 2018

@author: shashankgupta
"""

def maxSum(arr):
    if not arr:
        return 0
    
    max_so_far = arr[0]
    curr_max = arr[0]
    start_pos = 0
    end_pos = 0
    start = 0
    
    for i in range(1,len(arr)):
        curr_max = curr_max + arr[i]
            
        if max_so_far < curr_max:
            end_pos = i
            start_pos = start
            max_so_far = curr_max
            
        if curr_max < 0:
            curr_max = 0
            start = i+1
    
    print(start_pos,end_pos)
    return arr[start_pos:end_pos+1]


def main():
    arr = [-1,2,3,-4,5,8,-1]
    arr1 = [-1,-2,-3,-4,-5]
    arr2 = [-2,1,-4,-5,6,4,3]
    print(maxSum(arr1))
    

if __name__ == "__main__":
    main()