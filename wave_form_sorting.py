#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 00:38:32 2018

@author: shashankgupta
"""

def sort_wave_form(arr):
    for i in range(0,len(arr),2):
        if i > 0 and arr[i] < arr[i-1]:
            arr[i],arr[i-1] = arr[i-1],arr[i]
        elif i < len(arr)-1 and arr[i] < arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
    return arr

def main():
    arr1 = [1,2,3,4,5,6,7]
    print(sort_wave_form(arr1))
    
if __name__ == "__main__":
    main()
    