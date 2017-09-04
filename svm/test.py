# encoding=utf-8
# import pudb
# pu.db
import pandas as pd
import numpy as np
import svm

d = svm.create_data()
data = d.ix[:,2:]
label = d.ix[:,0]

norm = svm.normalize(data)
data_transformed = svm.pca(norm,0.9)
"""
arguments: *;*;ratio;class weight;decision function shape;kernel
"""
grid,accuracy = svm.classify(data_transformed,label,0.8,{0: 20, 1: 20, 2: 20, 3: 30, 4: 20, 5: 20},'ovo','rbf')

fall_accuracy = grid[3,6]


