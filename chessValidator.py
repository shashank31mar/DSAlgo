#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 12:30:53 2018

@author: shashankgupta
"""

class Node:
    def __init__(self,c,e):
        self.ele = e
        self.color = c
    def name(self):
        return self.color + self.ele
    def Color(self):
        return self.color
    def setEle(self,ele):
        self.ele = ele[1]
        self.color= ele[0]
    
class ChessValidator:
    def __init__(self,r=8,c=8):
        self.r = r
        self.c = c
        self.board = [[None]*c for i in range(r)]
        self.colorMap = {'b':'black','w':'white'}
        #self.initializeKey()
        self.initializeState()
        
    def initializeState(self):
        if(self.r != 8 or self.c != 8):
            return "ERROR: board size :{},{} - not initializing!".format(self.r,self.c)
        
        for col in range(self.c):
            self.board[1][col] = Node("w","p")
            self.board[6][col] = Node("b","p")
            if col == 3:
                self.board[0][col] = Node("w","q")
                self.board[7][col] = Node("b","q")
            elif col == 4:
                self.board[0][col] = Node("w","k")
                self.board[7][col] = Node("b","k")
            elif col ==0 or col == 7:
                self.board[0][col] = Node("w","r")
                self.board[7][col] = Node("b","r")
            elif col == 1 or col == 6:
                self.board[0][col] = Node("w","h")
                self.board[7][col] = Node("b","h")
            elif col == 2 or col == 5:
                self.board[0][col] = Node("w","b")
                self.board[7][col] = Node("b","b")
       
    def capture(self,element,r,c):
        ele_c = element[0]
        curr_ele = self.board[r][c]
        if curr_ele and curr_ele.Color() != ele_c:
            print("Capturing element : {}".format(curr_ele.name()))
            return True
        return False
            
    def movePawn(self,element,start,end):
        curr_r, curr_c = start[0],start[1]
        end_r, end_c = end[0],end[1]
        if end_r > self.r or end_r < 0 or end_c > self.c or end_c < 0 or abs(end_r-curr_r) != 1:
            print("!ERROR: Invalid {} Pawn Move".format(element[0])) 
            return
        
        if not self.board[end_r][end_c] or self.capture(element,end_r,end_c):
            self.board[curr_r][curr_c] = None
            self.board[end_r][end_c] = Node(element[0],element[1])
        else:
            print("!!Error: Invalid {} Pawn Move!".format(self.colorMap[element[0]]))
            return 

    def moveHorse(self,element,start,end):
        curr_r, curr_c = start[0],start[1]
        end_r, end_c = end[0],end[1]
        
        if end_r > self.r or end_r < 0 or end_c < 0 or end_c > self.c:
            print("!ERROR: Invalid Horse Move") 
            return
        
        if (abs(end_r-curr_r) == 2 and abs(end_c-curr_c) == 1) or (abs(end_r-curr_r) == 1 and abs(end_c-curr_c) == 2):
            if not self.board[end_r][end_c]:
                self.board[curr_r][curr_c] = None
                self.board[end_r][end_c] = Node(element[0],element[1])
            elif self.capture(element,end_r,end_c):
                self.board[curr_r][curr_c] = None
                self.board[end_r][end_c] = Node(element[0],element[1])
            else:
                print("!!ERROR: Invalid Horse Move")
                return
        else:
            print("ERROR: Invalid Horse Move")
            return
        
    def moveQueen(self,element,start,end):
        curr_r, curr_c = start[0],start[1]
        end_r, end_c = end[0],end[1]
        
        if end_r > self.r or end_r < 0 or end_c < 0 or end_c > self.c:
            print("!ERROR: Invalid Queen Move") 
            return
        i = curr_r
        j = curr_c
        if end_c == curr_c:
            while i != end_r+1:
                print("i si : " , i)
                if not self.board[i][end_c] or self.board[i][end_c].name() == element or self.capture(element,i,end_c):
                    print("here")
                    if end_r > curr_r:
                        i += 1
                    elif end_r < curr_r:
                        i -= 1
                    continue
                else:
                    print("!!ERROR: Invalid {} Queen Move".format(self.colorMap[element[0]]))
                    return
            self.board[curr_r][curr_c] = None
            self.board[end_r][end_c] = Node(element[0],element[1])
        elif end_r == curr_r:
            while j != end_c+1:
                print("j is ", j)
                if j < self.c and not self.board[end_r][j] or self.board[end_r][j].name() == element or self.capture(element,end_r,j):
                    if end_c > curr_c:
                        j += 1
                    elif end_c < curr_c:
                        j -= 1
                    #j += 1
                    continue
                else:
                    print("!ERROR: Invalid Queen Move") 
                    return
            self.board[curr_r][curr_c] = None
            self.board[end_r][end_c] = Node(element[0],element[1])
        else:
            while i != end_r and j != end_c:
                print("i,j",i,j)
                if (not self.board[i][j] or self.capture(element,i,j) or self.board[i][j].name() == element):
                    if end_r < curr_r and end_c > curr_c:
                        i -= 1
                        j += 1
                    elif end_r < curr_r and end_c < curr_c:
                        i -= 1
                        j -= 1
                    elif end_r > curr_r and end_c > curr_c:
                        i += 1
                        j += 1
                    elif end_r > curr_r and end_c < curr_c:
                        i += 1
                        j -= 1
                    continue
                else:
                    print("!ERROR: Invalid {} Queen Move".format(self.colorMap[element[0]])) 
                    return
            self.board[curr_r][curr_c] = None
            self.board[end_r][end_c] = Node(element[0],element[1])
    def printBoard(self):
        for i in range(self.r):
            for j in range(self.c):
                if self.board[i][j]:
                    print(self.board[i][j].name(), end= " ")
                else:
                    print("--",end = " " )
            print()

def main():
    cv = ChessValidator()
    cv.printBoard()
    '''
    cv.movePawn("wp",[1,0],[2,0])
    cv.movePawn("wp",[2,0],[3,0])
    cv.movePawn("wp",[3,0],[2,0])
    cv.movePawn("wp",[2,0],[1,0])
    #cv.movePawn("wp",[1,0],[0,0])
    cv.movePawn("bp",[6,1],[5,1])
    cv.moveHorse("wh",[0,1],[2,2])
    cv.moveHorse("bh",[7,1],[5,0])
    cv.moveHorse("bh",[5,0],[3,1])
    cv.movePawn("wp",[1,0],[2,0])
    cv.movePawn("wp",[2,0],[3,1])
    cv.movePawn("wp",[1,3],[2,3])
    cv.movePawn("wp",[2,3],[3,3])
    cv.movePawn("wp",[1,4],[2,4])
    cv.printBoard()
    print("white queen")
    cv.moveQueen("wq",[0,3],[3,6])
    cv.movePawn("bp",[6,4],[5,4])
    #cv.printBoard()
    print("black queen")
    cv.moveQueen("bq",[7,3],[3,6])
    '''
    cv.movePawn("bp",[6,4],[5,4])
    cv.moveQueen("bq",[7,3],[1,8])
    print()
    cv.printBoard()
if __name__ == "__main__":
    main()