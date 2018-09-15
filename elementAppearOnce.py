#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 19:12:05 2018

@author: shashankgupta
"""
'''
Given an array where every element occurs three times, 
except one element which occurs only once. 
Find the element that occurs once. 
Expected time complexity is O(n) and O(1) extra space.
'''

'''
LOGIC
To rectify this mistake, the code makes use of 2 variables.
ones - At any point of time, this variable holds XOR of all the elements which have
appeared "only" once.
twos - At any point of time, this variable holds XOR of all the elements which have
appeared "only" twice.

So if at any point time,
1. A new number appears - It gets XOR'd to the variable "ones".
2. A number gets repeated(appears twice) - It is removed from "ones" and XOR'd to the
variable "twice".
3. A number appears for the third time - It gets removed from both "ones" and "twice". 
'''

def elementAppearOnce(arr):
    ones = 0
    twos = 0
    notThrees = 0
    
    for x in arr:
        twos |= ones & x
        ones ^= x
        print("x:{}".format(x),end=' ')
        notThrees = ~(ones & twos)
        ones &= notThrees
        twos &= notThrees
        print("ones:{:b}, twos:{:b}, notThrees:{:b}".format(ones,twos,notThrees))
def main():
    arr = [1,2,2,2,3,3,3]
    elementAppearOnce(arr)

if __name__ == "__main__":
    main()