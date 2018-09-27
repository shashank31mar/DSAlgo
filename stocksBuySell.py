#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 15:51:58 2018

@author: shashankgupta
"""
class Node:
    def __init__(self,buy=None,sell=None):
        self.buy = buy
        self.sell = sell

class StocksBuySell:
    def __init__(self,arr):
        self.arr = arr
    
    '''
    All we need to keep finding min and take diff of elements with min_ele
    rather than taking diff of an element with every other element.
    Tricky algo - Nice one
    '''
    def buySellOnceMaximizeProfit(self):
        max_diff = self.arr[1]-self.arr[0]
        min_ele = self.arr[0]
        
        for i in range(1,len(self.arr)):
            if self.arr[i] - min_ele > max_diff:
                max_diff = self.arr[i] -  min_ele
                
            if self.arr[i] < min_ele:
                min_ele = self.arr[i]
                
        return max_diff
    
    def buySellMultiple(self):
        pass
    
def main():
    arr = [50,300,1,299,3,300]
    sbs = StocksBuySell(arr)
    print("Max profit is : {}".format(sbs.buySellOnceMaximizeProfit()))

if __name__ == "__main__":
    main()