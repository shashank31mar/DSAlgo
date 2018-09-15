#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 16 22:06:10 2018

@author: shashankgupta
"""

def max_sum(arr):
    max_so_far = arr[0]
    curr_max = arr[0]
    
    for i in range(1,len(arr)):
        curr_max = max(arr[i], curr_max + arr[i])
        max_so_far = max(curr_max, max_so_far)
    return max_so_far

def main():
    arr = [int(x) for x in input("Enter input : ").split(",")]
    print(max_sum(arr))
    
if __name__ == "__main__":
    main()