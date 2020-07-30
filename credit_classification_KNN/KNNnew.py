import csv
from numpy import *
import operator

def creatDataSet():
    group,labels=[],[]
    filename = 'loan.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        for row in reader:                 # 行号从1开始
            labels.append(row[3])
            del row[3]
            group.append(row)
    group = array(group).astype('float64') #从列表转换为浮点数数组
    return group,labels

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]  # 矩阵第一维度的长度
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)  # 按行相加形成列
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1  # classCount是字典，.get是取出键值，dict[key]对键值进行赋值
        sortedClassCount = sorted(classCount.items(),
                                  key=operator.itemgetter(1), reverse=True)
    print(classCount)
    return sortedClassCount[0][0]

group,labels =creatDataSet()
a = classify0([35000,22.15,969.65,11.72,0,0], group, labels, 20) #手工输入检验
print(a)

    #H:\E\lending-club-loan-data\loan.csv