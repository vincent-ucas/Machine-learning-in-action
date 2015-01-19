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

# ====== split the whole text by using re. module =====
def textParse(text_str):
    import re
    list_of_tokens = re.split(r'\W*', text_str)
    return [tok.lower() for tok in list_of_tokens if len(tok) > 2]

# ====== create a vocabulary list from an input dataSet ======
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

# ===== turn words into vector 'bag-of-word (BOW) model' ========
# bag-of-word model add up the frequency of each word instead of set the index to 1

def bagOfWords2Vect(vocab_list, input_set):
    ret_vector = [0]*len(vocab_list)
    for word in input_set:
        if word in vocab_list:
            ret_vector[vocab_list.index(word)] += 1
    return ret_vector

'''
# ===== training Bayes classifier ============
# Param:  trainMatrix:   consist of different kinds of documents
          trainCategory: category of different files
  Return: classes prob. vector & P(ci)

  this training module of Naive Bayes is used for 2 class, P(class = 1)=P(1); P(class=0)=P(0)..
  the same as multi-class. In the case of multi-class, return list p_vect = [[xxx], [xxx], ..., [xxx]]
# ============================================
'''
def trainNaiveBayes(train_matrix, train_category):
    num_docs = len(train_matrix)
    num_words = len(train_matrix[0])

    pInsult = sum(train_category)/float(num_docs)   # insulted(or abusive) words docs rate in all of docs.
    p0_num = ones(num_words)
    p1_num = ones(num_words)
    p0_norm = 2.0; p1_norm = 2.0

    # for each docs, accumulate each class words vector probability
    for i in range(num_docs):
        if train_category[i] == 1:          # class 1: insulted
            p1_num += train_matrix[i]
            p1_norm += sum(train_matrix[i])
        else:                               # class 0: regular
            p0_num += train_matrix[i]
            p0_norm += sum(train_matrix[i])
    p1_vect = log(p1_num/p1_norm)
    p0_vect = log(p0_num/p0_norm)
    return p0_vect, p1_vect, pInsult

# ======= classify training module of Navie Bayes ===============
def classifyNaiveBayes(vec2classify, p0_vect, p1_vect, p_class1):
    p1_temp = vec2classify*p1_vect
    p0_temp = vec2classify*p0_vect
    p1 = sum(p1_temp) + log(p_class1)
    p0 = sum(p0_temp) + log(1.0-p_class1)

    if p1 > p0:
        return 1
    else:
        return 0

#
# ======= RSS source classifier =====================
#
def calcMostFreq(vocab_list, full_text):
    import operator
    freq_dict = {}
    for token in vocab_list:
        freq_dict[token] = full_text.count[token]

    sorted_freq = sorted(freq_dict.iteritems(), key = operator.itemgetter(1), reversed = True)
    return sorted_freq[:30]

def localWord(feed1, feed2):
    import feedparser
    doc_list = []; class_list = []; full_text = []
    minLength = min(len(feed1['entries']), len(feed0['entries']))

    for i in range(minLength):
        # feedparser 1
        word_list = textParse(feed1['entries'][i]['summary'])
        doc_list.append(word_list)
        full_text.extend(word_list)
        class_list.append(1)

        # feedparser 2
        word_list = textParse(feed0['entries'][i]['summary'])
        doc_list.append(word_list)
        full_text.extend(word_list)
        class_list.append(0)

    vocab_list = createVocabList(doc_list)
    top_word30 = calcMostFreq(vocab_list, full_text)

    # remove the most frequency words
    for pair_word in top_word30:
        if pair_word[0] in vocab_list:
            vocab_list.remove(pair_word[0])

    # training: extract 20 samples for testing randomly
    training_set = range(2*minLength); test_set = []
    for i in range(20):
        rand_idx = int(random.uniform(0, len(training_set)))
        test_set.append(training_set[idx])
    trainMat = []; train_classes = []
    for idx in training_set:
        trainMat.append(bagOfWords2Vect(vocab_list, doc_list[idx]))
        train_classes.append(class_list[idx])
    p0_vect, p1_vect, p_ab = trainNaiveBayes(trainMat, train_classes)

    # testing
    error_cnt = 0
    for idx in test_set:
        word_vect = bagOfWords2Vect(vocab_list, doc_list[idx])
        if classifyNaiveBayes(word_vect, p0_vect, p1_vect, p_ab) != class_list[idx]:
            error_cnt += 1
    print 'the Error: ', float(error_cnt)/len(test_set)

    return vocab_list, p0_vect, p1_vect
