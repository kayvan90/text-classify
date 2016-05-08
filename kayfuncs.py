# -*- coding: utf-8 -*-
"""
my functions
@author: k1
"""
#==============================================================================
# imports
#==============================================================================
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.stem.porter import *
import re
import itertools as itr


#==============================================================================
# functions
#==============================================================================
# tokenizer:
stemmer = PorterStemmer()
def tokenizer( text ):
    # 1. Remove HTML
    text = BeautifulSoup(text).get_text() 
    #
    # 2. Remove non-letters        
    letters_only = re.sub("[^a-zA-Z]", " ", text) 
    #
    # 3. Convert to lower case, split into individual words
    words = letters_only.lower().split()                             
    #
    # 4. In Python, searching a set is much faster than searching
    #   a list, so convert the stop words to a set
    stops = set(stopwords.words("english"))                  
    # 
    # 5. Remove stop words and stem the remainings
    meaningful_words = [stemmer.stem(w) for w in words if not w in stops and len(w)>2]   
    #
    # 6. Return
    # return just a list
    return meaningful_words
    # join as a string
#    return( " ".join( meaningful_words ))   
    

#==============================================================================
# repeat word
#==============================================================================
def rep_word(s,n):
    return ' '.join(list(itr.repeat(s, n)))
    
#==============================================================================
# gaph representation of text
#==============================================================================
import networkx as nx
import matplotlib.pyplot as plt
import itertools as itr
def graph_analysis(text, win_size):
    lines_of_new_text = ''
    tokenized_text = tokenizer(text= text)
    word_graph = nx.Graph()
    for wrd in tokenized_text:
        if word_graph.has_edge(wrd, wrd):
            word_graph[wrd][wrd]['weight'] += 1
        else:
            word_graph.add_edge(wrd, wrd, weight=1)
    
    for i in range(len(tokenized_text)-win_size+1):
        word_win = tokenized_text[i: i+win_size]
        combs = list(itr.product(word_win[0:1], word_win[1:]))
        for cmb in combs:
            if word_graph.has_edge(cmb[0], cmb[1]):
                word_graph[cmb[0]][cmb[1]]['weight'] += 1
            else:
                word_graph.add_edge(cmb[0], cmb[1], weight=1)

    for u, v, a in word_graph.edges(data=True):
        lines_of_new_text = " ".join((rep_word(u+v, a['weight']),
                                      lines_of_new_text))
    return lines_of_new_text