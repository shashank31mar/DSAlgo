#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 17:04:48 2018

@author: shashankgupta
"""

from enum import Enum

class Algo(Enum):
    RECUR = "RECUR"
    DP = "DP"

class StringsRelated:
    def __init__(self):
        pass
    
    def max_common_subsequence(self,str1,str2,algo = Algo.DP):
        if algo.value == Algo.RECUR.value:
            return self.max_common_subsequence_recur(str1,str2,len(str1),len(str2))
        elif algo.value == Algo.DP.value:
            return self.max_common_subsequence_dp(str1,str2,len(str1),len(str2))
        else:
            print("Wrong algo given, select dp or recur")

    '''
    Writing recursive algo as from there we i was easily able to derive dp solution
    Recursive Logic:
        Theare are two cases for finding max com subsequence
        1) if str1[m-1] matches str2[n-1], it means that we have found at least
            one common subsequence and now we need to find rest in the remaining one
            so we compare the rest of the string similarly
            Final equation becomes : 1 + recur(str1[:m-1],str[:n-1])
        2) if the last chars dont meet then we have two cases:
            a) either we will have max string in str1[0:m-2] and str2[0:n-1]
            b) or we will have max string in str1[0:m-1] and str2[0:n-2]
            So all we do is recur on max(reucr(str1[0:m-2],str2[1:n-1]),(str1[1:m-1],str2[0:n-1]))
    '''
    
    def max_common_subsequence_recur(self,str1,str2,m,n):
        if m == 0 or n == 0:
            return 0
        
        if str1[m-1] == str2[n-1]:
            return 1 + self.max_common_subsequence_recur(str1,str2,m-1,n-1)
        else:
            return max(self.max_common_subsequence_recur(str1,str2,m,n-1),\
                       self.max_common_subsequence_recur(str1,str2,m-1,n))
    
    '''
    For a problem to be solve by seeing if we are some how computing something at a step
    that has already been computed. If yes then we can save it and reuse it.
    So in the above problem what we have is (mcsr(most_common_subsequence_recur))
                                    mcsr(abcd, cdabc)
                                /                       \
                    mcsr(abc,cdabc)                   mcsr(abcd, cdab)
                      /         \                       /
                mcsr(ab,cdabc)  mcsr(abc,cdab)       mcsr(abc,cdab)
                
    In the above recursion tree we see that mcsr(abc,cdab) has been calculated twice
    So we can save such computions and we do not have to do them again.
    This is how we reduce the complexity to n2.
    To do that we create a 2D array to size m,n and we calculated from bottom of the tree
    so that we can use saved computations
    '''
    def max_common_subsequence_dp(self,str1,str2,m,n):
        dp_arr = [[None]*(n+1) for i in range(m+1)]
        
        for i in range(m+1):
            dp_arr[i][0] = 0
            
        for j in range(n+1):
            dp_arr[0][j] = 0
            
        for i in range(1,m+1):
            for j in range(1,n+1):
                if str1[i-1] == str2[j-1]:
                    dp_arr[i][j] = 1 + dp_arr[i-1][j-1]
                else:
                    dp_arr[i][j] = max(dp_arr[i-1][j],dp_arr[i][j-1])
        
        #Printing max commom subsequence as well 
        idx = dp_arr[m][n]
        mcs = [""] * (idx+1)
        mcs[idx] = ""
        i = m
        j = n
        
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                mcs[idx-1] = str1[i-1]
                i-=1
                j-=1
                idx-=1
            elif dp_arr[i-1][j] > dp_arr[i][j-1]:
                i-=1
            else:
                j-=1

        return "".join(mcs),dp_arr[m][n]

    
def main():
    str1 = "abcd"
    str2 = "cdabc"
    sr = StringsRelated()
    print("RECUR: max common subsequence length is : {}".\
          format(sr.max_common_subsequence(str1,str2,Algo.RECUR)))
    
    print("DP: max common subsequence is : {}".\
          format(sr.max_common_subsequence(str1,str2,Algo.DP)))
    
if __name__ == "__main__":
    main()