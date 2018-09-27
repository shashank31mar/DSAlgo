#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 14:05:03 2018

@author: shashankgupta
"""
import heap

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class Median:
    def __init__(self):
        pass
    
    def getMedian(self, arr):
        if len(arr) % 2 == 0:
            l = len(arr)//2
            return (arr[l] + arr[l-1])/2
        else:
            return arr[len(arr)//2]

    def findMedian(self,arr1,arr2):
        if len(arr1) == len(arr2):
            self.findMedianEqual(arr1,arr2)
        else:
            self.findMedianUnEqual(arr1,len(arr1),arr2,len(arr2))
    '''
    Median of Two sorted arrays
    '''
    def findMedianEqual(self, arr1, arr2):
        if arr1 and not arr2:
            return self.getMedian(arr1)
        elif not arr1 and arr2:
            return self.getMedian(arr2)
        elif not arr1 and not arr2:
            return -1
        elif len(arr1) == 2 and len(arr2) == 2:
            mine, maxe = max(arr1[0],arr2[0]), min(arr1[1],arr2[1])
            return (mine+maxe)/2
        
        m1 = self.getMedian(arr1)
        idxM1 = arr1.index(m1)
        m2 = self.getMedian(arr2)
        idxM2 = arr2.index(m2)
        
        if m1 == m2:
            return m1
        elif m1 > m2:
            return self.findMedian(arr1[0:idxM1+1],arr2[idxM2:len(arr2)+1])
        elif m2 > m1:
            return self.findMedian(arr1[idxM1:len(arr1)+1],arr2[0:idxM2+1])
        
    def findMedianUnEqual(self,arr1,n,arr2,m):
        if arr1 and not arr2:
            return self.getMedian(arr1)
        elif not arr1 and arr2:
            return self.getMedian(arr2)
        elif not arr1 and not arr2:
            return -1
        
        min_i = 0
        max_j = n
        median = 0
        
        while min_i <= max_j:
            i = int((min_i + max_j)/2)
            j = int((n+m+1)/2 - i)
            
            if i < n and j > 0 and arr2[j-1] > arr1[i]:
                min_i = i + 1
            
            elif i > 0 and j < m and arr1[i-1] > arr2[j]:
                max_j = i - 1
                
            else:
                if i==0:
                    median = arr2[j-1]
                elif j==0:
                    median = arr1[i-1]
                else:
                    median = max(arr1[i-1],arr2[j-1])
                    #Condition found
                break
        if (n+m)%2 ==1:
            return median
        
        if i==n:
            return (median+arr2[j])/2
        
        if j ==m:
            return (median+arr1[i])/2
        
        return (median + min(arr1[i],arr2[j]))/2
        
    def findMedianKArr(self,arrays):
        arr = []
        dic = {}
        total_len =0
        for i, ar in enumerate(arrays):
            total_len += len(ar)
            arr.append(ar[0])
            if ar[0] in dic:
                dic[ar[0]].append(i)
            else:
                dic[ar[0]] = [i]
        print(arr)
        minH = heap.MinHeap(arr)
        prev = None
        min_ele = None

        for i in range(total_len//2):
            min_ele = minH.extractMin()
            #print("min ele is :{}".format(min_ele))
            #minH.printHeap()
            arr_index = dic[min_ele][0]
            dic[min_ele].remove(arr_index)
            ele_index = arrays[arr_index].index(min_ele)
            if ele_index + 1 < len(arrays[arr_index]):
                new_ele = arrays[arr_index][ele_index+1]
                #print("new ele is :{}".format(new_ele))
                minH.insert(new_ele)
                #minH.printHeap()
                if new_ele in dic:
                    dic[new_ele].append(arr_index)
                else:
                    dic[new_ele] = [arr_index]
            prev = min_ele

        if total_len %2 == 1 :
            return minH.getMin()
        else:
            return (prev + minH.getMin())/2
        
def main():
    arr = [[1,2,3,7,9],
           [2,10,11,12,13],
           [8,9,10,11,12],
           [13,14,15,16,17],
           [18,19,20,21,22],
           [2,3,4,5]
          ]
    m = Median()
    med = m.findMedianKArr(arr)
    print(med)
    

if __name__ == "__main__":
    main()