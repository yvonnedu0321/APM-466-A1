# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 12:16:14 2021

@author: Jinxtan
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('bonddata.csv') ## import data
header_name = df.columns.values.tolist()
Price = np.zeros((10,10))
for i in range(len(header_name[-10:])):
    Price[:,i] = df[header_name[-10:][i]]

FaceValue = df['Facevalue']
Term = df['Term']
zero_rate = np.zeros((10,10))

###### caluculate zero_rate ######
for i in range(10):
    for j in range(10):
        e4Calc = Price[i,j]/float(FaceValue[i])
        zero_rate[i,j] = np.log(e4Calc) / Term[i]

######## plt figure ######
fig = plt.figure(figsize=(10, 6),dpi=300)
ax = fig.add_subplot(111)
font1 = {'family':'Times New Roman','size':16}
y = zero_rate
plt.yticks(fontproperties = 'Times New Roman', size = 16)
plt.xticks(fontproperties = 'Times New Roman', size = 16)
plt.plot(y)
plt.xlabel('CouponFrequency',font1)
x_label = []
for i in range(10):
    x_label.append(str(df['Term'][i]) + '--'+ str(df['time'][i]))
ax.axes.set_xticklabels(x_label,rotation=0)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
plt.ylabel('Spot rate',font1)
plt.legend(header_name[-10:],prop = font1)
plt.title('2021-2025 Spot curve',font1)#命名
plt.savefig('vv.png')
plt.show()

    