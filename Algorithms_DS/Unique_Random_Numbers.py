# -*- coding: utf-8 -*-
"""
Created on Mon May 14 15:29:46 2018

@author: shagupta
"""

import random

def generateUniqueRandomNumers(low,high):
    arr = [i for i in range(low,high+1)]
    print(arr)
    max = high-low
    
    while(max !=0):
        r = random.sample(range(0, max+1),1)[0]
        #print(r)
        arr[r], arr[max] = arr[max],arr[r]
        #print(arr)
        max -= 1
        yield(arr[max+1])
        
    #print(arr)
    
if __name__ == "__main__":
    for x in generateUniqueRandomNumers(1,10):
        print(x)