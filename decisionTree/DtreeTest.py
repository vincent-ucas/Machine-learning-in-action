"""
    $author:      Ming
    $date:        2015/01/16
    $Description: Testing for decision tree classifier.
"""

import Dtree
import treePlotter

def test1():
    # load data to create decision tree
    dataSet, labels= Dtree.createDataSet()
    decision_tree = Dtree.createDtree(dataSet, labels)

    # plot tree
    treePlotter.plotDecisionTree(decision_tree)

    # classify
    dataSet, labels= Dtree.createDataSet()
    print Dtree.classify(decision_tree, labels, [1, 0])
    print Dtree.classify(decision_tree, labels, [1, 1])

    # store
    Dtree.storeTree(decision_tree, 'classifierStorage_DTree.txt')
    Dtree.grabTree('classifierStorage_DTree.txt')


def test2():
    fr = open('lenses.txt')
    lenses = [inst.strip().split('\t') for inst in fr.readlines()]
    lenses_labels = ['age', 'prescript', 'astigmatic', 'tearRate']
    lenses_tree = Dtree.createDtree(lenses, lenses_labels)

    print lenses_tree
    treePlotter.plotDecisionTree(lenses_tree)


if __name__ == '__main__' : test2()