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

# dating classfying test with kNN

def datingClassTest():
    testRatio = 0.10    # extract 10% data for testing, others for training
    datingDataMat, datingLabels = kNN.file2matrix('datingTestSet2.txt')
    normMat, ranges, minVal = kNN.autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTest = int(m * testRatio)
    errorCount = 0.0

    for i in range(numTest):
        classifierResult = kNN.kNNClassify(normMat[i, :], normMat[numTest:m, :], datingLabels[numTest:m], 3)
        print "classify: %d, the real classify is: %d" % (classifierResult, datingLabels[i])
        if classifierResult != datingLabels[i]: errorCount += 1.0

    print "Total error rate is %f" % (errorCount/float(numTest))


if __name__ == '__main__' : datingClassTest()