# encoding=utf-8
"This module is used to construct tree using matplotlib"
from matplotlib import pyplot as plt

def calLeafNum(tree):
	if tree!=None and len(tree.keys())>0:
		keys = tree.keys()	
		root = keys[0]
		subtrees = tree[root]
		subkeys = subtrees.keys()
		leafNum = 0
		for subkey in subkeys:
			if type(subtrees[subkey]).__name__ == 'dict':
				leafNum += calLeafNum(subtrees[subkey])
			else:
				leafNum += 1
	return leafNum

def calDepth(tree):
	return None

