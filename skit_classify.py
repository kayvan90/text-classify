#==============================================================================
# imports:
#==============================================================================
import os
from pandas import DataFrame
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.cross_validation import KFold
from sklearn.metrics import confusion_matrix, f1_score, accuracy_score
# mine:
from kayfuncs import *


#==============================================================================
# read file function:
#==============================================================================
NEWLINE = " "
SKIP_FILES = {'cmds'}

def read_files(path):
    for root, dir_names, file_names in os.walk(path, topdown=False):
#        for path in dir_names:
#            read_files(os.path.join(root, path))
        for file_name in file_names:
            if file_name not in SKIP_FILES:
                file_path = os.path.join(root, file_name)
                if os.path.isfile(file_path):
                    lines = []
                    # other encodings can be used here such as: utf-8 & ...
                    f = open(file_path, 'r')
                    for line in f:
                        lines.append(unicode(line, errors='ignore'))
                    f.close()
                    content = NEWLINE.join(lines)
                    yield file_path, content

#==============================================================================
# build data frame from data:
#==============================================================================
def build_data_frame(cls, addr):
    rows  = []
    index = []
    for file_name, text in read_files(addr + cls):
        rows.append({'text': text, 'class': cls})
        index.append(file_name)

    data_frame = DataFrame(rows, index=index)
    return data_frame
    
#==============================================================================
# build data frame from graph data:
#==============================================================================
def build_data_frame_from_text_graph(cls, addr):
    rows  = []
    index = []
    for file_name, text in read_files(addr + cls):
        new_text = graph_analysis(text, 3)
        rows.append({'text': new_text, 'class': cls})
        index.append(file_name)

    data_frame = DataFrame(rows, index=index)
    return data_frame
    


#==============================================================================
# main
#==============================================================================

addr = './data2/'
# all_sources = ['alt.atheism',
# 'comp.graphics',
# 'comp.os.ms-windows.misc',
# 'comp.sys.ibm.pc.hardware',
# 'comp.sys.mac.hardware',
# 'comp.windows.x',
# 'misc.forsale',
# 'rec.autos',
# 'rec.motorcycles',
# 'rec.sport.baseball',
# 'rec.sport.hockey',
# 'sci.crypt',
# 'sci.electronics',
# 'sci.med',
# 'sci.space',
# 'soc.religion.christian',
# 'talk.politics.guns',
# 'talk.politics.mideast',
# 'talk.politics.misc',
# 'talk.religion.misc']
all_sources = ['neg', 'pos']
# load some of the data just in case:
sources = all_sources[0:]


data = DataFrame({'text': [], 'class': []})
for cls in sources:
    # regular approach:
    # data = data.append(build_data_frame(cls, addr))
    # graph based approach:
   data = data.append(build_data_frame_from_text_graph(cls, addr))

data = data.reindex(np.random.permutation(data.index))

count_vectorizer = CountVectorizer()
counts = count_vectorizer.fit_transform(data['text'].values)

# train a classifier:
#ngram_range=(1, 3)

from sklearn import preprocessing

pipeline = Pipeline([
    ('vectorizer',  CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('classifier',  MultinomialNB()) ])
pipeline.fit(data['text'].values, data['class'].values)

# analysis and kfold validation


k_fold = KFold(n=len(data), n_folds=5)
scores = []
accuracy = []
confusion = np.zeros(shape=(len(sources), len(sources)))
for train_indices, test_indices in k_fold:
    print 'a fold is done!'
    train_text = data.iloc[train_indices]['text'].values
    train_y = data.iloc[train_indices]['class'].values

    test_text = data.iloc[test_indices]['text'].values
    test_y = data.iloc[test_indices]['class'].values

    pipeline.fit(train_text, train_y)
    predictions = pipeline.predict(test_text)

    confusion += confusion_matrix(test_y, predictions)
    score = f1_score(test_y, predictions, pos_label='pos')
    scores.append(score)
    accuracy.append(accuracy_score(test_y, predictions))

print('Total classifieds:', len(data))
print('f1_Score:', sum(scores)/len(scores))
print('accuracy:', sum(accuracy)/len(accuracy))
# print('Confusion matrix:')
# print(confusion)




