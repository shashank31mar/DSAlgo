#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 20:39:18 2018

@author: shashankgupta
"""
def sort_array(arr):
    low = 0
    mid=0
    high = len(arr)-1
    
    while mid <=high:
        if arr[mid] == 0:
            arr[low],arr[mid] = arr[mid],arr[low]
            low +=1
            mid +=1
        elif arr[mid] == 1:
            mid +=1
        elif arr[mid] == 2:
            arr[mid],arr[high] = arr[high],arr[mid]
            mid +=1
            high -=1
    return arr

def main():
    arr= [0,1,2,0,1,2,0,1,2]
    print(sort_array(arr))

if __name__ == "__main__":
    main()