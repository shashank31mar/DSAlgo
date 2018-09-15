#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 16 22:45:15 2018

@author: shashankgupta
"""

def find_numbers_add_up_to_a_number(arr,N):
    found  = False
    for x in arr:
        r = N-x
        for y in arr:
            if y == r and y!= x:
                found = True
                break
        if found:
            break
    return found
    
def main():
    arr = [int(x) for x in input("Enter input : ").split()]
    N = int(input("Enter sum : "))
    print(find_numbers_add_up_to_a_number(arr,N))
    
if __name__ == "__main__":
    main()