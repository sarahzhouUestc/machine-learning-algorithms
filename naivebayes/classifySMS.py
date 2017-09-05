# encoding=utf-8
from pudb import set_trace
set_trace()
import bayes
import pandas as pd

_filename="SMSSpamCollection"
def access():
	totalAcc = 0.0
	for i in range(10):
		labels,samples = bayes.load_data(_filename)
		trainIdx,testIdx = bayes.splitData(samples.index,0.7)
		dic = bayes.buildVocabularyList(samples)
		spamPro,pamPro,pw = bayes.bayesian(samples[trainIdx],labels[trainIdx],dic)
		acc = bayes.accuracy(samples[testIdx],labels[testIdx],dic,spamPro,pamPro,pw)
		totalAcc += acc
		print 'accuracy = %s' % acc
	averageAcc = float(totalAcc)/10
	print 'average accuracy is %f' % averageAcc


if __name__ == '__main__':
	access();