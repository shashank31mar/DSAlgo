#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 22:56:46 2018

@author: shashankgupta
"""

def min_value_rotated_sorted_array(arr):
    if len(arr) == 0:
        return -1
    elif len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return min(arr[0],arr[1])
    
    return modified_binary_search(arr,0,len(arr))

def modified_binary_search(arr,l,h):
    m = l + int(h/2 - l/2)
    print("h is : ", h)
    print("l is : ", l)
    print("m is : ", m)
    if m+1 == len(arr):
        return arr[0]
    elif arr[m] < arr[m-1] and arr[m] < arr[m+1]:
        return min(arr[0],arr[m])
    elif arr[m] > arr[m-1] and arr[m] > arr[m+1]:
        return min(arr[0], arr[m+1])
    elif arr[m] > arr[m-1] and arr[m] < arr[m+1]:
        return modified_binary_search(arr,m+1,h)
        
def main():
    arr = [int(x) for x in input("Enter arr : ").split()]
    print("min value is : " , min_value_rotated_sorted_array(arr))
    
if __name__ == "__main__":
    main()