#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 22:07:51 2018

@author: shashankgupta
"""

def binary_search(arr,X,low,high):
    if low > high:
        return False
    
    mid = low + (high-low)//2
    
    if arr[mid] == X:
        return True
    
    if X < arr[mid]:
        return binary_search(arr,X,low,mid-1)
    return binary_search(arr,X,mid+1,high)


def find_pivot(arr,low,high):
    if low > high:
        return -1
    
    mid = low + (high -low)//2
    
    if mid < high and arr[mid] > arr[mid+1]:
        return mid
    if mid > low and arr[mid-1] > arr[mid]:
        return mid-1
    
    if arr[low] >= arr[mid]:
        return find_pivot(arr,low,mid-1)
    return find_pivot(arr,mid+1,high)
    
def rotated_binary_search(arr,X,low,high):
    if low > high:
        return False
    
    pivot = find_pivot(arr,low,high-1)
    print("pivot is : " , pivot)
    if pivot == -1:
        return binary_search(arr,X,low,high)
    if arr[pivot] == X:
        return True
        
    if arr[low] <= X:
        return binary_search(arr,X,low,pivot-1)
    return binary_search(arr,X,pivot+1,high)

def optimized_rotated_bs(arr,X,low,high):
    if low > high:
        return False
    
    mid = low + (high - low)//2
    if X == arr[mid]:
        return True
    # It means left is sorted
    if arr[low] < arr[mid]:
        if X >= arr[low] and X <= arr[mid]:
            return optimized_rotated_bs(arr,X,low,mid-1)
        return optimized_rotated_bs(arr,X,mid+1,high)
    
    # means that right is sorted
    if X >= arr[mid] and X <= arr[high]:
        return optimized_rotated_bs(arr,X,mid+1,high)
    return optimized_rotated_bs(arr,X,low,mid-1)
    
    
def main():
    arr = [5,6,7,8,9,1,2,3,4]
    print(rotated_binary_search(arr,9,0,len(arr)))
    print(optimized_rotated_bs(arr,9,0,len(arr)-1))
    
if __name__ == "__main__":
    main()