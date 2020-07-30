# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 18:03:41 2020

@author: Fu Xingyu
"""

import pandas as pd
import numpy as np
import math
import random


# 读取原始数据表
df = pd.read_csv('test.csv', encoding="GBK")
df.index = df.city_name
df=df.drop(["city_name"], axis=1)
print(df)

# 行名与列名
listColNames = df.columns.values.tolist()

listIndexNames = df._stat_axis.values.tolist()

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
newdf.index = listIndexNames
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
dfP.index = listIndexNames
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
dfResult.index = listIndexNames
dfResult['Rank'] = dfResult.rank()
print(dfResult)
for w in listW:
    print(w)
dfResult.to_csv("result.csv", encoding="GBK")
