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
#   standard regression :  ws = xTx*(XT*Y)
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

#
#   local weighted linear regression : ws = xT*weights*x*(xT*weights*Y)
#
def lwlRegres(testPoint, xArr, yArr, k=1.0):
    '''
    :param testPoint:   test samples data
    :param xArr:        input data Matrix x, data;
    :param yArr:        input data Matrix y, label;
    :param k:           weighted parameters of gauss model
    :return:            testPoint * ws
    '''
    xMat = mat(xArr); yMat = mat(yArr).T
    m = shape(xMat)[0]
    weights = mat(eye(m))
    for j in range(m):
        diffMat = testPoint - xMat[j,:]
        weights = exp(diffMat*diffMat.T/(-2.0*k**2))
    xTx = xMat.T * (weights * xMat)

    if linalg.det(xTx) == 0.0:
        print "This matrix is singular, cannot be inverse"
        return
    ws = xTx.T * (xMat.T * (weights * yMat))
    return testPoint*ws

def lwlrTest(testArr, xArr, yArr, k=1.0):
    m = shape(testArr) [0]
    yHat = zeros(m)
    for i in range(m):
        yHat = lwlRegres(testArr[i], xArr, yArr, k)
    return yHat

#
#   ridge regression: ws = (xTx + lamda*I)* xT * Y
#
def ridgeRegres(xMat, yMat, lamda=0.2):
    xTx = xMat.T*xMat
    denom = xTx + eye(shape(xMat) [1])*lamda
    if linalg.det(denom) == 0:
        print "This matrix is singular, cannot be inverse"
        return
    ws = denom.I * (xMat.T*yMat)
    return ws

def ridgeRegresTest(xArr, yArr):
    '''
    :param xArr:    input data x Matrix
    :param yArr:    input data y Matrix (labels)
    :return:        use 30 different lamda for ridge regression, to test different effect.
    '''
    xMat = mat(xArr); yMat = mat(yArr)
    yMean = mean(yMat, 0)
    yMat = yMat - yMean
    xMean = mean(xMat, 0)
    xVar = var(xMat, 0)
    xMat = (xMat - xMean)/xVar
    numTestPts = 30
    wMat = zeros((numTestPts, shape(xMat) [1]))

    for i in range(numTestPts):
        ws = ridgeRegres(xMat, yMat, exp(i-10))
        wMat[i, :] = ws.T

    return wMat