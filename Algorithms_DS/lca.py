# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 13:16:38 2018

@author: shagupta
"""

# A recursive python program to find LCA of two nodes
# n1 and n2
 
# A Binary tree node
class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

'''
Idea is that is we encounter a node such that n1 data < node data < n2 data then node is LCA or
If n1 or n2 == node
else reccur accordingly
'''
def LCA_BST(root,n1,n2):
    if not root:
        return None
    
    if n1 > root.data and n2 > root.data:
        return LCA_BST(root.right,n1,n2)
    if n1 < root.data and root.data > n2:
        return LCA_BST(root.left,n1,n2)
    
    return root

'''
Idea is the if the current node data is either equal to n1 or n2 then that nod is the LCA else
find left lca and right lca if both are not null the root is the lca as it has onein left and other in right
else if left is null then right contains lca else left.
O(N)
handling case when the key is not present
'''
def LCA_BT_Util(root,n1,n2,v):
    if not root:
        return None
    
    if root.data == n1:
        v[0] = True
        return root
    
    if root.data == n2:
        v[1] = True
        return root
    
    l_lca = LCA_BT_Util(root.left,n1,n2,v)
    r_lca = LCA_BT_Util(root.right,n1,n2,v)
    
    if l_lca and r_lca:
        return root
    
    return l_lca if l_lca else r_lca

def find(root,k):
    if not root:
        return False
    
    if k == root.data or find(root.left,k) or find(root.right,k):
        return True
    
    return False


def LCA_BT(root,n1,n2):
    v = [False,False]
    
    lca = LCA_BT_Util(root,n1,n2,v)
    
    if (v[0] and v[1]) or (v[0] and find(lca,n2)) or (v[1] and find(lca,n1)):
        return lca.data
    else:
        return None
def main():
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    print(LCA_BST(root,10,14).data)
    print(LCA_BT(root,11,14))
    

if __name__ == "__main__":
    main()