# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 18:03:41 2020

@author: Fu Xingyu
"""

import pandas as pd
import numpy as np
import math
import random


# 生成随机DataFrame
def getRandomList():
    all_num = 100
    a_list = [i for i in range(all_num)]
    b_list = []
    num = 11
    for i in range(num):
        random_number = random.randint(1, all_num-1)
        b_list.append(random_number)
    return b_list


keshi = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
X1 = getRandomList()
X2 = getRandomList()
X3 = getRandomList()
X4 = getRandomList()
X5 = getRandomList()
X6 = getRandomList()
X7 = getRandomList()
X8 = getRandomList()
X9 = getRandomList()
df = pd.DataFrame({
                "X1": X1,
                "X2": X2,
                "X3": X3,
                "X4": X4,
                "X5": X5,
                "X6": X6,
                "X7": X7,
                "X8": X8,
                "X9": X9})
df.index = keshi

# 行名与列名
listColNames = df.columns.values.tolist()
listIndexNames = keshi

# 0-1标准化
newdf = pd.DataFrame()
for _ in listColNames:
    a = df[_]
    # print(a)
    listStdCol = []
    for _ in a:
        stdVal = (_ - a.min())/(a.max() - a.min())
        listStdCol.append(stdVal)
    newdf = pd.concat([newdf, pd.DataFrame(listStdCol)], axis=1)
newdf.index = keshi
newdf.columns = df.columns.values.tolist()

# 计算概率P表
dfP = pd.DataFrame()
for _ in listColNames:
    b = newdf[_]
    listPCol = []
    for _ in b:
        pVal = _/b.sum()
        listPCol.append(pVal)
    dfP = pd.concat([dfP, pd.DataFrame(listPCol)], axis=1)
dfP.index = keshi
dfP.columns = df.columns.values.tolist()

# 计算信息熵E表
n = dfP.iloc[:, 0].size
listE = []
for _ in listColNames:
    c = dfP[_]
    sumPlnP = 0
    for _ in c:
        if _ != 0:
            PlnP = _*math.log(_)
            sumPlnP = sumPlnP + PlnP
        else:
            PlnP = 0
            sumPlnP = sumPlnP + PlnP
    EVal = (-1)*(1/math.log(n))*sumPlnP
    listE.append(EVal)

# 计算权重W
listW = []
sumE = sum(listE)
k = dfP.columns.size
for _ in listE:
    W = (1-_)/(k-sumE)
    listW.append(W)

# 计算最终得分
listResult = []
for index, row in df.iterrows():
    eScore = row*listW
    totalScore = sum(eScore)
    listResult.append(totalScore)
dfResult = pd.DataFrame({'Score':listResult})
dfResult.index = keshi
dfResult['Rank'] = dfResult.rank()
print(dfResult)
