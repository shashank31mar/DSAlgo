#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 08:44:25 2018

@author: shashankgupta
"""

class Graph:
    def __init__(self,row,col,graph,nbr=8):
        self.row = row
        self.col = col
        self.graph = graph
        if nbr == 4:
            self.rowNbr = [-1,+0,0,1]
            self.colNbr = [+0,-1,1,0]
        elif nbr == 8:
            self.rowNbr = [-1,-1,-1,+0,+0,+1,1,1]
            self.colNbr = [-1,+0,+1,-1,+1,-1,0,1]
        
    def isSafe(self,i,j,visited):
        return (i >= 0 and i < self.row and
                j >= 0 and j < self.col and
                not visited[i][j] and self.graph[i][j])
               
    #Considers eight neighbours
    def DFS(self,i,j,visited):
        visited[i][j] = True
        for k in range(len(self.rowNbr)):
            if self.isSafe(i+self.rowNbr[k],j+self.colNbr[k],visited):
                self.DFS(i+self.rowNbr[k],j+self.colNbr[k],visited)
                
                
    def countIslands(self):
        visited = [[False for x in range(self.col)] for y in range(self.row)]
        count = 0 
        for i in range(self.row):
            for j in range(self.col):
                if not visited[i][j] and self.graph[i][j]:
                    self.DFS(i,j,visited)
                    count += 1
                    
        return count
    
    
def main():
    graph = [[1, 1, 0, 0, 0],
             [0, 1, 0, 0, 1],
             [1, 0, 0, 1, 1],
             [0, 0, 0, 0, 0],
             [1, 0, 1, 0, 1]]
 
 
    row = len(graph)
    col = len(graph[0])
    g = Graph(row,col,graph)
    print(g.countIslands())

if __name__ == "__main__":
    main()
    