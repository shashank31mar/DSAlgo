#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 23:02:16 2018

@author: shashankgupta
"""

'''
Given the N*N matrix, find the given number in the matrix. All rows are sorted. And each row first element is less than the previous row last index.
input :

[1,3,5,7,9]
[11,13,15,16,20]
[21,22,23,24,25]
[30,32,35,40,45]

Given Num : 23

What is the best Optimal solution ? I have used BST but the interviewer asked to use any other which could do better in the above scenario.
'''


def findX(arr,X):
    rows,cols = len(arr),len(arr[0])
    low, high = 0,rows*cols-1
    
    while low <= high:
        mid = high/2 + low/2
        currRow = int(mid/cols)
        currCol = int(mid%cols)
        currEle = arr[currRow][currCol]
        
        if currEle == X:
            return True
        elif currEle < X:
            low = mid +1
        else:
            high = mid -1
    return False

def main():
    arr = []
    rows,cols = input("Enter row and cols : ").split()
    for row in range(int(rows)):
        arr.append([int(x) for x in input("Enter first row : ").split()])
    X = int(input("Enter Element to find : "))
    print(findX(arr,X))

if __name__ == "__main__":
    main()