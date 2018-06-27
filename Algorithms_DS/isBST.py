# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 12:32:14 2018

@author: shagupta
"""

import math
class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
        

def isBST(root):
    return isBSTUtil(root,-math.inf,math.inf)

#Finding using decreasing range
def isBSTUtil(root,mini,maxi):
    if not root:
        return True
    
    if root.data < mini or root.data > maxi:
        return False
    
    return isBSTUtil(root.left,mini,root.data-1) and isBSTUtil(root.right,root.data+1,maxi)


def main():
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)
    print(isBST(root))
    
if __name__ == "__main__":
    main()