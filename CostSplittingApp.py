#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 13:01:51 2018

@author: shashankgupta
"""

import GenericHeap

class CostSplittingApp:
    def __init__(self):
        pass
    
    def settleDebt(self,creditors,debitors):
        c_maxH = GenericHeap.MaxGHeap(creditors)
        c_maxH.convertToHeap()
        d_maxH = GenericHeap.MaxGHeap(debitors)
        d_maxH.convertToHeap()
        #c_maxH.printHeap()
        #d_maxH.printHeap()
        self.settleDebtUtil(c_maxH,d_maxH)
    
    def settleDebtUtil(self,c_maxH,d_maxH):
        while c_maxH.heap_size > 0:
            min_val = min(c_maxH.getMax().key,d_maxH.getMax().key)
            c_max_name, c_max_val = c_maxH.getMax().name, c_maxH.getMax().key
            d_max_name, d_max_val = d_maxH.getMax().name, d_maxH.getMax().key
            
            #print("c_max_val :{}, d_max_val :{}, min_val :{}".format(c_max_val, d_max_val, min_val))

            if c_max_name == d_max_name:
                c_maxH.extractMax()
                d_maxH.extractMax()
                continue

            if c_max_val == 0:
                c_maxH.extractMax()
                continue
            
            if (c_max_val - min_val) == 0:
                c_maxH.extractMax()
            else:
                c_maxH.updateMaxKey(c_maxH.getMax().key - min_val)
            
            if (d_max_val - min_val) == 0:
                d_maxH.extractMax()
            else:
                d_maxH.updateMaxKey(d_maxH.getMax().key - min_val)
                
            #c_maxH.printHeap()
            #d_maxH.printHeap()
            print("{} --> {} --> {}".format(d_max_name, c_max_name, min_val))
            
def main():
    '''
    input syntax:
        total bill amount , A(Person):ows:paid, B:ows:paid
        1000 - total amount
        A 300 500 - person, ows, paid
        B 700 0
        C 0   500
    '''
    creditors = {'A':100, 'B':200, 'C':200, 'D':100}
    debitors = {'A':200, 'B':100, 'C':200, 'D':100}
    
    creditors1 = {'A':500, 'B':0, 'C':500}
    debitors1 = {'A':300, 'B':700, 'C':0}
    
    creditors2 = {'A':1000, 'B':1000, 'C':0, 'D':0, 'E':0}
    debitors2 = {'A':0, 'B':300, 'C':700, 'D':500, 'E':500}
    
    csa = CostSplittingApp()
    csa.settleDebt(creditors2, debitors2)

if __name__ == "__main__":
    main()