__author__ = 'Vincent HE'
"""
    $author:      Ming
    $date:        2015/01/16
    $Description: Testing for decision tree classifier.
"""

import Dtree

dataSet, labels= Dtree.createDataSet()
#Dtree.calShannonEnt(dataSet)
print Dtree.selectBestFeat(dataSet)
print dataSet