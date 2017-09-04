#encoding=utf-8
# from pudb import set_trace
# set_trace()
# import pudb
# pu.db
import tree
d = tree.load_data()
t = tree.createTree(d)
import visualization
leaf = visualization.calLeafNum(t)



