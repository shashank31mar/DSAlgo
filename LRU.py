#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 06:58:34 2018

@author: shashankgupta
"""
class LRUNode:
    def __init__(self,key,value,next=None,prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev
        
class LRU:
    def __init__(self,capacity):
        self.hashMap = {}
        self.head = None
        self.end = None
        self.capacity = capacity
        self.size = len(self.hashMap)
    
    def getKey(self,key):
        if key in self.hashMap:
            node = self.hashMap.get(key)
            #Removing the current pos of node
            self.delete(node)
            #Making current node as head as it has been accessed
            self.setHead(node)
            return node.value
        return -1
    
    def setKey(self,key,value):
        if key in self.hashMap:
            old = self.hashMap.get(key)
            old.value = value
            self.delete(old)
            self.setHead(old)
        else:
            newNode = LRUNode(key,value)
            if self.size >= self.capacity:
                self.hashMap.pop(self.end.key)
                self.delete(self.end)
                self.setHead(newNode)
            else:
                self.setHead(newNode)
                self.size += 1
            self.hashMap[key] = newNode
    
    def delete(self,node):
        #Head is not changing in this ase
        if node.prev:
            node.prev.next = node.next
        #Head is changing and is the next node
        else:
            self.head = node.next
            
        if node.next:
            node.next.prev = node.prev
        else:
            self.end = node.prev
        
    def setHead(self,node):
        node.next = self.head
        node.prev = None
        
        if self.head:
            self.head.prev = node
            
        self.head = node
        
        if not self.end:
            self.end = self.head
            
    def clearCache(self):
        self.hashMap.clear()
        self.head= None
        self.end = None
        
    def printLRU(self):
        curr = self.head
        print("None<->",end="")
        while curr:
            print("(k:{},v:{})<->".format(curr.key,curr.value),end = "")
            curr = curr.next
        print("None")
        
def main():
    lru = LRU(5)
    lru.setKey(1,10)
    lru.setKey(2,20)
    lru.setKey(4,30)
    lru.setKey(3,40)
    lru.setKey('a',"45")
    lru.printLRU()
    lru.setKey(3,50)
    lru.printLRU()
    lru.setKey("Tango","ALpha")
    lru.printLRU()
    lru.clearCache()
    lru.printLRU()

if __name__ == "__main__":
    main()