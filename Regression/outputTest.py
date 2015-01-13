import regression
import matplotlib.pyplot as plt
from numpy import *

def stdRegressionTest():
    xArr, yArr = regression.loadDataSet('ex0.txt')
    ws = regression.stdRegres(xArr, yArr)
    xMat = mat(xArr)
    yMat = mat(yArr)
    yHat = xMat * ws

    # draw figure
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xMat[:,1].flatten().A[0], yMat.T[:,0].flatten().A[0])

    xCopy = xMat.copy()
    xCopy.sort(0)
    yHat = xCopy*ws
    ax.plot(xCopy[:,1], yHat)
    plt.show()

    print corrcoef(yHat.T, yMat)

def ridgeRegressionTest():
    datX, datY = regression.loadDataSet('abalone.txt')
    ridgeWsMat = regression.ridgeRegresTest(datX, datY)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(ridgeWsMat)
    plt.show()

if __name__ == '__main__' : ridgeRegressionTest()
