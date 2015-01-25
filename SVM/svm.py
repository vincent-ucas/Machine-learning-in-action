"""
    $author:      Ming
    $date:        2015/01/25
    $Description: Support Vector Machine (SVM) classifier, training based on SMO algorithm.
"""
from numpy import *

def loadDataSet(filename):
    data_mat = []; label_mat = []
    fr = open(filename)
    for line in fr.readlines():
        line_arr = line.strip().split()
        data_mat.append([float(line_arr[0]), float(line_arr[1])])
        label_mat.append(int(line_arr[-1]))
    return data_mat, label_mat

def selectJrand(i, m):
    j = i
    while(j == i):
        j = int(random.uniform(0, m))
    return j

def clipAlpha(aj, h, l):
    if aj > h:  aj = h
    if aj < l:  aj = l
    return aj