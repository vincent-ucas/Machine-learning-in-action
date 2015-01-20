"""
    $author:      Ming
    $date:        2015/01/20
    $Description: Logistic Regression, two classes classifier.
"""

from numpy import *

def loadData(filename):
    data_mat = []; label_mat = []
    fr = open(filename)
    read_lines = fr.readlines()
    for line in read_lines:
        line_arr = line.strip().split()
        data_mat.append([1.0, float(line_arr[0]), float(line_arr[1])])
        label_mat.append(int(line_arr[2]))

    return data_mat, label_mat

#                                  1
#   sigmoid function: g(z) = -------------
#                             1 + exp(-z)
def sigmoid(in_x):
    return 1.0/(1+exp(-in_x))

#
#   gradient ascent for optimization of logistic regression:  w = w' + a*(f-delta)
#
def gradAscent(data_arr, label_arr):
    data_mat = mat(data_arr)
    label_mat = mat(label_arr).transpose()
    m,n = shape(data_mat)
    altha = 0.001           # learning rate
    max_iters = 500         # maximum of iteration
    weights = ones((n,1))

    for i in range(max_iters):
        h = sigmoid(data_mat*weights)
        dif = (label_mat - h)
        weights = weights + altha*(data_mat.transpose()*dif)    # updated weights by gradient ascent..

    return weights

#
#   random gradient ascent: increasing the iteration effiency.
#
def stocGradAscent(data_arr, label_arr, num_iter=150):
    m, n = shape(data_arr)
    weights = ones(n)
    for j in range(num_iter):
        data_idx = range(m)
        for i in range(m):
            alpha = 4/(1.0+j+i)+0.01
            rand_idx = int(random.uniform(0, len(data_idx)))
            h = sigmoid(sum(data_arr[rand_idx]*weights))
            dif = label_arr[rand_idx] - h
            weights = weights + alpha * dif * data_arr[rand_idx]
            del (data_idx[rand_idx])
    return weights

#
#   plot best fit weights, logistic regression.
#
def plotBestFit(data_mat, label_mat, w):
    import matplotlib.pyplot as plt

    weights = w#.getA()
    data_arr = array(data_mat)
    n = shape(data_arr)[0]

    x1_cords = []; y1_cords = []
    x2_cords = []; y2_cords = []
    for i in range(n):
        if int(label_mat[i]) == 1:
            x1_cords.append(data_arr[i, 1]); y1_cords.append(data_arr[i, 2])
        else:
            x2_cords.append(data_arr[i, 1]); y2_cords.append(data_arr[i, 2])

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(x1_cords, y1_cords, s=30, c='red',marker='s')
    ax.scatter(x2_cords, y2_cords, s=30, c='green')
    x = arange(-3.0, 3.0, 1.0)
    y = (-weights[0] - weights[1]*x)/weights[2]
    ax.plot(x,y)
    plt.xlabel('X1'); plt.ylabel('X2')
    plt.show()

