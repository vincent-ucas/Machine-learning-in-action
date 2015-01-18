"""
    $author:      Ming
    $date:        2015/01/18
    $Description: Bayes Estimation, a wonderful classifier based on probability theory.
"""

from numpy import *

def loadDataSet():
    post_list = [
        ['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
        ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
        ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
        ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
        ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
        ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']
    ]
    class_vec = [0, 1, 0, 1, 0, 1]  # 1 means insulting words, 0 means regular words
    return post_list, class_vec

def createVocabList(dataSet):
    vocab_set = set([])
    for vocab in dataSet:
        vocab_set = vocab_set | set(vocab)  # return unique vocabulary set
    return list(vocab_set)

# ===== turn words into vector ============
# if the word appears in inputSet, the accordingly index of return_vector will be 1, otherwise, 0

def words2Vec(vocab_list, input_set):
    ret_vector = [0]*len(vocab_list)
    for word in input_set:
        if word in vocab_list:
            ret_vector[vocab_list.index(word)] = 1
        else:
            print "the word: %s is not in this vocabulary list." % word
    return ret_vector

