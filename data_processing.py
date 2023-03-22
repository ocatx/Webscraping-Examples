# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 14:05:20 2023

@author: Administrator
"""
import pandas as pd
import matplotlib.pyplot as plt

# with open('allsides.json', 'r') as f:
#     data = json.load(f)

df = pd.read_json(open('allsides.json', 'r'))
df.set_index('name', inplace=True)

plt.style.use('seaborn-darkgrid')
df2 = df.head(25).copy()
fig, ax = plt.subplots(figsize=(20, 10))

ax.bar(df2.index, df2['agree'], color='#5DAF83')
ax.bar(df2.index, df2['disagree'], bottom=df2['agree'], color='#AF3B3B')

ax.set_ylabel = 'Total feedback'

plt.yticks(fontsize='x-large')
plt.xticks(rotation=60, ha='right', fontsize='x-large', rotation_mode='anchor')

plt.legend(['Agree', 'Disagree'], fontsize='xx-large')
plt.title('AllSides Bias Rating vs. Community Feedback', fontsize='xx-large')
plt.show()