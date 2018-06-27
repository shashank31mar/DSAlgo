# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 09:25:10 2018

@author: shagupta
"""

def convertToPolishNotation(expression):
    stack = []
    for val in expression.split(' '):
        print(val)
        if val in ['-', '+', '*', '/']:
            op1 = stack.pop()
            op2 = stack.pop()
            if val=='-': result = op2 - op1
            if val=='+': result = op2 + op1
            if val=='*': result = op2 * op1
            if val=='/': result = op2 / op1
            stack.append(result)
        else:
            stack.append(float(val))
 
    return int(stack.pop())

def main():
    s = "5 1 2 + 4 * + 3 -"
    print(convertToPolishNotation(s))
    
if __name__ == "__main__":
    main()