__author__ = 'Vincent HE'
"""
    $author:      Ming
    $date:        2015/01/15
    $Description: Decision Tree for classfiying data.
"""

from math import log

def createDataSet():
    dataSet = [
        [1, 1, 'yes'],
        [1, 1, 'yes'],
        [1, 0, 'no'],
        [0, 1, 'no'],
        [0, 1, 'no']
    ]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels

# ======= calculate the shannon entropy  ===========
def calShannonEnt(dataSet):
    numData = len(dataSet)
    labelsCount = {}        # create a dictionary
    for featVec in dataSet:
        curLabel = featVec[-1]
        if curLabel not in labelsCount.keys():
            labelsCount[curLabel] = 0
        labelsCount[curLabel] += 1
    shannonEnt = 0.0
    for key in labelsCount:
        prob = float(labelsCount[key])/numData
        shannonEnt -= prob*log(prob, 2)     # entropy computing: H(D)= -p*log(p)
    return shannonEnt

# ======= split feature ================
def splitFeatData(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedDataSet = dataSet[:axis]
            reducedDataSet.extend(dataSet[axis+1:])
            retDataSet.append(reducedDataSet)

    return retDataSet

# ======= select the best feature for spliting ==========
# according to :   best Gain Info: g(D,A) = H(D) - H(D|A)

def selectBestFeat(dataSet):
     numFeat = len(dataSet[0])-1
     baseEntropy = calShannonEnt(dataSet)
     bestGainInfo = 0.0; bestFeatId = -1



