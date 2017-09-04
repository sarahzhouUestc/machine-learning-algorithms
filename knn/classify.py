# encoding=utf-8
import falldetect as fall

data = fall.createData('falldeteciton.csv')
#  data = data.ix[0:20]
labels = data.ix[:,['ACTIVITY']]
features = data.ix[:,['TIME','SL','EEG','BP','HR','CIRCLUATION']]
norm = fall.normalize(features)
new_fea = fall.pca(norm,0.9)
dtr,dte,itr,ite = fall.partition(norm,0.8)
train_labels = labels.ix[itr]
test_labels = labels.ix[ite]


def accuracy(k):
    count = 0
    for x in dte.index:
        pre = fall.predict(dte.ix[x],dtr,train_labels,k)
        real = test_labels.ix[x]
        #  print pre,real.ix['ACTIVITY']
        if pre == real.ix['ACTIVITY']:
            count+=1
    return float(count)/float(len(dte))

print accuracy(7)

#  for i in [3,4,5,6,7,8,9,10,11,12,13]:
    #  print accuracy(i)
