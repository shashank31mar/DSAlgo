#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 21:23:44 2018

@author: shashankgupta
"""
'''
O(n2)
'''
def longest_increasing_subsequence(arr):
    n = len(arr)
    
    lis = [1]*n
    
    for i in range(1,n):
        for j in range(i):
            if arr[j] < arr[i] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
                
    print(lis)
    return max(lis)
    
#Binary search
def ceil(arr,l,r,key):
    while r-l > 1:
        m = l + (r-l)//2
        if arr[m] >= key:
            r = m
        else:
            l = m
    return r
#Nlog(N)
def longest_increasing_subsequence_op(arr):
    n = len(arr)
    tailTable = [0]*n
    length = 0
    tailTable[0] = arr[0]
    length = 1
    
    for i in range(1,n):
        if arr[i] < tailTable[0]:
            tailTable[0] = arr[i]
        elif arr[i] > tailTable[length-1]:
            tailTable[length] = arr[i]
            length += 1
        else:
            tailTable[ceil(tailTable,-1,length-1,arr[i])] = arr[i]
    print(tailTable)
    return tailTable[:length]
def main():
    arr = [10, -2, 22, -1, 9, 33, 21, 50, 41, 60]
    print(longest_increasing_subsequence_op(arr))
    
if __name__ == "__main__":
    main()