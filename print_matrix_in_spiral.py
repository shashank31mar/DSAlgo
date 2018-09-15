#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 23:26:14 2018

@author: shashankgupta
"""
    
def print_sprial(mat):
    row=int(0)
    col=int(0)
    bounds = int(7)
    times = bounds
    while bounds > 0:
        print(bounds)
        while times !=0 :
            print(mat[row][col])
            col +=1
            times -=1
        bounds -= 1
        times = bounds
        col = -1
        row +=1
        while times!=0:
            print(mat[row][col])
            row += 1
            times -= 1
        times = bounds
        col = -1
        row = -1
        while times != 0:
            print(mat[row][col])
            col -=1
            times -=1
        bounds -= 1
        times = bounds
        row = times
        col += 1
        while times !=0:
            print(mat[row][col])
            row -= 1
            times -=1
        col += 1
        row += 1
        times = bounds
 

def main():
    mat = [[1,2,3,4],[2,3,6]]
    print_sprial(mat)

if __name__ == "__main__":
    main()