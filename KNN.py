import numpy as np

from array import *
import operator
def createDataSet(random_book_count):
    group = np.array(random_book_count)
    labels = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B']
    return group, labels
# python处理数据
# 计算已知类别数据集中的点与当前点之间的距离（欧式距离）
# 按照距离递增次序排序
# 选取与当前点距离最小的K个点
# 确定前K个点所在类别的出现频率
# 返回前k个点出现频率最高的类别最为当前点的预测分类
# inX输入向量，训练集dataSet,标签向量labels，k表示用于选择最近邻的数目


def clissfy0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteLabel = labels[sortedDistIndicies[i]]
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

