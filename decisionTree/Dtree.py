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
        if curLabel not in labelsCount.keys():      #
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
            reducedDataVec = featVec[:axis]
            reducedDataVec.extend(featVec[axis+1:])
            retDataSet.append(reducedDataVec)

    return retDataSet

# ======= select the best feature for spliting ===========================
# =====  according to :   best Gain Info: g(D,A) = H(D) - H(D|A)  ========

def selectBestFeat(dataSet):
     numFeat = len(dataSet[0])-1
     baseEntropy = calShannonEnt(dataSet)
     bestGainInfo = 0.0; bestFeatId = -1

     for i in range(numFeat):
         dataList = [data[i] for data in dataSet]   # get the unique data set
         uniqueData = set(dataList)                 # set(): can return the unique data of any data sets
         conEntropy = 0.0

         # calculate the conditional entropy: H(D|A), for each unique feature..
         for value in uniqueData:
             subDataSet = splitFeatData(dataSet, i, value)
             prob = len(subDataSet)/float(len(dataSet))
             conEntropy += prob * calShannonEnt(subDataSet)

         # get the best gain information for the best feature to choose.
         gainInfo = baseEntropy - conEntropy
         if (gainInfo > bestGainInfo):
             bestGainInfo = gainInfo
             bestFeatId = i

     return bestFeatId





