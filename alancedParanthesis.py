# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 13:37:14 2018

@author: shagupta
"""

def isBalance(arr):
    count = 0
    for x in arr:
        if x == '(':
            count += 1
        elif x == ')':
            count -= 1
            if count < 0:
                return False
    if count:
        return False
    return True


def main():
    arr = "()(ABC))("
    print(isBalance(arr))

if __name__ == "__main__":
    main()