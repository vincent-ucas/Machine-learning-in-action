"""
    $author:      Ming
    $date:        2015/01/18
    $Description: Bayes Estimation, a wonderful classifier based on probability theory.
"""
import bayes

data_set, class_labels = bayes.loadDataSet()
vocab_list = bayes.createVocabList(data_set)
vocab_vector = bayes.words2Vec(vocab_list, data_set[0])
print vocab_list
print vocab_vector