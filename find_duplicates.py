#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 14:42:41 2018

@author: shashankgupta
"""

'''
Given an array wich contains duplicated in the range of the length of the array
starting from 0 - len(arr) - 1

find duplicate elements

'''
def findDuplicates(arr):
    n = len(arr)
    
    for i in range(n):
        arr[arr[i]] += n
        
    duplicates = {}
    
    print(arr)
    for i,x in enumerate(arr):
        if x-i > n:
            duplicates[i] = (x)//n
    
    print(duplicates)
    
def main():
    arr = [0,1,0,1,2,4,5,2]
    findDuplicates(arr)
    
if __name__ == "__main__":
    main()