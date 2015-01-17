__author__ = 'Vincent HE'
"""
    $author:      Ming
    $date:        2015/01/15
    $Description: Decision Tree for classfiying data.
"""

from math import log
import operator

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

# ======  get the majority counting feature ============
def getMajorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return classCount[0][0]

# ===== create decision tree by recursion =======
def createDtree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):     # no more class
        return classList[0]
    if len(dataSet[0]) == 1:                                # get majority count class
        return getMajorityCnt(classList)

    bestFeat = selectBestFeat(dataSet)
    bestFeatLabel = labels[bestFeat]
    ret_tree = {bestFeatLabel:{}}
    del(labels[bestFeat])

    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        ret_tree[bestFeatLabel][value] = createDtree(splitFeatData(dataSet, bestFeat, value), subLabels)

    return ret_tree

# ====== using decision tree classifier =======
def classify(input_tree, feat_labels, test_vec):
    node_str = input_tree.keys()[0]
    sub_dict = input_tree[node_str]
    feat_idx = feat_labels.index(node_str)

    for key in sub_dict.keys():
        if test_vec[feat_idx] == key:
            if type(sub_dict[key]).__name__ == 'dict':
                ret_label = classify(sub_dict[key], feat_labels, test_vec)
            else:
                ret_label = sub_dict[key]
    return ret_label

# ===== store decision tree: using pickle module ========
def storeTree(input_tree, filename):
    import pickle
    fw = open(filename, 'w')
    pickle.dump(input_tree, fw)
    fw.close()

# ==== load a file and grab decision tree ======
def grabTree(filename):
    import pickle
    fr = open(filename)
    return pickle.load(fr)
