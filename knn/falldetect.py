# encoding=utf-8

"This module is to classify by KNN algorithm"

def createData(url):
    pd = __import__('pandas')
    return pd.read_csv(url)


def normalize(features):
    np = __import__('numpy')
    aver = np.average(features, axis=0)
    sigma = np.std(features, axis=0)
    norm =\
    (features-np.tile(aver,(features.shape[0],1)))/np.tile(sigma,(features.shape[0],1))
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


def partition(d,ratio):
    """
    ratio是随机选取的用作训练的比例
    """
    np = __import__('numpy')
    pd = __import__('pandas')
    d = pd.DataFrame(d)
    idx = d.index.get_values()
    idx_train = np.random.choice(idx,int(d.shape[0]*ratio),replace=False)
    idx_test = [x for x in idx if x not in idx_train] 
    data_train = d.ix[idx_train]
    data_test = d.ix[idx_test]
    return data_train,data_test,idx_train,idx_test

def predict(x,train,train_labels,k):
    np = __import__('numpy')
    x_tile = np.tile(x,(train.shape[0],1))
    differ = x_tile-train
    square = differ**2
    square_dis = np.sum(square,axis=1)
    distance = np.sqrt(square_dis)
    distance = distance.sort_values(ascending=True)
    nearest = distance.iloc[0:k].index
    category = {}
    for x in nearest:
        label = train_labels.ix[x]
        if category.get(label['ACTIVITY'],0)==0:
            category[label['ACTIVITY']]=1
        else:
            category[label['ACTIVITY']]+=1
    n = sorted(category.iteritems(),key=lambda x:x[1],reverse=True)
    return n[0][0]



