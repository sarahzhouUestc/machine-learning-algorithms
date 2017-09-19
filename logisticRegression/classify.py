# encoding=utf-8
import logRegression

data,labels = logRegression.load_train_data()
ws = logRegression.normalGradientAscent(data,labels,500)
print logRegression.testNormal()
print logRegression.testSto()
print logRegression.testImproved()
