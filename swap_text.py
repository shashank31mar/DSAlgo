# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def swap(text,i,j):
    if i == j:
        return text
    lst = list(text)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)
    
def reverse_word(text,start,end):
    while start != end and start < end:
        text = swap(text,start,end)
        start += 1
        end -= 1
    return text

def reverse_text(text):
    start = 0
    end = 0
    
    for i , c in enumerate(text):
        if c != ' ' and i != len(text)-1:
            end = i
        elif i == len(text)-1:
            text = reverse_word(text,start,end+1)
        else:
            text = reverse_word(text,start,end)
            start = i+1 
    return text

def main():
    print("Reverse string is : " , reverse_text(input("Enter Text: ")))
    
if __name__ == "__main__":
    main()