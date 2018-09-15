#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 08:51:51 2018

@author: shashankgupta
"""

def longestPalindromicSequence(string):
    n = len(string)
    
    dp = [[0 for x in range(n+1)] for y in range(n+1)]
    
    for i in range(1,n):
        for j in range(i,n):
            if string[i]

def main():
    string = "shashank"
    print(longestPalindromicSequence(string))
    
if __name__ == "__main__":
    main()