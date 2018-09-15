#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 21:52:16 2018

@author: shashankgupta
"""

import math

def find_longest_consecutive_sequence(arr):
    min = math.inf
    max = -math.inf
    max_length = -1
    length = 0
    #arr = []
    for x in arr:
        if x < min:
            min = x
        if x > max:
            max = x
    print("min is : " , min)
    print("max is : ", max)
    if min < 0:
        arr1 = [None]*(max-min+1)
    else:
        arr1 = [None]*(max+1)
        
    for x in arr:
        if min <0:
            print("x-min is : ", x-min)
            arr1[x-min] = x
        else:
            arr1[x] = x
        
    print("arr1 is : ", arr1)
    for i, x in enumerate(arr1):
        if x == None:
            if max_length < length:
                max_length = length
            length = 0
        else:
            length +=1
            print("Length is : ", length)
    print("Max seq is : ", max_length)

def main():
    #-3 -2 -1 0 1 2 3 4 10 11 12 13 14 15 16 17 5 18 19
    #4 8 9 10 16 18 1 2 5 3
    arr = [int(x) for x in input("Enter arr : ").split()]
    find_longest_consecutive_sequence(arr)    

if __name__ == "__main__":
    main()