"""
    $author:      Ming
    $date:        2015/01/16
    $Description: Testing for decision tree classifier.
"""

import Dtree
import treePlotter

dataSet, labels= Dtree.createDataSet()
decision_tree = Dtree.createDtree(dataSet, labels)
treePlotter.plotDecisionTree(decision_tree)

