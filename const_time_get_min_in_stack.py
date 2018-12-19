#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 30 06:48:29 2018

@author: shashankgupta
"""
import math
from collections import deque

class Stack:
    def __init__(self):
        #self.stack = []
        self.max_stack = []
        #self.min_ele = math.inf
        self.max_ele = -math.inf
        
    def push(self,val):
        if not self.max_stack:
            #self.stack.append(val)
            self.max_stack.append(val)
            #self.min_ele = val
            self.max_ele = val
            return
        '''
        if self.min_ele <= val:
            self.stack.append(val)
        else :
            self.stack.append(2*val - self.min_ele)
            self.min_ele = val
        '''
        if self.max_ele < val:
            self.max_stack.append(2*val - self.max_ele)
            self.max_ele = val
        else:
            self.max_stack.append(val)
            
    def pop(self):
        return self.popMax()

    def popMin(self):
        if not self.stack:
            print("Stack is emtpy")
            return
        if self.stack[-1] < self.min_ele:
            #Removing min element from stack
            self.min_ele = 2*self.min_ele - self.stack[-1]
            return (self.min_ele +self.stack.pop())//2
            #print(self.stack.pop())
        return self.stack.pop()
        
    def popMax(self):
        if not self.max_stack:
            print("Stack is emtpy")
            return
        if self.max_stack[-1] > self.max_ele:
            self.max_ele = 2*self.max_ele - self.max_stack[-1]
            return (self.max_ele+self.max_stack.pop())//2

        return self.max_stack.pop()
                    
    def getMin(self,opId):
        print("operation id :{}, Min :{}".format(opId,self.min_ele))
        
    def getMax(self,opId):
        print("operation id :{}, Max :{}".format(opId,self.max_ele))
        
    def processOperations(self,operations):
        
        for i,query in enumerate(operations):
            if int(query[0]) == 1:
                for i in range(1,len(query)):
                    self.push(int(query[i]))
            elif int(query[0]) == 2:
                self.pop()
            elif int(query[0]) == 4:
                pass
                #print(self.getMin(i))
            elif int(query[0]) == 3:
                self.getMax(i)
            else:
                print("Invalid Operations, continuing to next operations!")
            print(self.max_stack)

def main():
    #n = int(input())
    operations = [[1,91],
                  [1,80],
                  [1,63],
                  [1,92],
                  [1,50],
                  [3],
                  
                  [2],
                  [3],
                  
                  [1,21],
                  [3],
                  
                  [2],
                  [2],
                  [3],
                  
                  [1,1],
                  [3],
                  
                  [2],
                  [2],
                  [3]
                  ]
    #for i in range(n):
    #    operations.append(input().split())
        
    print("")
    s = Stack()
    s.processOperations(operations)

if __name__ == "__main__":
    main()
    