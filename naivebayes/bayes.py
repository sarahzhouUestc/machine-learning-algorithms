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

# Split the whole sentence into words list
def splitSampleToWords(sample):
	re = __import__('re')	
	regEx = re.compile(r'[a-zA-Z]{3,}')
	sample = [s.lower() for s in regEx.findall(sample)]	
	return sample

# convert each sample to vector [0,0,1,1,0...]
def sample2vec(vocabList, sample):
	np = __import__('numpy')
	vec = list(np.zeros(len(vocabList)))
	for word in splitSampleToWords(sample):
		if word in vocabList:
			vec[vocabList.index(word)] = 1
		else:
			print "The dictionary is inadequate!"
	return vec

# convert each sample to vector with its times
def sample2bagVec(vocabList, sample):
	np = __import__('numpy')
	vec = list(np.zeros(len(vocabList)))
	for word in splitSampleToWords(sample):
		if word in vocabList:
			vec[vocabList.index(word)] += 1
	return vec

def process_rss_data(rss1, rss2):
	parser = __import__('feedparser')
	pd = __import__('pandas')
	e1 = parser.parse(rss1)['entries']
	e2 = parser.parse(rss2)['entries']
	minLen = min(len(e1), len(e2))
	samples = []
	labelList = []
	for i in range(minLen):
		samples.append(e1[i]['summary'])
		labelList.append(1)
		samples.append(e2[i]['summary'])
		labelList.append(2)

	return pd.Series(labelList), pd.Series(samples)

def removeHighFreq(dic, samples):
	count = {}
	fullText = []
	for sample in samples:
		fullText.extend(splitSampleToWords(sample))
	for d in dic:
		count[d] = count.get(d,0) + fullText.count(d)
	operator = __import__('operator')
	sortedCount = sorted(count.iteritems(), key=operator.itemgetter(1), reverse=True)
	newDic = set([])
	for t in sortedCount[15:]:
		newDic.add(t[0])
	return list(newDic)

def load_data(filename):
	pd = __import__('pandas')
	data = pd.read_table(filename,header=None)
	labels = [1 if l=='spam' else 0 for l in data.ix[:,0]]
	samples = data.ix[:,1]
	return pd.Series(labels),pd.Series(samples)

def buildVecsAndLabels(samples, labels, dic):
	#spam sms category's probability
	pw = sum(labels)/float(len(labels))
	#make samples from text to [0,1] vector, who has same length with dic
	sampleVecs = []
	sampleLabs = []
	for i in samples.index:
		sampleVecs.append(sample2vec(dic,samples[i]))
		sampleLabs.append(labels[i])
	return sampleVecs, sampleLabs, pw

def buildVecsAndLabelsBag(samples, labels, dic):
	#spam sms category's probability
	pw = sum([l for l in labels if l==1])/float(len(labels))
	#make samples from text to [0,1] vector, who has same length with dic
	sampleVecs = []
	sampleLabs = []
	for i in samples.index:
		sampleVecs.append(sample2bagVec(dic,samples[i]))
		sampleLabs.append(labels[i])
	return sampleVecs, sampleLabs, pw

def bayesian(vecs,labels,dic):
	#each for spam category and pam category, respective likelihood probability
	np = __import__('numpy')
	spamCount = 2
	spamStat = np.ones(len(dic))
	pamCount = 2
	pamStat = np.ones(len(dic))
	for i in range(len(vecs)):
		s = vecs[i]
		if labels[i] == 1:
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
	return spamPro,pamPro

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

def classifyRss(sample,dic,pro1,pro2,pw):
	v = sample2bagVec(dic, sample)
	np = __import__('numpy')
	math = __import__('math')
	pro1 = sum(np.multiply(v,pro1)) + math.log(pw,2)
	pro2 = sum(np.multiply(v,pro2)) + math.log((1-pw),2)
	if pro1 >= pro2:
		return 1
	else:
		return 2

def splitData(idx,ratio):
	np = __import__('numpy')
	trainIdx = list(np.random.choice(idx,int(len(idx)*ratio),replace=False))
	testIdx = [i for i in idx if i not in trainIdx]
	return trainIdx,testIdx

def getTopWordsOfRss(pro1,pro2,vocabList):
	top1 = []
	top2 = []
	for i in range(len(vocabList)):
		if pro1[i] > (-1)*7.0:
			top1.append((vocabList[i],pro1[i]))
		if pro2[i] > (-1)*7.0:
			top2.append((vocabList[i],pro2[i]))
	return top1,top2


def accuracyRss(testSamples,testlabels,dic,spampro,pampro,pw):
	testnum = len(testSamples)
	rightCount = 0
	for i in testSamples.index:
		sample = testSamples[i]
		pred = classifyRss(sample,dic,spampro,pampro,pw)
		if(pred == testlabels[i]):
			rightCount += 1
	return float(rightCount)/testnum

def accuracy(testSamples,testlabels,dic,pro1,pro2,pw):
	testnum = len(testSamples)
	rightCount = 0
	for i in testSamples.index:
		sample = testSamples[i]
		pred = classify(sample,dic,pro1,pro2,pw)
		if(pred == testlabels[i]):
			rightCount += 1
	return float(rightCount)/testnum
	

