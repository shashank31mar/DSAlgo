#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 21:24:12 2018

@author: shashankgupta
"""
import math
class MaxHeap:
    def __init__(self,cap):
        self.heap = [None]*cap
        self.heap_size = 0
        self.capacity = cap
        
    def parent(self,i):
        return (i-1)//2
    
    def left(self,i):
        return 2*i +1
    
    def right(self,i):
        return 2*i+2
    
    def extractMax(self):
        if self.heap_size <= 0:
            print("heap is emtpy!!")
            return None
        if self.heap_size == 1:
            self.heap_size -= 1
            return self.heap[0]
        max_ele = self.heap[0]
        self.heap[0] = self.heap[self.heap_size-1]
        self.heap_size -= 1
        self.maxHeapify(0)
        return max_ele
        
    def maxHeapify(self,index):
        l = self.left(index)
        r = self.right(index)
        largest = index
        
        if l < self.heap_size and self.heap[l] > self.heap[index]:
            largest = l
        if r < self.heap_size and self.heap[r] > self.heap[largest]:
            largest = r
            
        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self.maxHeapify(largest)
    
    def insert(self,key):
        if self.heap_size == self.capacity:
            print("Heap is full!!")
            return None
        else:
            self.heap_size += 1
            i = self.heap_size - 1
            self.heap[i] = key
            self.fixHeap(i)
    
    def delete(self,index):
        self.decreaseKey(index,math.inf)
        self.extractMin()
    
    def decreaseKey(self,index,key):
        self.heap[index] = key
        self.fixHeap(index)
    
    def fixHeap(self,index):
        while index !=0 and self.heap[self.parent(index)] < self.heap[index]:
            self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
            index = self.parent(index)
    
    def getMax(self):
        if self.heap_size > 0:
            return self.heap[0]
        else:
            print("Heap is emtpy!")
            return math.inf
        
    def convertToHeap(self,arr):
        for x in arr:
            self.insert(x)
            
    def printHeap(self):
        print(self.heap[:self.heap_size])
        
    def replaceMax(self,key):
        self.heap[0] = key
        self.maxHeapify(0)

def main():
    arr = [10,9,8,7,6,5,4,3,2,1,1]
    mh = MaxHeap(25)
    mh.convertToHeap(arr)
    mh.printHeap()
    print("max :{}".format(mh.getMax()))
    mh.extractMax()
    mh.printHeap()
    print("max :{}".format(mh.getMax()))
    mh.replaceMax(8)
    mh.printHeap()
    print("max :{}".format(mh.getMax()))
    

if __name__ == "__main__":
    main()