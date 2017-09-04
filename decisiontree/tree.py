# encoding=utf-8
"这个模块是决策树的核心模块"

_filename = 'lenses.txt'
_name = ['age','prescription','astigmatic','tear','class'] 

def load_data():
    pd = __import__('pandas')
    return pd.read_table(_filename,sep='  ',header=None,engine='python')

def splitDataSet(data,fea,value):
    """   
    根据特征，和特征对应的值，抽取对应的子集，其中子集排除了该特征
    """
    #selected: extracted samples that meet fea's value==value
    selected = data[data[fea]==value]
    if fea==0:
        return selected.ix[:,1:]
    else:
        pd = __import__('pandas')
        sub1 = selected.ix[:,:(fea-1)]
        sub2 = selected.ix[:,(fea+1):]
    return pd.concat([sub1,sub2],axis=1)

#calculate shanon entroy
def shanonEntroy(data):
    classcount = _getClassCount(data)
    total = len(data)
    entroy = 0.0
    math = __import__('math')
    for v in classcount.values():
        prob = float(v)/total
        entroy -= prob*math.log(prob,2)
    return entroy 

def chooseBestFea(data):
    origEntroy = shanonEntroy(data)
    bestFea = -1
    bestIG = 0.0
    feas = data.columns
    # 条件熵
    for i in range(len(feas)-1):
        fea = feas[i]
        newEntroy = 0.0
        cfea_values = set(data[fea])
        for v in cfea_values:
            subset = splitDataSet(data,fea,v)
            prob = float(len(subset))/len(data)
            e = shanonEntroy(subset)
            newEntroy += prob * e
        ig = origEntroy - newEntroy #信息增益
        if ig > bestIG:
            bestIG = ig
            bestFea = i
    return feas[bestFea]

def createTree(dataset):
    #递归终止条件
    cols = dataset.columns 
    classes = dataset[cols[len(cols)-1]]
    if len(set(classes))==1:
        return set(classes)
    if len(cols)==1:
        return _majority(classes) 
    bestFea = chooseBestFea(dataset)
    label = _name[bestFea]
    node = {label:{}}
    bestFeaValues = set(dataset[bestFea])
    for value in bestFeaValues:
        node[label][value] = createTree(splitDataSet(dataset,bestFea,value))
    return node

def _majority(l):
    count = {}
    for i in l:
        if i not in count.keys():
            count[i]=0
        count[i] += 1
    operator = __import__('operator')
    count = sorted(count.iteritems(),key=operator.itemgetter(1),reverse=True)
    return count[0][0]


def _getClassCount(data):
    classcount = {}
    cols = data.columns
    classes = data[cols[len(cols)-1]]
    for i in classes:
        if i not in classcount.keys():
            classcount[i]=0
        classcount[i] += 1
    return classcount
