"""
    $author:      Ming
    $date:        2015/01/18
    $Description: Bayes Estimation, a wonderful classifier based on probability theory.
"""
import bayes
import feedparser
from numpy import *

#
#  application I: judge if there is abusive word.
#
def NB_test1():
    list_post, list_class = bayes.loadDataSet()
    vocab_list = bayes.createVocabList(list_post)
    trainMat = []

    for doc in list_post:
        trainMat.append(bayes.words2Vec(vocab_list, doc))
    p0_vect, p1_vect, p_ab = bayes.trainNaiveBayes(trainMat, array(list_class))

    # testing I
    test_entry = ['love', 'my', 'dalmation']
    vect2classify = array(bayes.words2Vec(vocab_list, test_entry))
    print "classified as: ", bayes.classifyNaiveBayes(vect2classify, p0_vect, p1_vect, p_ab)

    # testing II
    test_entry = ['stupid', 'fuck', 'garbage']
    vect2classify = array(bayes.words2Vec(vocab_list, test_entry))
    print "classified as: ", bayes.classifyNaiveBayes(vect2classify, p0_vect, p1_vect, p_ab)

#
#  application II: filtering spam
#
def NB_test2():
    spamAddr = 'email/spam/'
    hamAddr = 'email/ham/'
    doc_list = []; class_list = []

    # step 1: loading data and create vocabulary list
    for i in range(1, 26):
        word_list = bayes.textParse(open(spamAddr + '%d.txt' % i).read())    # spam
        doc_list.append(word_list)
        class_list.append(1)

        word_list = bayes.textParse(open(hamAddr + '%d.txt' % i).read())     # ham
        doc_list.append(word_list)
        class_list.append(0)

    vocab_list = bayes.createVocabList(doc_list)

    # step 2: extract 10 email randomly for testing, others for training..
    training_set = range(50)
    test_set = []
    for i in range(10):
        rand_idx = int(random.uniform(0, len(training_set)))
        test_set.append(training_set[rand_idx])
        del training_set[rand_idx]

    # training
    trainMat = []; train_classes = []
    for idx in training_set:
        trainMat.append(bayes.words2Vec(vocab_list, doc_list[idx]))
        train_classes.append(class_list[idx])
    p0_vect, p1_vect, p_ab = bayes.trainNaiveBayes(array(trainMat), array(train_classes))

    # step 3: testing..
    error_cnt = 0
    for idx in test_set:
        word_vector = bayes.words2Vec(vocab_list, doc_list[idx])
        if bayes.classifyNaiveBayes(word_vector, p0_vect, p1_vect, p_ab) != class_list[idx]:
            error_cnt += 1

    print 'the Error: ', float(error_cnt)/len(test_set)

#
#   application III: find out the related regional words based on Naive Bayes.
#
def NB_test3():
    import operator
    ny = feedparser.parser('http://newyork.craigslist.org/stp/index.rss')
    sf = feedparser.paser('http://sfbay.craigslist.org/stp/index.rss')
    vocab_list, p0_vect, p1_vect = bayes.localWord(ny, sf)

    topNY = []; topSF = []
    for i in range(len(p0_vect)):
        if p0_vect[i] > -0.6:   topSF.append((vocab_list[i], p0_vect[i]))
        if p1_vect[i] > -0.6:   topNY.append((vocab_list[i], p1_vect[i]))

    sorted_SF = sorted(topSF, key=lambda pair: pair[1], reversed=True)
    print "SF CITY: "
    for item in topSF:
        print item[0]

    sorted_NY = sorted(topNY, key=lambda pair: pair[1], reversed=True)
    print "NY CITY: "
    for item in topNY:
        print item[0]

NB_test3()