# -*- coding: utf-8 -*-
"""
Created on Mon May 14 15:54:30 2018

@author: shagupta
"""

def reverse_word(word):
    rev = ''
    for i in range(0,len(word)):
        rev = rev + word[len(word)-1-i]
    return rev
    
def reverse_text(text):
    word = ''
    new_text = ''
    for c in text:
        if c != ' ' or c == '':
            word += c
            print(c)
        else:
            if new_text == ' ':
                new_text = reverse_word(word)
            else:
                new_text = new_text + ' ' + reverse_word(word)
            word = ''
    return new_text

if __name__ == "__main__":
    print(reverse_text(input()))