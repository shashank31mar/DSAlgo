#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 22:29:54 2018

@author: shashankgupta
"""


def merge_two_sorted_list(arr1,arr2):
    len1 = len(arr1)
    len2 = len(arr2)
    final_arr = []
    j=0
    k=0
    
    for i in range(len1+len2):    
        if j == len1:
            final_arr.extend(arr2[k:])
            break
        elif k == len2:
            final_arr.extend(arr1[j:])
            break
        elif arr1[j] <= arr2[k]:
            final_arr.append(arr1[j])
            j += 1
        elif arr1[j] > arr2[k]:
            final_arr.append(arr2[k])
            k +=1
    return final_arr
    

def main():
    arr1 = [int(x) for x in input("Enter first list : ").split()]
    arr2 = [int(x) for x in input("Enter second list : ").split()]
    print(merge_two_sorted_list(arr1,arr2))
    
if __name__ == "__main__":
    main()