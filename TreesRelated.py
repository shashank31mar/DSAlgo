#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 10:10:51 2018

@author: shashankgupta
"""

class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
        
class BinaryTree:
    def __init__(self,root):
        self.root = root
        self.dic = {}
    
    def getHeight(self,root):
        if not root:
            return 0
        
        return (1 + max(self.getHeight(root.left),self.getHeight(root.right)))
    
    def diameter(self,root):
        dia_1st = self.diameter_using_height_func(root)
        _, dia = self.diameter_height(root)
        return dia
    
    def diameter_using_height_func(self,root):
        if not root:
            return 0
        
        lh = self.getHeight(root.left)
        rh = self.getHeight(root.right)
        
        ld = self.diameter_using_height_func(root.left)
        rd = self.diameter_using_height_func(root.right)
        #print("ld is in 1st :{}".format(ld))
        #print("rd is in 1st :{}".format(rd))
        return max(1+lh+rh,ld,rd)
    
    def diameter_height(self,root):
        if not root:
            return 0,0
        
        lh, ld = self.diameter_height(root.left)
        rh, rd = self.diameter_height(root.right)
        #print("ld is :{}".format(ld))
        #print("rd is :{}".format(rd))
        
        return 1+max(lh,rh), max(1+lh+rh,ld,rd)

    def width(self,root,level=None):
        self.widthUtil(root,2)
        self.dic[1] = [root.data]
        if level:
            lis = self.dic[level]
            if not lis[0][0] and not lis[len(lis)-1][0]:
                return len(lis) -2
            elif not lis[0][0] and lis[len(lis)-1][0]:
                return len(lis) - 1
            elif lis[0][0] and not lis[len(lis)-1][0]:
                return len(lis) - 1
            else:
                return len(lis)
        #count = {}
        #self.widthUtilOp(root,count,1)
        #print(count)
        
    def widthUtil(self,root,level):
        if not root:
            return None
        
        ln = self.widthUtil(root.left,level+1)
        rn = self.widthUtil(root.right,level+1)
        
        if level in self.dic:
            if (not ln and rn) or (ln and not rn):
                self.dic[level].append((ln,'l'))
                self.dic[level].append((rn,'r'))
            
        else:
            if (not ln and rn) or (ln and not rn):
                self.dic[level] = [(ln,'l'),(rn,'r')]
            
        return root.data
    
    def widthUtilOp(self,root,count,level):
        if not root:
            return
        
        self.widthUtilOp(root.left,count,level+1)
        self.widthUtilOp(root.right,count,level+1)
        if level in count:
            count[level] += 1
        else:
            count[level] = 1
            
    def isSymmetric(self,root):
        return self.isSymmetricUtil(root,root)
    
    def isSymmetricUtil(self,root1,root2):
        if not root1 and not root2:
            return True
        
        """ For two trees to be mirror images, the following three 
        conditions must be true 
        1 - Their root node's key must be same 
        2 - left subtree of left tree and right subtree 
          of right tree have to be mirror images 
        3 - right subtree of left tree and left subtree 
           of right tree have to be mirror images 
        """
        if (root1 and root2) and (root1.data == root2.data):
            return self.isSymmetricUtil(root1.left, root2.right)\
            and self.isSymmetricUtil(root1.right, root2.left)
            
        return False
        
    def commonAncestor(self,root,d1,d2):
        # For keeping track if both elements are present in the tree
        v = [False]*2
        
        node = self.commonAncestorUtil(root,d1,d2,v)
        
        if (v[0] and v[1]) or (v[0] and self.find(root,d2)) or (v[1] and self.find(root,d1)):
            return node
        return None
        
    def commonAncestorUtil(self,root,d1,d2,v):
        if not root:
            return None
        
        if root.data == d1:
            v[0] = True
            return root
            
        if root.data == d2:
            v[1] = True
            return root
            
        left = self.commonAncestorUtil(root.left,d1,d2,v)
        right = self.commonAncestorUtil(root.right,d1,d2,v)
        
        if left and right:
            return root
        
        return left if not right else right
    
    def find(self,root,data):
        if not root:
            return False
        
        if root.data == data or self.find(root.left,data) or self.find(root.right,data):
            return True

    def distance(self,d1,d2):
        comAncs = self.commonAncestor(self.root,d1,d2)
        #print(comAncs.data)
        dis1 = []
        dis2 = []
        if comAncs:
            self.distanceUtil(comAncs,d1,0,dis1)
            self.distanceUtil(comAncs,d2,0,dis2)
            return dis1[0] + dis2[0]
        return -1
    
    def distanceUtil(self,root,d,level,dis):
        if not root:
            return
        
        #print("root.data is :{}, d is :{}, level is :{}, dis is :{}".format(root.data,d,level,dis))
        if root.data == d:
            dis.append(level)
            return
        
        self.distanceUtil(root.left,d,level+1,dis)
        self.distanceUtil(root.right,d,level+1,dis)
        
    def distanceK(self,node,k):
        dis = {}
        self.distanceKUtil(self.root,node,dis)
        print(dis)
        if k in dis:
            return dis[k]
        return None
    
    def distanceKUtil(self,root,node,dis):
        if not root:
            return
        
        self.distanceKUtil(root.left,node,dis)
        self.distanceKUtil(root.right,node,dis)
        d = self.distance(root.data,node.data)
        if d in dis:
            dis[d].append(root.data)
        else:
            dis[d] = [root.data]
            
    def printVerticalOrder(self,root):
        dic = {}
        h_dis = 0
        level = 0
        self.printVerticalOrderUtil(root,h_dis,level,dic)
        dic_1 = []
        for v in sorted(dic.values()):
            dic_1.append(sorted(v,key=lambda x:x[1]))
            
        return dic_1
        
    def printVerticalOrderUtil(self,root,h_dis,level,dic):
        if not root:
            return
        
        try:
            dic[h_dis].append((root.data,level))
        except:
            dic[h_dis] = [(root.data,level)]
        self.printVerticalOrderUtil(root.left,h_dis-1,level+1,dic)
        
        self.printVerticalOrderUtil(root.right,h_dis+1,level+1,dic)
        
    def printTopView(self,root):
        dic = self.printVerticalOrder(root)
        dic_1 = []
        for v in dic:
            dic_1.append(v[0][0])
        return dic_1
            
    def levelOrder(self,root):
        if not root:
            return
        dic = []
        queue = []
        queue.append(root)
        count = 1
        while queue:
            temp = []
            while count:
                pop = queue.pop(0)
                dic.append(pop.data)
                if pop.left:
                    temp.append(pop.left)
                if pop.right:
                    temp.append(pop.right)
                count -= 1
            queue = temp
            count = len(temp)
        return dic
        
def main():
    
    data1 = Node(1)
    data2 = Node(2,data1)
    data3 = Node(3)
    data4 = Node(4,data3)
    data5 = Node(5,data2)
    data6 = Node(6,None,data4)
    data7 = Node(7,data5)
    data8 = Node(8,data6)
    data12 = Node(12)
    data11 = Node(11,None,data12)
    data9 = Node(9,data7,data11)
    root = Node(10,data9,data8)
    
    d6 = Node(6)
    d6_1 = Node(6)
    d5 = Node(5)
    d5_1 = Node(5)
    d4 = Node(4,None,d5)
    d4_1 = Node(4,d5_1)
    d3 = Node(3,d6)
    d3_1 = Node(3,None,d6_1)
    d2 = Node(2,d3,d4)
    d2_1 = Node(2,d4_1,d3_1)
    d1 = Node(1,d2,d2_1)
    
    
    bt = BinaryTree(root)
    width = bt.width(root,4)
    print("width is : {}".format(width))
    print("Diameter is :{}".format(bt.diameter(root)))
    print("Is Symmetric :{}".format(bt.isSymmetric(d1)))
    print("Common Ancestor :{}".format(bt.commonAncestor(root,9,15)))
    print("Distance b/w nodes are :{}".format(bt.distance(11,12)))
    node = data7
    k=3
    print("Distance at {} nodes from node {} are :{}".format(k,node.data,bt.distanceK(node,k)))
    print("Vertical Order :{}".format(bt.printVerticalOrder(root)))
    print("Top View :{}".format(bt.printTopView(root)))
    print("Level Order is :{}".format(bt.levelOrder(root)))
    
if __name__ == "__main__":
    main()