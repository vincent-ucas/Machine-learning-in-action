"""
    $author:      Ming
    $date:        2015/01/16
    $Description: Testing for decision tree classifier.
"""

import Dtree
import treePlotter

# load data to create decision tree
dataSet, labels= Dtree.createDataSet()
decision_tree = Dtree.createDtree(dataSet, labels)

# plot tree
treePlotter.plotDecisionTree(decision_tree)

# classify
dataSet, labels= Dtree.createDataSet()
print Dtree.classify(decision_tree, labels, [1, 0])
print Dtree.classify(decision_tree, labels, [1, 1])

