# encoding=utf-8
"This module encapsulate primary logic of logistic regression"
# from pudb import set_trace
# set_trace()

def load_train_data():
	pd = __import__('pandas')
	np = __import__('numpy')
	d = pd.read_table('horseTraining.txt',header=None,engine='python')
	labels = d.iloc[:,-1]
	data = d.iloc[:,0:-1]
	return np.mat(data),np.mat(labels).transpose()

def load_test_data():
	pd = __import__('pandas')
	np = __import__('numpy')
	d = pd.read_table('horseTest.txt',header=None,engine='python')
	labels = d.iloc[:,-1]
	data = d.iloc[:,0:-1]
	return data,labels

def sigmoid(x):
	np = __import__('numpy')
	return longfloat(1/(1+np.exp((-1)*x)))

def normalGradientAscent(data,labels,iterNum):
	np = __import__('numpy')
	ws = np.mat(np.ones(data.shape[1])).transpose()
	alpha = 0.001
	for i in range(iterNum):
		pred = sigmoid(np.dot(data,ws))
		error = pred-labels
		grad = np.dot(np.mat(data).transpose(),error)
		ws = ws + alpha*grad
	return ws

def stochasticGradientAscent(data,labels):
	np = __import__('numpy')
	m,n = data.shape
	ws = np.mat(np.ones(n)).transpose()
	alpha = 0.001
	for i in range(m):
		e = labels[i]-sigmoid(data[i]*ws)
		ws = ws + (alpha*e*data[i]).transpose()
	return ws

def improvedStoGraAscent(data,labels,iterNum):
	pd = __import__('pandas')
	np = __import__('numpy')
	# data = pd.DataFrame(data)
	# labels = pd.DataFrame(labels)
	m,n = data.shape
	ws = np.mat(np.ones(n)).transpose()
	for i in range(iterNum):
		idxs = list(pd.DataFrame(labels).index)
		for j in range(m):
			alpha = 4/(1.0+i+j)+0.001
			idx = np.random.choice(idxs,1)
			sample = data[idx]
			e = labels[idx]-sigmoid(data[idx]*ws)
			ws = ws + np.mat(alpha*e*data[idx]).transpose()
			idxs.remove(idx[0])
	return ws

def predict(s,w):
	np = __import__('numpy')
	pred = sigmoid(np.dot(s,w))
	if(pred >= 0.5):
		return 1
	else:
		return 0

def testNormal():
	np = __import__('numpy')
	train,train_labels = load_train_data()
	test,test_labels = load_test_data()
	weights = normalGradientAscent(train,train_labels,500)
	total = len(test)
	error_count = 0.0
	for i in test.index:
		t = test.loc[i]
		pred = predict(t,weights)
		if pred != int(test_labels.loc[i]):
			error_count += 1
	return error_count/total

def testSto():
	np = __import__('numpy')
	train,train_labels = load_train_data()
	test,test_labels = load_test_data()
	weights = stochasticGradientAscent(train,train_labels)
	total = len(test)
	error_count = 0.0
	for i in test.index:
		t = test.loc[i]
		pred = predict(t,weights)
		if pred != int(test_labels.loc[i]):
			error_count += 1
	return error_count/total

def testImproved():
	np = __import__('numpy')
	train,train_labels = load_train_data()
	test,test_labels = load_test_data()
	weights = improvedStoGraAscent(train,train_labels,5)
	total = len(test)
	error_count = 0.0
	for i in test.index:
		t = test.loc[i]
		pred = predict(t,weights)
		if pred != int(test_labels.loc[i]):
			error_count += 1
	return error_count/total

