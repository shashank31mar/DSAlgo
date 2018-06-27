# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 15:04:41 2018

@author: shagupta
"""

def lis(X):
    return lis_util(X,len(X))

def lis_util(X,n):
    if n == 1:
        return 1
    
    max_ending_here = 1
    
    
    res = lis_util(X,n-1)
    if X[n-1] > X[n-2] and res+1 > max_ending_here:
        max_ending_here = res + 1
    print(res)
    
    return max_ending_here

def main():
    X = [10,22,9,-1,33,21,50,41,60,80]
    print(lis(X))
    
if __name__ == "__main__":
    main()