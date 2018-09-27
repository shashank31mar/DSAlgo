#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 21:03:13 2018

@author: shashankgupta
"""
import math

class Node:
    def __init__(self,key,name):
        self.key = key
        self.name = name

    def printData(self):
        print("Name :{} --> Key :{}".format(self.name, self.key))
        
    def getData(self):
        return self.name + "-" + str(self.key)
        
class GenericHeap:
    def __init__(self,capacity=10,arr=[]):
        print("Initializing : " + type(self).__name__)
        self.heap = []
        self.capacity = capacity
        self.heap_size = 0
        if not arr:
            self.heap = [None]*capacity
        else:
            for x in arr:
                self.heap.append(x)
            self.capacity = capacity
    
    def parent(self,i):
        return (i-1)//2
    
    def left(self,i):
        return (2*i +1)
    
    def right(self,i):
        return (2*i + 2)
  
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
        print(type(self).__name__ + " is :", end="\n")
        for i in range(self.heap_size):
            self.heap[i].printData()
        #print(self.heap[:self.heap_size])
        
    def convertToHeap(self,dic):
        print(type(self).__name__)
        for k,v in dic.items():
            n = Node(v,k)
            self.insert(n)

class MinGHeap(GenericHeap):
    def getMin(self):
        if self.heap_size > 0:
            print(type(self).__name__[:3] + " is :", end=" ")
            return self.heap[0].getData()
        else:
            print("Heap is empty!")
            return None
    
    def extractMin(self):
        if self.heap_size <= 0:
            print("heap is emtpy!!")
            return None
        if self.heap_size == 1:
            self.heap_size -= 1
            return self.heap[0].getData()
        
        min_ele = self.heap[0].getData()
        self.heap[0] = self.heap[self.heap_size-1]
        self.heap_size -= 1
        self.minHeapify(0)
        return min_ele
    
    def minHeapify(self,index=0):
        l = self.left(index)
        r = self.right(index)
        smallest = index
        if l < self.heap_size and self.heap[l].key < self.heap[index].key:
            smallest = l
        if r < self.heap_size and self.heap[r].key < self.heap[smallest].key:
            smallest = r
        if smallest != index:
            self.heap[smallest],self.heap[index] = self.heap[index], self.heap[smallest]
            self.minHeapify(smallest)
    
    def fixHeap(self,index):
        while index!=0 and self.heap[self.parent(index)].key > self.heap[index].key:
            #print("parent :{}, index :{}".format(self.parent(index),index))
            self.heap[self.parent(index)], self.heap[index] = self.heap[index],\
            self.heap[self.parent(index)]
            index = self.parent(index)
    
    def delete(self):
        pass
    
    def replaceMin(self,key):
        self.heap[0] = key
        self.minHeapify(0)

def main():
    dic = {'A':40,'B':30,'C':20,'D':10}
    minH = MinGHeap()
    minH.convertToHeap(dic)
    minH.printHeap()
    names = ['X','Y','Z']
    for i in range(3):
        print("Min ele is : {}".format(minH.extractMin()))
        n = Node(i*20,names[i])
        minH.insert(n)
        minH.printHeap()

    print("Min ele is : {}".format(minH.extractMin()))
    print("Min ele is : {}".format(minH.extractMin()))
    print("Min ele is : {}".format(minH.extractMin()))
    print("Min ele is : {}".format(minH.extractMin()))
if __name__ == "__main__":
    main()