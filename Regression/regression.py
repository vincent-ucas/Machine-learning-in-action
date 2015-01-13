##  Regression: standard regression for linear model
#   $author: Ming
#   $date:   Jan.13 2015
#
###########################################

from numpy import *

def loadDataSet(filename):
    '''
    :param filename: input a database contains samples data, while the last data of each line is label
    :return:         data Matrix and label Matrix
    '''
    numFeat = len(open(filename).readline().split('\t')) - 1
    dataMat = []; labelMat = []
    fr = open(filename)
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat, labelMat

#
def stdRegres(xArr, yArr):
    '''
    :param xArr, yArr:    input data Matrix and Label Matrix as (xArr, yArr)
    :return:              using standard regression (Ordinary least squares) for computing the weight matrix ws
    '''
    xMat = mat(xArr); yMat = mat(yArr).T
    xTx = xMat.T*xMat
    if linalg.det(xTx) == 0.0:
        print "This matrix is singular, cannot do inverse"
        return
    ws = xTx.I * (xMat.T*yMat)
    return ws