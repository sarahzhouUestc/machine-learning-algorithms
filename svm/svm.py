# encoding=utf-8
from sklearn import svm
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

_data_file = 'falldeteciton.csv'

def create_data():
	pd = __import__('pandas')		
	data = pd.read_csv(_data_file)
	return data


def normalize(data):
    np = __import__('numpy')
    aver = np.average(data, axis=0)
    sigma = np.std(data, axis=0)
    norm = (data-np.tile(aver,(data.shape[0],1)))/np.tile(sigma,(data.shape[0],1))
    return norm 



def pca(norm,e):
    np = __import__('numpy')
    cov = np.cov(norm.T)
    w,v = np.linalg.eig(cov)
    sort = np.argsort(-w)
    sel = []
    total = 0
    s = sum(w)
    for i in sort:
        sel.append(i)
        total += w[i]
        if float(total)/float(s) >= e:
            break
    trans_matrix = v[sel]
    return np.matrix(norm)*np.matrix(trans_matrix).T 


def spilitData(data,ratio=0.7):
    """
    ratio
    """
    np = __import__('numpy')
    pd = __import__('pandas')
    data = pd.DataFrame(data)
    idx = data.index.get_values()
    idx_train = np.random.choice(idx,int(data.shape[0]*ratio),replace=False)
    idx_test = [x for x in idx if x not in idx_train] 
    data_train = data.ix[idx_train]
    data_test = data.ix[idx_test]
    return data_train,data_test,idx_train,idx_test



def classify(data,label, ratio, class_weight, decision_function_shape, kernel):
	train,test,idx_train,idx_test = spilitData(data,ratio)
	X = np.matrix(train)
	Y = label[idx_train]
	clf = svm.SVC(decision_function_shape=decision_function_shape,class_weight=class_weight,kernel=kernel)
	clf.fit(X,Y)
	return accuracy(test,label[idx_test],clf)

def accuracy(test_data,test_label,classifier):
	pred = []
	truth = []
	right_count = 0
	idx = test_data.index.get_values()
	for i in idx:
		d = test_data.ix[i]
		pre = classifier.predict([list(d)])[0]
		pred.append(pre)
		truth.append(test_label[i])
		if(pre == test_label[i]):
			right_count += 1

	grid = np.matrix(np.zeros((7,7)))
	for i in range(len(truth)):
		t = truth[i]
		p = pred[i]
		grid[t,p] += 1
		if t != p:
			grid[p,t] += 1
	for i in range(6):
		c_total = len(test_label[test_label==i])
		c_correct = grid[i,i]
		grid[i,6] = float(c_correct)/c_total
		grid[6,i] = float(c_correct)/c_total
	accuracy = float(right_count)/len(test_data)
	return grid,accuracy


