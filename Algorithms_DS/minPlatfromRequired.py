# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 16:28:49 2018

@author: shagupta
"""

def minPlatformRequired(arr,dep):
    # Taking care of the case where arr,dep = 1900,200(next day)
    for i in range(len(arr)):
        dep[i] = 2400 + dep[i] if arr[i] > dep[i] else dep[i]
 
    arr.sort()
    dep.sort()
    
    i=0
    j=0
    plat = 0
    result = 0
    
    while i < len(arr) and j < len(dep):
        #case where train is leaivng early
        if arr[i] > dep[j]:
            plat -= 1
            j += 1
            
        else:
            plat += 1
            result = max(plat,result)
            i += 1
            
    return result

def main():
    arr = [900, 940, 950, 1100, 1500, 1800,1900,1930,1945]
    dep = [910, 1200, 1120, 1130, 1900, 2000,0100,0200,0130]
    print(minPlatformRequired(arr,dep))

if __name__ == "__main__":
    main()