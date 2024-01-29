import datetime
import black.lines
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.linear_model import LogisticRegression


#定义数据读取路径
file='./DelayedFlights.csv'
#读取数据
df=pd.read_csv(file,index_col=0)
#以出发延误时间DepDelay作为飞机延误时间
#查看数据中的空值部分
col_null = df.isnull().sum(axis=0)
#print(col_null)
#输出飞机延误时间最长的十个航班

#delay=pd.DataFrame(df.nlargest(10,['DepDelay']),columns=['Year','Month','DayofMonth','FlightNum','DepDelay'])
#print(delay)
#print(df.DepDelay.describe())

#计算延误的和没有延误的航空公司的比例 >15算延误
#
# delay_bool=df['DepDelay']>15
# delay_num=delay_bool.sum()
# normal_num=df['DepDelay'].sum()-delay_bool.sum()
# print(df['DepDelay'].sum())
# print(delay_num)
# print(normal_num)
# print(delay_num/normal_num)

# #分析一天中、一周中延误最严重的飞行时间。
# #print(df.groupby(['Year','Month','DayofMonth'])['DepDelay'].max())
# #获取每天延误最严重的时间
# day=list(df.groupby([df['Year'],df['Month'],df['DayofMonth']])['DepDelay'].max())
# #创建标准的时间序列
# time_series_2008 = pd.date_range(start='2008-01-01', end='2008-12-31', freq='D')
# #print(time_series_2008)
# #将每天的延误时间输出为Excel文件
# #print(day)
# # plt.plot(time_series_2008, day, 'b*--', alpha=0.5, linewidth=1, label='acc')
# # plt.legend()  # 显示上面的label
# # plt.xlabel('time')  # x_label
# # plt.ylabel('number')  # y_label

# # plt.ylim(-1,1)#仅设置y轴坐标范围
# plt.show()
# #接下来求每周的延误时间
# #2008年1月1日为周二
# # day.insert(0,0)
# # week=[]
# # for i in range(0,len(day),7):
# #     week.append(max(day[i:i+7]))
# # print(week)
# # week_time=list(range(1,54))
# # plt.plot(week_time, week, 'b*--', alpha=0.5, linewidth=1, label='ang')
# # plt.legend()  # 显示上面的label
# # plt.xlabel('time')  # x_label
# # plt.ylabel('number')  # y_label
# # plt.show()
# #print(df.groupby([df['Year'],df['Month'],df['DayofMonth']])['DepDelay'].max())
# #display(day)
# #print(day)
# #3000英里以上算长途，其余算短程和中程
# #查看distance异常值
# #long=df['Distance']>700
# #short=df['Distance']<700
# #long_canceled=(df['Cancelled']==1)&(df['Distance']>700)
# #short_cancelled=(df['Cancelled']==1)&(df['Distance']<700)
# #print(long_canceled.sum()/long.sum())
# #print(short_cancelled.sum()/short.sum())

# #采用支持向量机进行预测
# #构造数据集，
# Y=pd.DataFrame(df,columns=['Cancelled']).values.ravel()
# X=pd.DataFrame(df,columns=['Distance','DepDelay'])
# print(X.info)
# print(Y)
# # 将数据集划分为训练集和测试集
# X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

# # 构建logic模型
# clf = LogisticRegression(random_state=0, solver='lbfgs')

# # 训练模型
# clf.fit(X_train, Y_train)

# train_predict = clf.predict(X_train)
# test_predict = clf.predict(X_test)
# print('The accuracy of the Logistic Regression is:',metrics.accuracy_score(Y_train,train_predict))
# print('The accuracy of the Logistic Regression is:',metrics.accuracy_score(Y_test,test_predict))






