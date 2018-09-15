#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 16 22:28:48 2018

@author: shashankgupta
"""

import math
def sum_of_two_largest_numbers(arr):
    max = -math.inf
    smax = -math.inf
    
    for x in arr:
        if x > max:
            smax = max
            max = x
        elif x > smax:
            smax = x
    print("max {}, smax {}", (max,smax))
    return max+smax

def main():
    arr = [int(x) for x in input("Enter input : ").split()]
    print(sum_of_two_largest_numbers(arr))
    
if __name__ == "__main__":
    main()