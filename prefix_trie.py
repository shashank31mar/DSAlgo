#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 21:21:27 2018

@author: shashankgupta
"""

class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEndOfWord = False
        
class Trie:
    def __init__(self):
        self.root = self.getNode()
        
    def getNode(self):
        return TrieNode()
    
    def _charToIndex(self,ch):
        return ord(ch) - ord('a')
    
    def insert(self,key):
        pCrawl = self.root
        length = len(key)
        
        for level in range(length):
            index = self._charToIndex(key[level])
            # IF child not present add it
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
            
        #Now mark the end of the key as leaf node
        pCrawl.isEndOfWord = True
        
    def search(self,key):
        pCrawl = self.root
        length = len(key)
        
        for level in range(length):
            index = self._charToIndex(key[level])
            
            #If not present return false
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
            
        #Now we could still have not found the key as we reached at the end
        return pCrawl != None and pCrawl.isEndOfWord
    

def main():
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the","a","there","anaswe","any",
            "by","their","shashank","shas","hank"]
    
    output = ["Not present in trie",
              "Present in tire"]
 
    # Trie object
    t = Trie()
 
    # Construct trie
    for key in keys:
        t.insert(key)
 
    # Search for different keys
    print("{} ---- {}".format("the", output[t.search("the")]))
    print("{} ---- {}".format("these",output[t.search("these")]))
    print("{} ---- {}".format("their",output[t.search("their")]))
    print("{} ---- {}".format("thaw",output[t.search("thaw")]))
    print("{} ---- {}".format("sha",output[t.search("shas")]))
    print("{} ---- {}".format("hank",output[t.search("hank")]))
        
if __name__ == "__main__":
    main()