# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 12:40:06 2018

@author: shagupta
"""

class Node:
    def __init__(self,data,right=None,left=None):
        self.data = data
        self.right = right
        self.left = left
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def push(self,data):
        if not self.head:
            self.head = Node(data)
        else:
            newNode = Node(data,self.head)
            self.head.left = newNode
            self.head = newNode
    
    def reverse(self):
        self.head = self.reverseUitl()
        print("Revesed list is : ")
    
    def reverseUitl(self,start=None,stop=None):
        prev = None
        curr = self.head if not start else start
        next = curr
        
        while next != stop:
            next = next.right
            curr.right = prev
            prev = curr
            curr = next
            
        return prev
    
    def reverseBlock(self,k):
        self.head = self.reverseBlockUtil(self.head,k)
        self.reverse()
        print("Block reversed list is : ")
        
    def reverseBlockUtil(self,head,k):
        curr = head
        next = head
        prev = None
        i=0
        
        while next and i < k:
            next = next.right
            curr.right = prev
            prev = curr
            curr = next
            i += 1
            
        if next :
            head.right = self.reverseBlockUtil(next,k)
            head.right.left = head
            
        return prev
        
    
    def printDLL(self):
        node = self.head
        print("None",end="<->")
        while node:
            print(node.data,end="<->")
            node = node.right
        print("None")
            
def main():
    dll = DoublyLinkedList()
    dll.push(10)
    dll.push(20)
    dll.push(30)
    dll.push(40)
    dll.push(50)
    dll.push(40)
    dll.push('a')
    dll.printDLL()
    dll.reverse()
    dll.printDLL()
    dll.reverse()
    dll.printDLL()
    dll.reverse()
    dll.printDLL()
    dll.reverse()
    dll.printDLL()
    dll.reverseBlock(4)
    dll.printDLL()

if __name__ == "__main__":
    main()