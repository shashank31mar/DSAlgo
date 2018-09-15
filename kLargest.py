#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 22:15:18 2018

@author: shashankgupta
"""
from heap import MaxHeap,MinHeap

def kLargestElement(arr,k):
    minH = MinHeap(arr[:k])
    minH.convertToHeap()
    
    for x in arr[k:]:
        min_ele = minH.getMin()
        if min_ele < x:
            minH.replaceMin(x)
    
    return minH.getMin()

def kSmallestElement(arr,k):
    maxH = MaxHeap(arr[:k])
    maxH.convertToHeap()
    
    for x in arr[k:]:
        max_ele = maxH.getMax()
        if max_ele > x:
            maxH.replaceMax(x)
    
    return maxH.getMax()

def main():
    arr = [1, 23, 12, 9, 30, 2, 50]
    print("{}{} largest element is :{} ".format(3,"rd",kLargestElement(arr,3)))
    print("{}{} largest element is :{} ".format(4,"th",kSmallestElement(arr,4)))

if __name__ == "__main__":
    main()

