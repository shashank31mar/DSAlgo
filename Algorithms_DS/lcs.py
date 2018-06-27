# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 14:35:44 2018

@author: shagupta
"""

def lcs(X,Y,algo='recur'):
    if algo == 'recur':
        return lcs_util(X,Y,len(X),len(Y))
    elif algo == 'dp':
        return lcs_dp(X,Y,len(X),len(Y))

def lcs_dp(X,Y,m,n):
    L = [[None]*(n+1) for x in range(m+1)]
    
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = 1 + L[i-1][j-1]
            else:
                L[i][j] = max(L[i-1][j],L[i][j-1])

    print(L)
    # Code to print LCS
    '''
    Following is detailed algorithm to print the LCS. It uses the same 2D table L[][].

    1) Construct L[m+1][n+1] using the steps discussed in previous post.
    
    2) The value L[m][n] contains length of LCS. Create a character array lcs[] of length equal to the length of lcs plus 1 (one extra to store \0).
    
    2) Traverse the 2D array starting from L[m][n]. Do following for every cell L[i][j]
    …..a) If characters (in X and Y) corresponding to L[i][j] are same (Or X[i-1] == Y[j-1]), then include this character as part of LCS.
    …..b) Else compare values of L[i-1][j] and L[i][j-1] and go in direction of greater value.
    
    '''
    index = L[m][n]
    
    lcs_str = [""]*(index+1)
    i = m
    j = n
    
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs_str[index-1] = X[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1
            
    print(lcs_str)
    print("".join(lcs_str))
    
    
def lcs_util(X,Y,m,n):
    if m == 0 or n == 0:
        return 0
    
    if X[m-1] == Y[n-1]:
        return 1 + lcs_util(X,Y,m-1,n-1)
    return max(lcs_util(X,Y,m,n-1),lcs_util(X,Y,m-1,n))

def main():
    X = "Shashank"
    Y = "Swati"
    lcs(X,Y,'dp')
    
if __name__ == "__main__":
    main()
    