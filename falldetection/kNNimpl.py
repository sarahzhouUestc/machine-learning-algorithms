# encoding=utf-8
import pandas as pd
from matplotlib import pyplot as plt 
import kNN

raw_data = pd.read_csv(r'falldeteciton.csv',engine='python') 
columns = ['ACTIVITY','TIME','SL','EEG','BP','HR','CIRCLUATION']
labels = raw_data[0:]['ACTIVITY']
data = raw_data[0:][['TIME','SL','EEG','BP','HR','CIRCLUATION']]
count = data.shape[0]

radio,data_transformed = kNN.pca(data,0.9) 

test_data = data_transformed[:int(count*0.3)]
test_labels = list(labels[:int(count*0.3)])
train_data = data_transformed[int(count*0.3):]
train_labels = list(labels[int(count*0.3):])

#  pre_label = kNN.classifyKNN(test_data[0],train_data,train_labels,5)
#  print "The prediction label is %s" % pre_label
#  print "The true label is %s" % test_labels[0]

def predict(index):
    pre_label = kNN.classifyKNN(test_data[index],train_data,train_labels,5)
    true_label = test_labels[index]
    print "The prediction label is %s" % pre_label
    print "The true label is %s" % test_labels[index]


def accuracy():
    count = len(test_data)
    wrong_num = 0
    for i in range(count):
        if (kNN.classifyKNN(test_data[i],train_data,train_labels,7) !=
        test_labels[i]):
            wrong_num+=1
    return float(count-wrong_num)/float(count)

