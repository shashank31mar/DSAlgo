#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 07:48:53 2018

@author: shashankgupta
"""

def swap(arr,ai,bi,d):
    for i in range(d):
        arr[ai+i],arr[bi+i] = arr[bi+i],arr[ai+i]

def rotate_array(arr,d,n):
    '''
    divide array in two parts A[1...D-1] and B[D....high]
    if A < B divide B such that Bl is of same size as A and swap them
    So... ABlBr -> BrBlA
    else
    AlArB -> BArAl
    after doing this recur of remaining peices of A or B by changing the d
    '''
    if d == 0 or d == n:
        return
    
    if n-d == d:
        return swap(arr,0,n-d,d)
    #A is bigger
    if d > n-d:
        swap(arr,0,d,n-d)
        rotate_array(arr[n-d:],d-(n-d),d)
    elif d < n-d:
        swap(arr,0,d,n-d)
        rotate_array(arr,d,n-d)

def main():
    arr= [1,2,3,4,5]
    rotate_array(arr,4,len(arr))
    print("rotated arrary is:{}".format(arr))
    
if __name__ == "__main__":
    main()