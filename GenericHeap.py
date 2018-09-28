#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 12:15:13 2018

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
    def __init__(self,arr={},capacity=10):
        print("Initializing : " + type(self).__name__)
        self.heap = []
        self.capacity = capacity
        self.heap_size = 0
        self.heap = [None]*capacity
        self.arr = arr
        #self.convertToHeap(arr)
    
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
            print("Heap is full!")
            inp = input("Do you want to increase the capacity of heap?(Y/N):").lower()
            if inp == 'y' or inp == 'yes':
                self.capacity += 10
            elif inp == 'n' or inp == 'no':
                print("not inserting curr element!!")
            
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
        
    def convertToHeap(self):
        print(type(self).__name__)
        for k,v in self.arr.items():
            n = Node(v,k)
            self.insert(n)

class MinGHeap(GenericHeap):
    def getMin(self):
        if self.heap_size > 0:
            print(type(self).__name__[:3] + " is :", end=" ")
            return self.heap[0]
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
        
    def isEmpty(self):
        if self.heap_size == 0:
            return True
        return False

class MaxGHeap(GenericHeap):
    def getMax(self):
        if self.heap_size > 0 :
            #print(type(self).__name__[:3] + " is :", end=" ")
            return self.heap[0]
        else:
            print("Heap is empty!")
            return None
        
    def extractMax(self):
        if self.heap_size <= 0:
            print("Heap is empty!!")
            return None
        
        if self.heap_size == 1:
            self.heap_size -= 1
            return self.heap[0].getData()
        
        max_ele = self.heap[0].getData()
        self.heap[0] = self.heap[self.heap_size - 1]
        self.heap_size -= 1
        self.maxHeapify(0)
        return max_ele
    
    def maxHeapify(self,index=0):
        l = self.left(index)
        r = self.right(index)
        largest = index
        
        if l < self.heap_size and self.heap[l].key > self.heap[index].key:
            largest = l
        if r < self.heap_size and self.heap[r].key > self.heap[largest].key:
            largest = r
            
        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self.maxHeapify(largest)
            
    def fixHeap(self,index):
        while index !=0 and self.heap[self.parent(index)].key < self.heap[index].key:
            self.heap[self.parent(index)], self.heap[index] = self.heap[index],\
            self.heap[self.parent(index)]
            index = self.parent(index)

    def replaceMax(self,key):
        self.heap[0] = key
        self.maxHeapify(0)
        
    def updateMaxKey(self,val):
        self.heap[0].key = val
        self.maxHeapify(0)
        
    def isEmpty(self):
        if self.heap_size == 0:
            return True
        return False
    
    def delete(self,index):
        self.decreaseKey(index,math.inf)
        self.extractMin()
        
def main():
    dic = {'A':40,'B':30,'C':20,'D':10}
    minH = MinGHeap(dic)
    minH.convertToHeap()
    minH.printHeap()
    maxH = MaxGHeap(dic)
    maxH.convertToHeap()
    maxH.printHeap()
    maxH.updateMaxKey(-10)
    maxH.printHeap()
    
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
    print("is empty : {}".format(maxH.isEmpty()))
    minH.printHeap()
    
if __name__ == "__main__":
    main()