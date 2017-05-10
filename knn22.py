# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from numpy import *
import pandas as pd
path = '/users/admin/PycharmProjects/knn/test1.csv'
arr = pd.read_csv(path)
print type(arr)
l = type(arr)
def kNNClassify(newInput, dataSet, labels, k):
    numSamples = dataSet.shape[0]  # shape[0] stands for the num of row

    ## step 1: calculate Euclidean distance
    # tile(A, reps): Construct an array by repeating A reps times
    # the following copy numSamples rows for dataSet
    diff = tile(newInput, (numSamples, 1)) - dataSet  # Subtract element-wise
    squaredDiff = diff ** 2  # squared for the subtract
    squaredDist = sum(squaredDiff, axis=1)  # sum is performed by row
    distance = squaredDist ** 0.5

    ## step 2: sort the distance
    # argsort() returns the indices that would sort an array in a ascending order
    sortedDistIndices = argsort(distance)

    classCount = {}  # define a dictionary (can be append element)
    for i in xrange(k):
        ## step 3: choose the min k distance
        voteLabel = labels[sortedDistIndices[i]]

        ## step 4: count the times labels occur
        # when the key voteLabel is not in dictionary classCount, get()
        # will return 0
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1

        ## step 5: the max voted class will return
    maxCount = 0
    for key, value in classCount.items():
        if value > maxCount:
            maxCount = value
            maxIndex = key

    return maxIndex

l = []
for i in range(0, arr.shape[0]):
    results = []
    for j in range(0, arr.shape[1]-1):
        inX = [j, arr[str(j)][i]]
        dataset = []
        label = list(arr['class'])
        del label[i]
        for k in range(0, arr.shape[0]):
            dataset.append([j, arr[str(j)][k]])
            pass
        dataset.remove([j,arr[str(j)][i]])

        c1 = kNNClassify(inX, array(dataset), list(label), 5)
        results.append(c1)
    l.append(results)
print(l)
A_true = [0]*(arr.shape[1]-1)
A_false= [0]*(arr.shape[1]-1)
B_true = [0]*(arr.shape[1]-1)
B_false = [0]*(arr.shape[1]-1)
classLabel = list(arr['class'])
for m in range(0,len(classLabel)):
    for n in range(0,arr.shape[0]):
        if classLabel[m]=='A':
            if arr[str(n)][m]=='A':
                A_true[n] += 1
            elif arr[str(n)][m]=='B':
                A_false[n] += 1
        if classLabel[m]=='B':
            if arr[str(n)][m]=='B':
                B_true[n] += 1
            elif arr[str(n)][m]=='A':
                B_false[n] += 1
print A_true
print A_false
print B_true
print B_false

