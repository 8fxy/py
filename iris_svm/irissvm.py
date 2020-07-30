# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 10:08:18 2019

@author: FXY
"""

# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
from sklearn import svm
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import colors
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from sklearn.model_selection import train_test_split
def iris_type(s):
    it = {b'setosa': 0, b'versicolor': 1, b'virginica': 2}
    return it[s]


def show_accuracy(y_hat, y_test, param):
    pass
 
path = 'iris.txt' # 数据文件路径
data = np.loadtxt(path, dtype=float, delimiter=',', converters={4: iris_type})
x, y = np.split(data, (4,), axis=1)
#x = x[:, :u2]
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, train_size=0.8)


clf = svm.SVC(C=0.1, kernel='linear', decision_function_shape='ovr') #线性核函数
#clf = svm.SVC(C=0.8, kernel='rbf', gamma=20, decision_function_shape='ovr') #非线性核函数
clf.fit(x_train, y_train.ravel())
print(clf.score(x_train, y_train))  # 精度
y_hat = clf.predict(x_train)
show_accuracy(y_hat, y_train, '训练集')
print(clf.score(x_test, y_test))
y_hat = clf.predict(x_test)
show_accuracy(y_hat, y_test, '测试集')
 
#输出决策方程和预测值

print ('decision_function:\n', clf.decision_function(x_train))
print ('\npredict:\n', clf.predict(x_train))

x1_min, x1_max = x[:, 0].min(), x[:, 0].max()  # 第0列的范围
x2_min, x2_max = x[:, 1].min(), x[:, 1].max()  # 第1列的范围
x3_min, x3_max = x[:, 2].min(), x[:, 2].max()
x4_min, x4_max = x[:, 3].min(), x[:, 3].max()

x1, x2 = np.mgrid[x1_min:x1_max:200j, x2_min:x2_max:200j]  # 生成网格采样点
x3, x4 = np.mgrid[x3_min:x3_max:200j, x4_min:x4_max:200j]  # 生成网格采样点
grid_test = np.stack((x1.flat, x2.flat, x3.flat, x4.flat), axis=1)  # 测试点

mpl.rcParams['font.sans-serif'] = [u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False
 
cm_light = mpl.colors.ListedColormap(['#A0FFA0', '#FFA0A0', '#A0A0FF'])
cm_dark = mpl.colors.ListedColormap(['g', 'r', 'b'])
'''
#print 'grid_test = \n', grid_test
grid_hat = clf.predict(grid_test)       # 预测分类值
grid_hat = grid_hat.reshape(x1.shape)  # 使之与输入的形状相同

alpha = 0.5
plt.pcolormesh(x1, x2, grid_hat, cmap=cm_light)     # 预测值的显示
plt.scatter(x[:, 0], x[:, 1], c=np.squeeze(y), edgecolors='k', s=50, cmap=cm_dark)  # 样本
#plt.plot(x[:, 0], x[:, 1], 'o', color='blue',alpha=alpha, markeredgecolor='k')
plt.scatter(x_test[:, 0], x_test[:, 1], s=120, facecolors='none', zorder=10)  # 圈中测试集样本
plt.xlabel(u'花萼长度', fontsize=13)
plt.ylabel(u'花萼宽度', fontsize=13)
plt.xlim(x1_min, x1_max)
plt.ylim(x2_min, x2_max)
plt.title(u'鸢尾花SVM二特征分类', fontsize=15)
#plt.grid() #网格
'''
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
xs = x[:, 0]
ys = x[:, 1]
fs = x[:, 2]
print(type(y))
#X, Y = np.meshgrid(X, Y)
#R =
zs = x[:,2]
def showme(x):
    print(type(x))
    print(x.shape)
    print(x)
showme(xs)
showme(ys)
showme(zs)

ax = Axes3D(fig)
ax.scatter(xs, ys, zs,  marker='o',s=20*fs**2,c=np.squeeze(y), cmap=cm_dark)
plt.show()