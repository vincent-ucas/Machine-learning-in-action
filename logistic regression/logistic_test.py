import logistic
from numpy import *

data_mat, label_mat = logistic.loadData('testSet.txt')
weights = logistic.stocGradAscent(array(data_mat), label_mat)
logistic.plotBestFit(data_mat, label_mat, weights)

