#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 20:29:05 2018

@author: shashankgupta
http://norvig.com/spell-correct.html
"""

import re
from collections import Counter

def words(text):
    """ Convert all words to lower case """
    return re.findall(r'\w+', text.lower())

# =============================================================================
# Read words from a file
# =============================================================================
WORDS_DICT = Counter(words(open('big1.txt').read()))
#WORDS_DICT1 = Counter(words(open('big1.txt').read()))

def prob(word, n=sum(WORDS_DICT.values())):
    """ Calculates probability of each word occurring in the dictionary """
    return WORDS_DICT[word]/n

# =============================================================================
# I defined a trivial, flawed error model that says all known words of edit 
# distance 1 are infinitely more probable than known words of edit distance 2, 
# and infinitely less probable than a known word of edit distance 0. 
# So we can make candidates(word) produce the first non-empty list of 
# candidates in order of priority:

#    • The original word, if it is known; otherwise
#    • The list of known words at edit distance one away, if there are any; otherwise
#    • The list of known words at edit distance two away, if there are any; otherwise
#    • The original word, even though it is not known. 

# Then we don't need to multiply by a P(w|c) factor, because every candidate 
# at the chosen priority will have the same probability (according to our 
# flawed model)
# =============================================================================

def correction(word):
    """ Most Probable Spelling correction for a word """
    return max(candidates(word),key=prob)

def candidates(word):
    word = word.lower()
    """ Generate possible spelling correction for the word.\n
        Order Assumption:\n
        • The original word, if it is known; otherwise
        • The list of known words at edit distance one away, if there are any; otherwise
        • The list of known words at edit distance two away, if there are any; otherwise
        • The original word, even though it is not known.
    """
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])
    
def known(words_list):
    """ Checks what words are there in dictionary """
    return list(set(w for w in words_list if w in WORDS_DICT))

def edits1(word):
    """ Calculates edits that are 1 distances.\n
        Candidate Model: First a new concept:\n
        ∙ A simple edit to a word is a deletion (remove one letter), \n
        ∙ A transposition (swap two adjacent letters), \n
        ∙ A replacement (change one letter to another) or\n
        ∙ An insertion (add a letter). \n
        The function edits1 returns a set of all the edited strings
        (whether words or not) that can be made with one simple edit.
    """
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word)+1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[1:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]

    return set(deletes+transposes+replaces+inserts)

def edits2(word):
    """ Calculates edits that are 2 distances """
    return [e2 for e1 in edits1(word) for e2 in edits1(e1)]

def edits3(word):
    return [e3 for e2 in edits2(word) for e3 in edits2(e2)]

def main():
    """ main function """
    words = ["eting","chankat","chutiya","chapet","choopachoos"]
    for word in words:
        print("Suggestion for : {} is : {}".format(word,correction(word)))

if __name__ == "__main__":
    main()
