# encoding=utf-8
import numpy as np
import operator

def normalize(dataset):
    """
    Normalize dataset, and make mean value be 0 and variance be 1.
    """
    minVals = dataset.min(axis=0)
    maxVals = dataset.max(axis=0)
    factors = maxVals-minVals
    num = dataset.shape[0]
    norm_data = (dataset - np.tile(minVals,(num,1)))/np.tile(factors,(num,1)) 
    return norm_data

def pca(dataset,e):
    """
    e: threshold, for example 90%
    """
    d = np.array(dataset)
    cov = np.cov(d.transpose())
    vals,vecs = np.linalg.eig(cov)
    desc_idx = np.argsort(-vals)
    desc_idx_sel = []
    sum_vals = sum(vals)
    temp = 0
    for x in desc_idx:
        desc_idx_sel.append(x)
        temp = temp+vals[x]
        if(temp/sum_vals>=e):
            break
    ratio = temp/sum_vals
    transform_matrix = vecs[desc_idx_sel]
    data_transformed = np.mat(dataset)*np.transpose(np.mat(transform_matrix))
    return ratio,data_transformed

def classifyKNN(x,dataset,labels,k):
    dataSetNum = dataset.shape[0]     
    diffMat = np.tile(x, (dataSetNum, 1)) - dataset
    sqDistances = list(np.tile(0,diffMat.shape[0]))
    for i in range(diffMat.shape[0]):
        for j in range(diffMat.shape[1]):
            sqDistances[i]+=diffMat[i,j]**2    

    distances = [d**0.5 for d in sqDistances]
    distances = np.array(distances)
    sortedDistanceIdx = distances.argsort()  
    classCount={}
    for i in range(k):
        voteLabel = labels[int(sortedDistanceIdx[i])]
        classCount[voteLabel] = classCount.get(voteLabel,0) + 1
    sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    #  print sortedClassCount
    return sortedClassCount[0][0]
