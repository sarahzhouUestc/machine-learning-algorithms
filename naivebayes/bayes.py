# encoding=utf-8
"This module is used to implement bayes algorithm"

# build vocabulary dictionary using all data
def buildVocabularyList(samples):
	pd = __import__('pandas')
	vocabList = set([])
	re = __import__('re')	
	regEx = re.compile(r'[a-zA-Z]{3,}')
	for idx in samples.index:
		vocabList = vocabList.union([s.lower() for s in regEx.findall(samples[idx])])
	return list(vocabList)

# convert each sample to vector [0,0,1,1,0...]
def sample2vec(vocabList, sample):
	np = __import__('numpy')
	vec = list(np.zeros(len(vocabList)))
	re = __import__('re')	
	regEx = re.compile(r'[a-zA-Z]{3,}')
	sample = [s.lower() for s in regEx.findall(sample)]	
	for word in sample:
		if word in vocabList:
			vec[vocabList.index(word)] = 1
		else:
			print "The dictionary is inadequate!"
	return vec

def load_data(filename):
	pd = __import__('pandas')
	data = pd.read_table(filename,header=None)
	labels = [1 if l=='spam' else 0 for l in data.ix[:,0]]
	samples = data.ix[:,1]
	return pd.Series(labels),pd.Series(samples)

def bayesian(samples,labels,dic):
	#spam sms category's probability
	pw = sum(labels)/float(len(labels))
	#make samples from text to [0,1] vector, who has same length with dic
	sampleVecs = []
	sampleLabs = []
	for i in samples.index:
		sampleVecs.append(sample2vec(dic,samples[i]))
		sampleLabs.append(labels[i])
	
	#each for spam category and pam category, respective likelihood probability
	np = __import__('numpy')
	spamCount = 2
	spamStat = np.ones(len(dic))
	pamCount = 2
	pamStat = np.ones(len(dic))
	for i in range(len(sampleVecs)):
		s = sampleVecs[i]
		if sampleLabs[i] == 1:
			spamCount += sum(s)
			for j in range(len(s)):
				if s[j] == 1:
					spamStat[j] += 1
		else:
			pamCount += sum(s)
			for j in range(len(s)):
				if s[j] == 1:
					pamStat[j] +=1
	math = __import__('math')
	spamPro = [math.log(stat/float(spamCount),2) for stat in spamStat]
	pamPro = [math.log(stat/float(pamCount),2) for stat in pamStat]
	return spamPro,pamPro,pw

def classify(sample,dic,spampro,pampro,pw):
	v = sample2vec(dic,sample)
	np = __import__('numpy')
	math = __import__('math')
	pro1 = sum(np.multiply(v,spampro)) + math.log(pw,2)
	pro0 = sum(np.multiply(v,pampro)) + math.log((1-pw),2)
	if pro1 >= pro0:
		return 1
	else:
		return 0

def splitData(idx,ratio):
	np = __import__('numpy')
	trainIdx = list(np.random.choice(idx,int(len(idx)*ratio),replace=False))
	testIdx = [i for i in idx if i not in trainIdx]
	return trainIdx,testIdx


def accuracy(testSamples,testlabels,dic,spampro,pampro,pw):
	testnum = len(testSamples)
	rightCount = 0
	for i in testSamples.index:
		sample = testSamples[i]
		pred = classify(sample,dic,spampro,pampro,pw)
		if(pred == testlabels[i]):
			rightCount += 1
	return float(rightCount)/testnum

