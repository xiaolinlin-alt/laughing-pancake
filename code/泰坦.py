import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 读取Excel文件
file_path=r"D:\Desktop\train.xlsx"
sheet_name="train"
data = pd.read_excel(file_path,sheet_name=sheet_name)

# 显示数据头部信息
print(data.head)
#直接查看所有聚合函数的信息
print(data.describe())
#查看每一列的名
print(data.columns)
#查看每一列的数据类型
print(data.dtypes)
#查看表格的比例
print(data.shape)
#统计总体生还率
survived_counts = data['Survived'].value_counts()
print(survived_counts)

#数据可视化

#总体生还机率
#饼图
# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(10,10))
sizes=[survived_counts[0],survived_counts[1]]
labels=["死亡","生存"]
colors=["red","green"]
plt.pie(sizes,labels=labels,colors=colors,autopct='%.2f%%', startangle=140,pctdistance=0.4,labeldistance=0.6,shadow=True,explode=[0,0.1],textprops=dict(size=15))
plt.title("总体生还机率扇形图")
plt.show()
#性别对生还机率的影响
#统计出分性别的存活数
survived_by_gender_counts = data.groupby("Sex")['Survived'].value_counts()
print(survived_by_gender_counts)
#饼图
plt.figure(figsize=(2*5,5))
axes1=plt.subplot(1,2,1)
axes1.pie(survived_by_gender_counts.loc["female"][::-1],labels=["死亡","生存"],colors=["red","green"],autopct='%.2f%%',startangle=140,pctdistance=0.4,labeldistance=0.6,shadow=True,explode=[0,0.1],textprops=dict(size=15))
axes1.set_title("女性生还率")
axes2=plt.subplot(1,2,2)
axes2.pie(survived_by_gender_counts.loc["male"][::1],labels=["死亡","生存"],colors=["red","green"],autopct='%.2f%%',startangle=140,pctdistance=0.4,labeldistance=0.6,shadow=True,explode=[0,0.1],textprops=dict(size=15))
axes2.set_title("男性生还率")
plt.show()
#统计不同年龄段的生还机率
#条形统计图
age_range = data['Age']
print(age_range.min(),age_range.max())
# 各年龄阶段人数
age_num,_ = np.histogram(age_range,range=[0,80],bins=16 )
print(age_num)
# 各年龄阶段生还人数
age_survived = []
for age in range(5,81,5):
    survived_num = data.loc[(age_range>=age-5) & (age_range<=age)]['Survived'].sum()
    age_survived.append(survived_num)
print(age_survived)
# 绘制条形图
plt.figure(figsize=(12,6))
plt.bar(np.arange(2,78,5)+0.5,age_num,width=5,label='总人数',alpha=0.8)
plt.bar(np.arange(2,78,5)+0.5,age_survived,width=5,label='生还人数')
plt.xticks(range(0,81,5))
plt.yticks(range(0,121,10))
plt.xlabel('年龄', position=(0.95, 0), fontsize=15)
plt.ylabel('人数', position=(0, 0.95), fontsize=15)
plt.title('各年龄阶段人数和生还人数条形图')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.show()

#登港口对生还机率的影响Embarked
survived_by_Embarked_counts=data.groupby("Embarked")['Survived'].value_counts()
print(survived_by_Embarked_counts)
plt.figure(figsize=(3*5,5))
axes1=plt.subplot(1,3,1)
axes1.pie(survived_by_Embarked_counts["C"][::-1],labels=["死亡","生存"],colors=["red","green"],autopct='%.2f%%',startangle=140,pctdistance=0.4,labeldistance=0.6,shadow=True,explode=[0,0.1],textprops=dict(size=15))
axes1.set_title("在C口生还率")
axes2=plt.subplot(1,3,2)
axes2.pie(survived_by_Embarked_counts["Q"][::1],labels=["死亡","生存"],colors=["red","green"],autopct='%.2f%%',startangle=140,pctdistance=0.4,labeldistance=0.6,shadow=True,explode=[0,0.1],textprops=dict(size=15))
axes2.set_title("在Q口生还率")
axes3=plt.subplot(1,3,3)
axes3.pie(survived_by_Embarked_counts["S"][::1],labels=["死亡","生存"],colors=["red","green"],autopct='%.2f%%',startangle=140,pctdistance=0.4,labeldistance=0.6,shadow=True,explode=[0,0.1],textprops=dict(size=15))
axes3.set_title("在S口生还率")
plt.show()
#不同船舱等级对生还率的影响
survived_by_Pclass_counts=data.groupby("Pclass")['Survived'].value_counts()
print(survived_by_Pclass_counts)
plt.figure(figsize=(3*5,5))
axes1=plt.subplot(1,3,1)
axes1.pie(survived_by_Pclass_counts[1][::-1],labels=["死亡","生存"],colors=["red","green"],autopct='%.2f%%',startangle=140,pctdistance=0.4,labeldistance=0.6,shadow=True,explode=[0,0.1],textprops=dict(size=15))
axes1.set_title("1等的生还率")
axes2=plt.subplot(1,3,2)
axes2.pie(survived_by_Pclass_counts[1][::-1],labels=["死亡","生存"],colors=["red","green"],autopct='%.2f%%',startangle=140,pctdistance=0.4,labeldistance=0.6,shadow=True,explode=[0,0.1],textprops=dict(size=15))
axes2.set_title("2等的生还率")
axes3=plt.subplot(1,3,3)
axes3.pie(survived_by_Pclass_counts[1][::1],labels=["死亡","生存"],colors=["red","green"],autopct='%.2f%%',startangle=140,pctdistance=0.4,labeldistance=0.6,shadow=True,explode=[0,0.1],textprops=dict(size=15))
axes3.set_title("3等的生还率")
plt.show()
#不同票价乘客的生还情况
fare_count=data.groupby("Fare")['Survived'].value_counts()
print(fare_count)
# 重新组织 fare_count 以便于计算总人数
fare_count = fare_count.unstack(fill_value=0)
#各票价乘客总人数
# 计算每个票价的总人数
fare_count['Total'] = fare_count.sum(axis=1)
print(fare_count)
# 计算生还率和死亡率
fare_count['Survival_Rate'] = fare_count[1] / fare_count['Total']
fare_count['Death_Rate'] = fare_count[0] / fare_count['Total']
#乘客生还率与票价的关系散点图
#乘客死亡率与票价的关系散点图
plt.figure(figsize=(2*10,5))
axes1=plt.subplot(1,2,1)
axes1.scatter(fare_count.index, fare_count['Survival_Rate'], color='green')
axes1.set_title('乘客生还率和票价关系散点图')
axes1.set_xlabel('票价')
axes1.set_ylabel('生还率')
axes2=plt.subplot(1,2,2)
axes2.scatter(fare_count.index, fare_count['Death_Rate'], color='red')
axes2.set_title('乘客死亡率和票价关系散点图')
axes2.set_xlabel('票价')
axes2.set_ylabel('死亡率')
plt.show()






