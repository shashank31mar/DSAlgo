#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 20:51:00 2018

@author: shashankgupta
"""

from collections import Counter
import re
import math

FILE_PATH = ['files/big.txt','files/big1.txt']
FILE_PATH1 = ['files/tsElliot.txt']
class TFIDF:
    def __init__(self,texts):
        self.allDocs = []
        self.get_all_docs(texts)
        self.term_freq_doc()
        
    def words(self,text):
        """ Convert all words to lower case """
        return re.findall(r'\w+', text.lower())
    
    def get_all_docs(self,texts):
        self.allDocs = [Counter(self.words(open(text).read())) for text in texts]
    
    def term_freq(self,term):
        #self.get_all_docs(texts)
        term_freq_vec = []
        for doc in self.allDocs:
            if term in doc:
                term_freq_vec.append(doc[term])

        return term_freq_vec
            
    def term_freq_doc(self):
        """ Normalizing all docs """
        for doc_dict in self.allDocs:
            factor = sum(doc_dict.values(),0.0)
            for x in doc_dict:
                doc_dict[x] /= factor
       
    def inverse_doc_freq(self,term):
        numOfDocWithThisTerm = 0
        #print(len(self.allDocs))
        for doc in self.allDocs:
            if doc[term.lower()]:
                numOfDocWithThisTerm += 1
        #print(numOfDocWithThisTerm)
        if numOfDocWithThisTerm > 0:
            return 1.0 + math.log(float(len(self.allDocs))/numOfDocWithThisTerm)
        else:
            #print("here")
            return 1.0

    def tfidf(self,term):
        term_freq_vec = self.term_freq(term)
        idf = self.inverse_doc_freq(term)
        #print(term_freq_vec)
        #print(idf)
        tfidf_term = [x*idf for x in term_freq_vec]
        return tfidf_term
    
    def cosine_similarity(self,query):
        doc = self.allDocs[0]
        for x in query:
            query[x] = math.pow(query[x],2)
        for x in doc:
            doc[x] = math.pow(doc[x],2)
            
        query_mod = math.sqrt(sum(query.values()))
        doc_mod = math.sqrt(sum(doc.values()))
        
        
        return self.dot_product(query,doc)/(query_mod * doc_mod)
    
    def dot_product(self,query,doc):
        product = []
        for x in query:
            if x in doc:
                product.append(query[x] * doc[x])
        
        return sum(product)
    
    def get_feature_vec(self,text):
        doc = Counter(self.words(open(text).read()))
        feature_vec = []
        for x in doc:
            feature_vec.append(self.tfidf(x))
        return feature_vec
    
def main():
    tfidf = TFIDF(FILE_PATH)
    #doc_dict = tfidf.get_all_docs(FILE_PATH1)[0]
    print(tfidf.get_feature_vec(FILE_PATH1[0]))
    
if __name__ == "__main__":
    main()