#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 22:37:49 2018

@author: shashankgupta
"""
'''
1) Find the largest number and count its digit n
2) extend every number by n+1 and trim the remaining chars
3) sort based on extended values
4) join the elements

'''
def comparator(item):
    print(item)
    return item

def formBiggestNumber(arr):
    max_ele = max(arr)
    max_digit = len(str(max_ele)) + 1
    new_arr = [int((str(x)*max_digit)[:max_digit]) for x in arr]
    new_arr = dict(zip(arr,new_arr))
    new_arr = sorted(new_arr.items(),key=lambda x:x[1], reverse=True)
    print(new_arr)
    number = "".join([str(x[0]) for x in new_arr])
    return number

def main():
    arr = [98,9,1,112,99,4,998]
    print(formBiggestNumber(arr))
    
if __name__ == "__main__":
    main()