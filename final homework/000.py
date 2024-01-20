import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import pandas as pd
import math
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
df1 = pd.read_csv("C:\homework\附件1. 电影评分.csv",encoding='gb18030')
# print(df1)
df2 = pd.read_csv("C:\homework\附件2. 电影票房.csv",encoding='gb18030')
df2 = df2.loc[(df2['总票房(元)']>=100000)&(df2['上映年份']>1950)]
# print(df2)
df3 = pd.read_csv("C:\homework\世界gdp总量.csv")
# print(df3)


df1_info = df1[['电影名称','评分']]
# print(df_info.head)
df2_info = df2[['电影名称','总票房(元)','上映年份']]
df_merge = pd.merge(left = df2_info,right = df1_info,on = '电影名称')
df = pd.merge(left = df_merge,right = df3,on = '上映年份')
df['相对票房指数'] = 0.0001 * (df['总票房(元)'] / df['世界gdp总量（万亿美元）'])
df['相对票房指数'] = df['相对票房指数'].apply(np.log)
#print(df)


p_X = df['相对票房指数']
p_Y = df['评分']
plt.figure(figsize = (10,5))
plt.scatter(p_X,p_Y,color='b',label = 'data')
plt.xlabel("相对票房指数")
plt.ylabel("评分")
plt.show()


r = pearsonr(df['相对票房指数'],df['评分'])[0]
print(r)