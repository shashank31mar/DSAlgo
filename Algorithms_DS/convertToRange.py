# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 09:31:24 2018

@author: shagupta
"""

import itertools

def ranges(i):
    for a, b in itertools.groupby(enumerate(i)):
        b = list(b)
        yield str(b[0][1])+"-"+str(b[-1][1])

def main():
    print(list(ranges([0, 1, 2, 3, 4, 7, 8, 9, 11])))
    
if __name__ == "__main__":
    
    main()
