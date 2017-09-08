# encoding=utf-8
"This module is used to find district tendency"
# from pudb import set_trace
# set_trace()

_filename1 = "https://sfbay.craigslist.org/stp/index.rss"
_filename2 = "https://newyork.craigslist.org/stp/index.rss"

import bayes
labels,samples = bayes.process_rss_data(_filename1, _filename2)
trainIdx,testIdx = bayes.splitData(samples.index, 0.7)
dic = bayes.buildVocabularyList(samples)
newDic = bayes.removeHighFreq(dic, samples)
trainVecs,trainLabels, pw = bayes.buildVecsAndLabelsBag(samples[trainIdx],labels[trainIdx],newDic)
pro1,pro2 = bayes.bayesian(trainVecs, trainLabels, newDic)
acc = bayes.accuracyRss(samples[testIdx], labels[testIdx], newDic, pro1, pro2, pw)

top1,top2 = bayes.getTopWordsOfRss(pro1,pro2,newDic)

print acc
print "===========sfbay============="
for t in top1:
	print t[0]
print "===========newyork==========="
for t in top2:
	print t[0]
