#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 20:27:17 2018

@author: shashankgupta
"""

import heapq as heap
from collections import deque
import math

class Heap:
    def __init__(self,arr=[]):
        print("Initializing : " + type(self).__name__)
        self.heap = []
        for x in arr:
            self.heap.append(x)
        self.heap_size = 0
        self.capacity = len(arr)
        self.convertToHeap()
        
    def parent(self,i):
        return  (i-1)//2
    
    def left(self,i):
        return (2*i)+1
    
    def right(self,i):
        return (2*i)+2
    
    def fixHeap(self,index):
        print("No Base class implementation")
        
    def decreaseKey(self,index,key):
        self.heap[index] = key
        self.fixHeap(index)
        
    def insert(self,key):
        #print("size :{}, cap :{}".format(self.heap_size,self.capacity))
        if self.heap_size == self.capacity:
            print("Heap is full, not inserting!!")
            return None
        self.heap_size += 1
        i = self.heap_size - 1
        self.heap[i] = key
        self.fixHeap(i)
        
    def printHeap(self):
        print(type(self).__name__ + " is :", end=" ")
        print(self.heap[:self.heap_size])
        
    def convertToHeap(self):
        print(type(self).__name__)
        for x in self.heap:
            self.insert(x)
    
class MinHeap(Heap):
    def getMin(self):
        if self.heap_size > 0:
            print(type(self).__name__[:3] + " is :", end=" ")
            return self.heap[0]
        else:
            print("Heap is empty!")
            return None
    
    def extractMin(self):
        if self.heap_size <= 0:
            print("Heap is emtpy!")
            return None
        if self.heap_size == 1:
            self.heap_size -= 1
            data = self.heap[0]
            self.heap.remove(data)
            return data
    
        min_ele = self.heap[0]
        self.heap[0] = self.heap[self.heap_size-1]
        self.heap_size -= 1
        self.minHeapify(0)
        return min_ele
    
    def minHeapify(self,index=0):
        l = self.left(index)
        r = self.right(index)
        smallest = index
        if l < self.heap_size and self.heap[l] < self.heap[index]:
            smallest = l
        if r < self.heap_size and self.heap[r] < self.heap[smallest]:
            smallest = r
        if smallest != index:
            self.heap[smallest],self.heap[index] = self.heap[index], self.heap[smallest]
            self.minHeapify(smallest)
    
    def fixHeap(self,index):
        while index!=0 and self.heap[self.parent(index)] > self.heap[index]:
            #print("parent :{}, index :{}".format(self.parent(index),index))
            self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
            index = self.parent(index)
    
    def delete(self,key):
        self.decreaseKey(key,-math.inf)
        self.extractMin()
        
    def replaceMin(self,key):
        self.heap[0] = key
        self.minHeapify()

class MaxHeap(Heap):
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
    
    def delete(self,index):
        self.decreaseKey(index,math.inf)
        self.extractMin()
    
    def fixHeap(self,index):
        while index !=0 and self.heap[self.parent(index)] < self.heap[index]:
            self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
            index = self.parent(index)
    
    def getMax(self):
        if self.heap_size > 0:
            print(type(self).__name__[:3] + " is :", end = " ")
            return self.heap[0]
        else:
            print("Heap is emtpy!")
            return math.inf
        
    def replaceMax(self,key):
        self.heap[0] = key
        self.maxHeapify(0)

def main():
    arr = [1]
    minH = MinHeap(arr)
    maxH = MaxHeap(arr)
    #minH.convertToHeap()
    #maxH.convertToHeap()
    minH.printHeap()
    maxH.printHeap()
    print(minH.extractMin())
    '''
    minH.extractMin()
    minH.printHeap()
    print(minH.getMin())
    minH.replaceMin(11)
    minH.printHeap()
    print(minH.getMin())
    '''
    

if __name__ == "__main__":
    main()