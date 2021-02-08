# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 14:39:58 2021

@author: Jinxtan
"""
from datetime import datetime
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

rf = np.zeros((9, 10))
##### caluculate forward rate ######
for i in range(9):
    for j in range(10):
        start_time = datetime(2021,1,1)
        end_time1 = datetime.strptime(df['time'][i+1], '%Y-%m-%d')
        end_time2 = datetime.strptime(df['time'][i], '%Y-%m-%d')
        a1 = end_time1 - start_time
        rf_1 = zero_rate[i+1,j]*(a1.days/365)
        a2 = end_time2 - start_time
        rf_2 = zero_rate[i,j]*(a2.days/365)
        a3 = end_time1 - end_time2
        rf[i,j] = (rf_1 - rf_2) / (a3.days/365)

######## plt figure ######
fig = plt.figure(figsize=(14, 6),dpi=300)
ax = fig.add_subplot(111)
# plt.tight_layout()
font1 = {'family':'Times New Roman','size':16}
y = rf
plt.yticks(fontproperties = 'Times New Roman', size = 16)
plt.xticks(fontproperties = 'Times New Roman', size = 16)
plt.plot(y)
plt.xlabel('CouponFrequency',font1)
x_label = [' ']
for i in range(9):
    x_label.append(str(df['time'][i+1]))
ax.axes.set_xticklabels(x_label,rotation=0)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
plt.ylabel('Forward rate',font1)
plt.legend(header_name[-10:],prop = font1)
plt.title('2021-2025 Forward curve',font1)#命名
plt.savefig('forward.png')
plt.show()

    
