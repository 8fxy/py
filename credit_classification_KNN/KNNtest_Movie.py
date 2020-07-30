import numpy as np
import operator

def createDataset():
    #四组二维特征,[kiss, act]
    group = np.array([[0,1,1],[78,122,4],[103,200,5],[2,9,1]])
    #四组对应标签
    labels = ('A','B','B','A')
    return group,labels

def classify(intX,dataSet,labels,k):
    '''
    KNN算法
    '''
    #numpy中shape[0]返回数组的行数，shape[1]返回列数
    dataSetSize = dataSet.shape[0]
    #将intX在横向重复dataSetSize次，纵向重复1次
    #例如intX=([1,2])--->([[1,2],[1,2],[1,2],[1,2]])便于后面计算
    print(np.tile(intX, (dataSetSize, 1)))
    print(dataSet)
    diffMat = np.tile(intX,(dataSetSize,1))-dataSet
    #二维特征相减后乘方
    sqdifMax = diffMat**2
    #计算距离,现在对于数据的处理更多的还是numpy。没有axis参数表示全部相加，axis＝0表示按列相加，axis＝1表示按照行的方向相加
    seqDistances = sqdifMax.sum(axis=1)
    distances = seqDistances**0.5
    print ("distances:",distances)
    #返回distance中元素从小到大排序后的索引值
    sortDistance = distances.argsort()
    print ("sortDistance:",sortDistance)
    #创建空字典
    classCount = {}
    for i in range(k):
        print("i=",i)
        #取出前k个元素的类别
        voteLabel = labels[sortDistance[i]]
        print ("第%d个是"%(i+1),voteLabel)
        # 类别计数
        # dict.get(key,default=None),字典的get()方法,返回指定键的值,如果值不在字典中返回默认值。
        classCount[voteLabel] = classCount.get(voteLabel,0)+1
    #key=operator.itemgetter(1)根据字典的值进行排序
    #key=operator.itemgetter(0)根据字典的键进行排序
    #reverse降序排序字典
    sortedClassCount = sorted(classCount.items(),key = operator.itemgetter(1),reverse = True)
    #结果sortedClassCount = [('动作片', 2), ('爱情片', 1)]
    print ("sortedClassCount:",sortedClassCount)
    return sortedClassCount[0][0]
if __name__ == '__main__':
    group,labels = createDataset()
    test = [30,40,1]
    test_class = classify(test,group,labels,3)
    print (test_class)