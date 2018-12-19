#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 08:40:33 2018

@author: shashankgupta
"""

def longestRepeatedSequence(string):
    n = len(string)
    temp = [[0 for x in range(n+1)] for y in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if (string[i-1] == string[j-1] and i != j):
                temp[i][j] = 1+ temp[i-1][j-1]
            else:
                temp[i][j] = max(temp[i-1][j],temp[i][j-1])
                
    print(temp)
    return temp[n][n]
        

def main():
    string = "shashank"
    print(longestRepeatedSequence(string))

if __name__ == "__main__":
    main()