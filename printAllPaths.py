#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 18:13:03 2018

@author: shashankgupta
"""

def printAllPaths(mat):
    #count = 0
    return printAllPathsUtil(mat,0,0,"")
    #return count
    
def printAllPathsUtil(mat,i,j,path):
    count = 0
    if i == len(mat) - 1:
        for k in range(j,len(mat[0])):
            path += str(mat[i][k])
        print(path)
        count += 1
        #print(count)
        return count
    elif j == len(mat[0]) - 1:
        for k in range(i,len(mat)):
            path += str(mat[k][j])
        print(path)
        count += 1
        #print(count)
        return count
    
    #print("i:{}, j:{}".format(mat[i][j],j))
    count += printAllPathsUtil(mat,i,j+1,path+str(mat[i][j]))
    count += printAllPathsUtil(mat,i+1,j,path+str(mat[i][j]))
    #count += printAllPathsUtil(mat,i+1,j+1,path+str(mat[i][j]))
    return count

def main():
    mat = [[1,2,3],
           [4,5,6],
           [7,8,9]]
    print(printAllPaths(mat))

if __name__ == "__main__":
    main()