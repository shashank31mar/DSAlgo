#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 20:29:05 2018

@author: shashankgupta
"""

import re
from collections import Counter

def words(text):
    """ Convert all words to lower case """
    return re.findall(r'\w+', text.lower())

# =============================================================================
# Read words from a file
# =============================================================================
WORDS_DICT = Counter(words(open('files/big.txt').read()))


def edits1(word):
    """ Calculates edits that are 1 distances """
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


def main():
    """ main function """
    print(WORDS_DICT.most_common(10))

if __name__ == "__main__":
    main()
