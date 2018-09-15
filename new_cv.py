#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 12:30:53 2018

@author: shashankgupta
"""
WHITE = "white"
BLACK = "black"
class Piece:
    def __init__(self,color,name):
        self.color = color
        self.pos = None
        self.name = name
    def name(self):
        return self.name
    def Color(self):
        return self.color
    
    def isInBound(self,x,y):
        if (x < 8 or x>=0) and (y<8 or y>=0):
            return True
        return False
    
    def move(self,r,c,board,color,moves):
        for (x,y) in moves:
            xt,yt = r+x,c+y
            answer = []
            while self.isInBounds(xt,yt):
                target = board[xt][yt]
                if not target:
                    answer.append((xt,yt))
                elif target.color != color:
                    answer.append((xt,yt))
                    break
                else:
                    break
                xt,yt = xt+x,yt+y
        return answer
    
class Pawn(Piece):
    def __init__(self,color,name,direction):
        self.color = color
        self.name = name
        self.direction = direction
    def move(self,element,start,end):
        '''
        curr_r, curr_c = start[0],start[1]
        end_r, end_c = end[0],end[1]
        if end_r > self.r or end_r < 0 or end_c > self.c or end_c < 0 or abs(end_r-curr_r) != 1:
            print("!ERROR: Invalid {} Pawn Move".format(element[0])) 
            return
        
        if (not self.board[end_r][end_c] or self.capture(element,end_r,end_c)):
            self.board[curr_r][curr_c] = None
            self.board[end_r][end_c] = Piece(element[0],element[1])
            self.curr_pos_r = end_r
            self.cur_pos_c = end_c
        else:
            print("!!Error: Invalid {} Pawn Move!".format(self.colorMap[element[0]]))
            return
        '''

class Knight(Piece):
    def move(self,element,start,end):
        '''
        curr_r, curr_c = start[0],start[1]
        end_r, end_c = end[0],end[1]
        
        if end_r > self.r or end_r < 0 or end_c < 0 or end_c > self.c:
            print("!ERROR: Invalid Horse Move") 
            return
        
        if (abs(end_r-curr_r) == 2 and abs(end_c-curr_c) == 1) or (abs(end_r-curr_r) == 1 and abs(end_c-curr_c) == 2):
            if not self.board[end_r][end_c]:
                self.board[curr_r][curr_c] = None
                self.board[end_r][end_c] = Piece(element[0],element[1])
            elif self.capture(element,end_r,end_c):
                self.board[curr_r][curr_c] = None
                self.board[end_r][end_c] = Piece(element[0],element[1])
            else:
                print("!!ERROR: Invalid Horse Move")
                return
        else:
            print("ERROR: Invalid Horse Move")
            return
        '''
        
class Queen(Piece):
    def move(self,element,start,end):
        '''
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
            self.board[end_r][end_c] = Piece(element[0],element[1])
        elif end_r == curr_r:
            while j != end_c+1:
                print("j is ", j)
                if not self.board[end_r][j] or self.board[end_r][j].name() == element or self.capture(element,end_r,j):
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
            self.board[end_r][end_c] = Piece(element[0],element[1])
        else:
            while i != end_r and j != end_c:
                #print("i,j",i,j)
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
            self.board[end_r][end_c] = Piece(element[0],element[1])
        '''

class Rook(Piece):
    def move():
        pass
    
class Bishop(Piece):
    def move():
        pass
    
class King(Piece):
    def move():
        pass
    
class ChessValidator:
    def __init__(self,r=8,c=8):
        self.r = r
        self.c = c
        self.board = [[None]*c for i in range(r)]
        self.uniDict = {WHITE : {Pawn : "♙", Rook : "♖", Knight : "♘", Bishop : "♗", King : "♔", Queen : "♕" }, BLACK : {Pawn : "♟", Rook : "♜", Knight : "♞", Bishop : "♝", King : "♚", Queen : "♛" }}
        self.placers = [Rook,Knight,Bishop,Queen,King,Bishop,Knight,Rook]
        self.initializeState()
        
    def initializeState(self):
        for col in range(self.c):
            self.board[1][col] = Pawn(WHITE,self.uniDict[WHITE][Pawn],1)
            self.board[6][col] = Pawn(BLACK,self.uniDict[BLACK][Pawn],-1)
            
            self.board[0][col] = self.placers[col](WHITE,self.uniDict[WHITE][self.placers[col]])
            self.board[7][self.c-1-col] = self.placers[col](BLACK,self.uniDict[BLACK][self.placers[col]])
       
    def capture(self,element,r,c):
        ele_c = element[0]
        curr_ele = self.board[r][c]
        if curr_ele and curr_ele.Color() != ele_c:
            print("Capturing element : {}".format(curr_ele.name()))
            return True
        return False
            
    def moves(self):
        '''
        p.move("wp",[1,0],[2,0])
        p.move("wp",[2,0],[3,0])]
        #p.move("wp",[3,0],[2,0])
        p.move("bp",[6,0],[5,0])
        p.move("wp",[3,0],[2,0])
        '''
        #k.move("wh",[0,1],[2,2])
        #k.move("wh",[2,2],[4,1])
        #k.move("wh",[4,1],[6,2])
        #k.move("bh",[5,0],[3,1])
        #p.move("wp",[1,4],[2,4])
        '''
        #q.move("wq",[0,3],[3,6])
        p.move("wp",[1,3],[2,3])
        q.move("wq",[0,3],[2,3])
        #p.move("bp",[6,4],[5,4])
        #q.move("bq",[7,3],[1,8])'''
        pass
    
    def printBoard(self):
        for i in range(self.r):
            for j in range(self.c):
                if self.board[i][j]:
                    print(self.board[i][j].name, end= " ")
                else:
                    print("-",end = " " )
            print()

def main():
    cv = ChessValidator()
    cv.printBoard()
    #cv.moves()
    
if __name__ == "__main__":
    main()