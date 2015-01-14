import kNN2, kNN
import matplotlib
import matplotlib.pyplot as plt
from numpy import *

def kNN_test():
    kNN2.testHandWritingClass()

def dataAnalyzing():
    # open a data file 'datingTestSet.txt'
    datingDataMat, datingDataLabel = kNN.file2matrix('datingTestSet2.txt')
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(datingDataMat[:, 0], datingDataMat[:, 1],
               15.0*array(datingDataLabel), 15.0*array(datingDataLabel))
    plt.show()


if __name__ == '__main__' : dataAnalyzing()