#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 18:25:19 2018

@author: shashankgupta
"""

class ArraysRelated:
    def __init__(self):
        pass
    
    """1) Push the first element to stack.
        2) Pick rest of the elements one by one and follow following steps in loop.
            ….a) Mark the current element as next.
            ….b) If stack is not empty, then pop an element from stack and compare it with next.
            ….c) If next is greater than the popped element, then next is the next greater element for the popped element.
            ….d) Keep popping from the stack while the popped element is smaller than next. next becomes the next greater element for all such popped elements
        3) After the loop in step 2 is over, pop all the elements from stack and print -1 as next element for them.
    """
    def pop(self,stack):
        if not stack:
            print("Error : stack underflow")
        else:
            return stack.pop()
    
    def nextGreaterElement(self,arr):
        stack = []
        stack.append(arr[0])
        #print(stack)
        for i in range(1,len(arr)):
            next = arr[i]
            
            if stack:
                pop_e = self.pop(stack)
                '''If the popped element is smaller than next, then
                a) print the pair
                b) keep popping while elements are smaller and
                   stack is not empty '''
                if pop_e:
                    while pop_e < next:
                        print(str(pop_e)+ " -- " + str(next))
                        if not stack:
                            break
                        pop_e = stack.pop()
                    '''If element is greater than next, then push
                   the element back '''
                    if pop_e > next:
                        stack.append(pop_e)
            #find next grater for next element
            stack.append(next)
            
        while stack:
            pop_e = self.pop(stack)
            next = -1
            print(str(pop_e) + " -- " + str(next))
    
def main():
    ar = ArraysRelated()
    arr = [13,7,6,1,14,13,12]
    ar.nextGreaterElement(arr)
    
if __name__ == "__main__":
    main()