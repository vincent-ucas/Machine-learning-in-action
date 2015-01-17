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

# ======== annotate Parameters ==========
#   more details can be found:
#   http://matplotlib.org/api/axes_api.html?highlight=annotate#matplotlib.axes.Axes.annotate
#
#   xy: (x, y)  position of element to annotate
#   xytext:     optional, default: None, position of labels
#   textcoords: string, optional, default: data
#   arrowprops: Dictionary of line properties for the arrow that connects the annotation to the point.
# =======================================

def plotNode(node_text, center_pt, parent_pt, node_type):
    createPlot.ax1.annotate(node_text, xy = parent_pt,
                            xycoords = 'axes fraction', xytext = center_pt,
                            textcoords = 'axes fraction', va = "center", ha = "center",
                            bbox = node_type, arrowprops = arrow_args)

# =====  create a plot for drawing leaf node and decision node ========
def createPlot():
    fig = plt.figure(1, facecolor = 'white')
    fig.clf()
    createPlot.ax1 = plt.subplot(111, frameon=False)
    plotNode('Decision Node', (0.5, 0.1), (0.1, 0.5), decision_node)
    plotNode('Leaf Node', (0.8, 0.1), (0.3, 0.8), leaf_node)

    plt.show()

if __name__ == '__main__' : createPlot()
