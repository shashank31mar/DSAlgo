#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 07:48:57 2018

@author: shashankgupta
"""

def longestUniqueSubstring(string):
    if not string:
        return 0
    
    n = len(string)
    MAX_CHAR = 256
    max_len = 1
    curr_len = 1
    visited = [-1]*MAX_CHAR
    visited[ord(string[0])] = 0
    prev_index = 0
    
    for i in range(1,n):
        prev_index = visited[ord(string[i])]
        
        # If the currentt character is not present in the already
        # processed substring or it is not part of the current NRCS,
        # then do cur_len++
        # Case: ABCCDEFA, in this case A already there when we come to last to
        # last A but at this point A is not in the NRCS as curr it sis CDEF
        # so simply increment current length
        if prev_index == -1 or i - curr_len > prev_index:
            curr_len += 1
        
        # If the current character is present in currently considered
        # NRCS, then update NRCS to start from the next character of
        # previous instance.
        # Case: ABCEA
        else:
            max_len = max(curr_len,max_len)
            curr_len = i - prev_index
        
        visited[ord(string[i])] = i
        
    return max(curr_len,max_len)

def main():
    s = "shashank gupta is doing it!!"
    print(longestUniqueSubstring(s))
    
if __name__ == "__main__":
    main()