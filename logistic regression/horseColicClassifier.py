"""
    $author:      Ming
    $date:        2015/01/20
    $Description: horse Colic forecast through logistic regression classifier
"""
import logistic
from numpy import *

def LR_classify(in_x, weights):
    prob = logistic.sigmoid(sum(in_x*weights))
    if prob > 0.5:
        return 1
    else:
        return 0

def horseClolicTest():
    fr_train = open('horseColicTraining.txt')
    fr_test = open('horseColicTest.txt')

    # load training data
    training_set = []; training_labels = []
    for line in fr_train.readlines():
        data_line = line.strip().split('\t')
        data_arr = []
        data_num = len(data_line) - 1
        for i in range(data_num):
            data_arr.append(float(data_line[i]))
        training_set.append(data_arr)
        training_labels.append(float(data_line[data_num]))

    # get weigths by logistic regression by random gradient ascent
    training_weights = logistic.stocGradAscent(array(training_set), training_labels)

    # add up error classification
    err_cnt = 0; num_test = 0.0
    for line in fr_test.readlines():
        num_test += 1
        data_line = line.strip().split('\t')
        data_arr = []
        data_num = len(data_line) - 1
        for i in range(data_num):
            data_arr.append(float(data_line[i]))
        if int(LR_classify(array(data_arr), training_weights)) != int(data_line[data_num]):
            err_cnt += 1

    # Error rate
    err_rate = float(err_cnt)/num_test

    print "the Error rate: ", err_rate

    return err_rate

horseClolicTest()