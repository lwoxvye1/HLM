import numpy as np
import KNN
from numpy import *
from array import *
(dataSet, labels) = KNN.createDataSet()
testX = np.array([1.2, 1.1])
k = 3
outputLabelX = KNN.clissfy0(testX, dataSet, labels, k)
testY = np.array([0.1, 0.3])
outputLabelY = KNN.clissfy0(testY, dataSet, labels, k)
print('input is :', testX, 'output class is :', outputLabelX)
print('input is :', testY, 'output class is :', outputLabelY)
"""python结果输出
('input is :', array([1.2, 1.1]), 'output class is :', 'A')
('input is :', array([0.1, 0.3]), 'output class is :', 'B')
"""