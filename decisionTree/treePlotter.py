"""
    $author:      Ming
    $date:        2015/01/17
    $Description: Graph plotting of decision tree, using matplotlib.pyplot
"""

import matplotlib.pyplot as plt

#   defination of box style of nodes and arrow style.
decision_node = dict(boxstyle = "sawtooth", fc = "0.8")
leaf_node = dict(boxstyle = "round4", fc = "0.8")
arrow_args = dict(arrowstyle = "<-")

'''
# ======== annotate Parameters ==========
#   more details can be found:
#   http://matplotlib.org/api/axes_api.html?highlight=annotate#matplotlib.axes.Axes.annotate
#
#   xy: (x, y)  position of element to annotate
#   xytext:     optional, default: None, position of labels
#   textcoords: string, optional, default: data
#   arrowprops: Dictionary of line properties for the arrow that connects the annotation to the point.
# =======================================
'''

def plotNode(node_text, center_pt, parent_pt, node_type):
    createPlot.ax1.annotate(node_text, xy = parent_pt,
                            xycoords = 'axes fraction', xytext = center_pt,
                            textcoords = 'axes fraction', va = "center", ha = "center",
                            bbox = node_type, arrowprops = arrow_args)

# =====  create a simple plot for drawing leaf node and decision node ========
def createPlot():
    fig = plt.figure(1, facecolor = 'white')
    fig.clf()
    createPlot.ax1 = plt.subplot(111, frameon=False)
    plotNode('Decision Node', (0.5, 0.1), (0.1, 0.5), decision_node)
    plotNode('Leaf Node', (0.8, 0.1), (0.3, 0.8), leaf_node)

    plt.show()

# ====== get the number of leaf nodes to determinate the length of X coords ====
def getNumLeafs(decision_tree):
    num_leafs = 0
    node_str = decision_tree.keys()[0]
    sub_dict = decision_tree[node_str]

    for key in sub_dict.keys():
        if type(sub_dict[key]).__name__ == 'dict':
            num_leafs += getNumLeafs(sub_dict[key])
        else:
            num_leafs += 1
    return num_leafs

# ===== get the depth of decision tree =====
def getTreeDepth(decision_tree):
    max_depth = 0
    node_str = decision_tree.keys()[0]
    sub_dict = decision_tree[node_str]

    for key in sub_dict.keys():
        if type(sub_dict[key]).__name__ == 'dict':
            this_depth = getTreeDepth(sub_dict[key]) + 1
        else:
            this_depth = 1
        if (this_depth > max_depth):
            max_depth = this_depth

    return max_depth

#
# =======  Graphic plot:  decision tree ======
#
def plotTextBetweenNodes(center_pt, parent_pt, text_str):
    x_mid = (parent_pt[0] - center_pt[0])/2.0 + center_pt[0]
    y_mid = (parent_pt[1] - center_pt[1])/2.0 + center_pt[1]
    createPlot.ax1.text(x_mid, y_mid, text_str)     # plot text string between parent nodes and center nodes.

def plotTree(decision_tree, parent_pt, node_text):

    # paramemters of the decision tree
    num_leafs = getNumLeafs(decision_tree)
    depth = getTreeDepth(decision_tree)

    node_str = decision_tree.keys()[0]
    sub_dict = decision_tree[node_str]

    # get the center point of this decison tree..
    center_pt = (plotTree.xOff + (1.0 + float(num_leafs))/2.0/plotTree.totalW, plotTree.yOff)
    plotTextBetweenNodes(center_pt, parent_pt, node_text)

    # plot the root node of this tree
    plotNode(node_str, center_pt, parent_pt, decision_node)
    plotTree.yOff = plotTree.yOff - 1.0/plotTree.totalD

    for key in sub_dict.keys():
        if type(sub_dict[key]).__name__ == 'dict':
            plotTree(sub_dict[key], center_pt, str(key))
        else:
            plotTree.xOff = plotTree.xOff + 1.0/plotTree.totalW
            plotNode(sub_dict[key], (plotTree.xOff, plotTree.yOff), center_pt, leaf_node)   # plot the tree node
            plotTextBetweenNodes((plotTree.xOff, plotTree.yOff), center_pt, str(key))
    plotTree.yOff = plotTree.yOff + 1.0/plotTree.totalD

def plotDecisionTree(decision_tree):
    fig = plt.figure(1, facecolor = 'white')
    fig.clf()
    axprops = dict(xticks=[], yticks=[])
    createPlot.ax1 = plt.subplot(111, frameon = False, **axprops)

    plotTree.totalW = float(getNumLeafs(decision_tree))
    plotTree.totalD = float(getTreeDepth(decision_tree))
    plotTree.xOff = -0.5/plotTree.totalW
    plotTree.yOff = 1.0
    plotTree(decision_tree, (0.5, 1.0), '')

    plt.show()
