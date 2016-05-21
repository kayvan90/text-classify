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
import operator
from collections import Counter
import math

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
#    deg = nx.degree_centrality(word_graph)
#    clns = nx.closeness_centrality(word_graph)
    return lines_of_new_text#, deg, clns
    
# path analysis:
def path_analysis(text, win_size):
    lines_of_new_text = ''
    tokenized_text = tokenizer(text= text)
    word_graph = nx.DiGraph()
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

#    for u, v, a in word_graph.edges(data=True):
#        lines_of_new_text = " ".join((rep_word(u+v, a['weight']),
#                                      lines_of_new_text))
    deg  = nx.degree_centrality(word_graph)
    clns = nx.closeness_centrality(word_graph)
    deg_cen = dict(Counter(deg) + Counter(clns))
    s_deg_cen = sorted(deg_cen.items(), key=operator.itemgetter(1), reverse=True)
    tops = s_deg_cen[0:int(math.ceil(len(word_graph)*.2))]
    for t in tops:
#        print "<<=====================>>", t[0]
        sh_path = nx.shortest_path(word_graph, target=t[0])
        for sh_p in sh_path:
            if len(sh_path[sh_p]) == 1:
                lines_of_new_text = " ".join((sh_path[sh_p][0]+sh_path[sh_p][0],
                                             lines_of_new_text))
#            print 'inline:'
            for idx in range(len(sh_path[sh_p])-1):
#                print sh_path[sh_p][idx:idx+2]
                lines_of_new_text = " ".join((sh_path[sh_p][idx]+sh_path[sh_p][idx+1],
                                             lines_of_new_text))
            
#    nx.draw(word_graph, with_labels = True)
#    plt.show()
    return lines_of_new_text