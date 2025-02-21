# Pandas标签库学习

[TOC]

## 对象的创建

列表之于字典，类比numpy之于pandas

要导入可以用import pandas as pd

### 1.一维对象的创建

字典创建法

numpy中，用np.array()将列表转化为数组

同理

pandas中，通过pd.Series()将字典转化成Series对象

```python
import pandas as pd
dict_v={"a":15,"b":20.0}
print(pd.Series(dict_v))
```



数组创建法

直接给pd.Series()函数参数，需要两个参数，第一个参数是values（列表，数组，张量都可以），第二个参数是键index（索引）

```python
import pandas as pd
v=[0,1,2,3]
i=["a","b","c","d"]
print(pd.Series(v,index=i))
print(pd.Series(v))
```

要用中括号哦

### 2.一维对象的属性

有两个属性，values和index

```python
import pandas as pd
v=[1,2,3,4,5]
i=['a','b','c','d','e']
sr=pd.Series(v,index=i)
print(sr)
print(sr.index)
print(sr.values)
```

无论用什么，最后values都是数组

如果想要pandas退化为numpy库的时候，我们查看数值的属性就好了

### 3.二维对象的创建

二维对象面向矩阵，不仅有行标签index，还有列标签columns

字典创建法

```python
import pandas as pd
v1=[53,64,72,88]
i=["一号","二号","三号","四号"]
sr1=pd.Series(v1,index=i)
print(sr1)
v2=["男","女","男","女"]
sr2=pd.Series(v2,index=i)
print(sr2)
df=pd.DataFrame({"年龄":sr1,"性别":sr2})
print(df)
```

如果sr1和sr2的index不完全一致，那么二维对象的index就会取sr1和sr2的index交集，相应的，对象就会产生一定数量的缺失值（NAN

）

数组创建法

直接的创建方法是给pd.DataFrame函数参数，其需要三个参数，第一个参数是值values（数组），第二个参数是行标签index，第三个参数是列标签columns，其中，index和columns参数可以忽略

```python
import pandas as pd
import numpy as np
v=np.array([[53,"女"],[75,"男"],[78,"女"]])
i=[1,2,3]
c=["年龄","性别"]
df=pd.DataFrame(v,index=i,columns=c)
print(df)
```

### 4.二维对象的属性

有三个属性，values，index，columns

```python
import pandas as pd
import numpy as np
v=np.array([[53,"女"],[75,"男"],[78,"女"]])
i=[1,2,3]
c=["年龄","性别"]
df=pd.DataFrame(v,index=i,columns=c)
print(df)
print(df.index)
print(df.columns)
print(df.values)
```

## 对象的索引

pandas索引分为显式索引--是使用pandas对象提供的索引和隐式索引--是使用数组本身自带的从0开始的索引

索引器

loc   iloc

### 1.一维对象的索引

访问元素

```python
import pandas as pd
v=[0,1,2,3]
i=["a","b","c","d"]
sr=pd.Series(v,index=i)
print(pd.Series(v,index=i))
print(sr.loc[["a","b","c"]])
print(sr["a"])
```

```python
import pandas as pd
v=[45,78,54,67]
i=["a","b","c","d"]
sr=pd.Series(v,index=i)
print(pd.Series(v,index=i))
print(sr.iloc[1])
```

访问切片

```python
import pandas as pd
v=[45,78,54,67]
i=["a","b","c","d"]
sr=pd.Series(v,index=i)
print(pd.Series(v,index=i))
print(sr.iloc[0:3])
```

一对象的索引的索引器其实加不加无所谓了

### 2.二维对象的索引

二维对象不能去掉索引器，索引器必须存在

访问元素

```python
import pandas as pd
v1=[53,64,72,88]
i=["一号","二号","三号","四号"]
sr1=pd.Series(v1,index=i)
print(sr1)
v2=["男","女","男","女"]
sr2=pd.Series(v2,index=i)
print(sr2)
df=pd.DataFrame({"年龄":sr1,"性别":sr2})
print(df)
print(df.loc["一号","年龄"])
print(df.loc[["一号","三号"],["性别","年龄"]])
print(df.iloc[0])
```

访问切片

```python
print(df.loc["一号":"三号",:])
```



## 对象的变形

### 1.对象的转置

```python
import pandas as pd
v=[[45,67,89,66],["女","男","女","男"]]
i=["年龄","性别"]
c=["一号","二号","三号","四号"]
df=pd.DataFrame(v,index=i,columns=c)
print(df)
print(df.T)
```

### 2.对象的翻转

左右翻转和上下翻转

左右翻转

上下翻转

```python
import pandas as pd

i = ['1号', '2号', '3号', '4号']
v1 = [53, 64, 72, 82]
v2 = ['女', '男', '男', '女']
sr1 = pd.Series(v1, index=i)
sr2 = pd.Series(v2, index=i)
df = pd.DataFrame({'年龄': sr1, '性别': sr2})
print(df)
df_lr = df.iloc[:, ::-1]
print(df_lr)
df_ud = df.iloc[::-1, :]
print(df_ud)
```



### 3.对象的重塑

对象是有行列标签的，因此.reshape()就不再适用，因此对象的重塑没那么灵活

```python
import pandas as pd
i = ['1号', '2号', '3号', '4号']
v1 = [10,20,30,40]
v2 = ['女', '男', '男', '女']
v3=[1,2,3,4]
sr1 = pd.Series(v1, index=i)
sr2 = pd.Series(v2, index=i)
sr3 = pd.Series(v3, index=i)
print(sr1)
print(sr2)
print(sr3)
df=pd.DataFrame({"年龄":sr1,"性别":sr2})
print(df)
df["牌照"]=sr3
print(df)
```



### 4.对象的拼接

用pd.concat()函数，与np.concatenate()函数相似

```python
import pandas as pd
i1 = ['1号', '2号', '3号', '4号']
v1 = [10,20,30,40]
sr1=pd.Series(v1,index=i1)
i2=["5号","6号","7号"]
v2=[50,60,70]
sr2=pd.Series(v2,index=i2)
sr3=pd.concat([sr1,sr2])
print(sr3)
```

然后用is_unique来检查是否重复

一维对象和二维对象的合并

```python
import pandas as pd
v1=[10,20,30]
v2=["女","男","女"]
i=["一号","二号","三号"]
sr1=pd.Series(v1,index=i)
sr2=pd.Series(v2,index=i)
print(sr1)
print(sr2)
df=pd.DataFrame({"年龄":sr1,"性别":sr2})
print(df)
df["牌照"]=[1,2,3]
print(df)
df.loc["四号"]=[40,"男",4]
print(df)
```

二维对象的合并

依然用pd.concat()函数，不过多个axis参数

## 对象的运算

### 1.对象与系数之间的运算

```python
import pandas as pd
i=["一号","二号","三号"]
v=[45,67,79]
sr1=pd.Series(v,index=i)
print(sr1)
print(sr1+10)
```

```python
import pandas as pd
v1=[53,64,72,88]
i=["一号","二号","三号","四号"]
sr1=pd.Series(v1,index=i)
print(sr1)
v2=["男","女","男","女"]
sr2=pd.Series(v2,index=i)
print(sr2)
df=pd.DataFrame({"年龄":sr1,"性别":sr2})
print(df)
print(df["年龄"]+5)
```

### 2.对象与对象之间的运算

必须保证其都是数字型对象，两个对象之间的维度可以不同

一维对象之间的运算

```python
import pandas as pd
v1=[10,20,30,40,50]
i1=["一号","二号","三号","四号","五号"]
v2=[1,2,3]
i2=["一号","二号","三号"]
sr1=pd.Series(v1,index=i1)
sr2=pd.Series(v2,index=i2)
print(sr1)
print(sr2)
print(sr1+sr2)
print(sr1-sr2)
print(sr1*sr2)
print(sr1/sr2)
```

二维对象之间的运算

```python
import pandas as pd
v1=[[10,"女"],[20,"男"],[30,"男"],[40,"女"]]
v2=[1,2,3,6]
i1=["一号","二号","三号","四号"]
i2=["一号","二号","三号","六号"]
c1=["年龄","性别"]
c2=["牌照"]
sr1=pd.DataFrame(v1,index=i1,columns=c1)
sr2=pd.DataFrame(v2,index=i2,columns=c2)
print(sr1)
print(sr2)
sr1["加法"]=sr1["年龄"]+sr2["牌照"]
print(sr1)
```

这里可以用numpy里面的数学函数

创建布尔型数组也可以



## 对象的缺失值

### 1.发现缺失值

适用.isnull()方法

输出结果是布尔型数组

一维对象的

```python
import pandas as pd
v=[10,20,None,40]
i=[1,2,3,4]
sr=pd.Series(v,index=i)
print(sr)
print(sr.isnull())
```

二维对象的

```python
import pandas as pd
import numpy as np
v=np.array([[None,"女"],[75,None],[78,"女"]])
i=[1,2,3]
c=["年龄","性别"]
df=pd.DataFrame(v,index=i,columns=c)
print(df)
print(df.isnull())
print(df.notnull())
```

.notnull()来找不是none的值

### 2.剔除缺失值

剔除缺失值，我们用.dropna()方法，一维对象比较简单，二维对象则要分行和列

一维对象的

```python
import pandas as pd
v=[10,20,None,40]
i=[1,2,3,4]
sr=pd.Series(v,index=i)
print(sr)
print(sr.isnull())
print(sr.dropna())
```

二维对象的

一般删除行，不删去列

```python
import pandas as pd
import numpy as np
v=np.array([[None,"女"],[75,None],[78,"女"]])
i=[1,2,3]
c=["年龄","性别"]
df=pd.DataFrame(v,index=i,columns=c)
print(df)
print(df.isnull())
print(df.notnull())
print(df.dropna())
print(df.dropna(axis=1))
```

只要有一行有缺失值就全部删除有点缺陷，我们可以设定一个参数，当该行全部是NAN或者超过某一个设定的数值就删除

```python
import pandas as pd
v=[10,20,None,40]
i=[1,2,3,4]
sr=pd.Series(v,index=i)
print(sr)
print(sr.isnull())
print(sr.dropna())
print(sr.dropna(how='all'))
print(sr.dropna(thresh=1))
```



### 3.填补缺失值

.fillna()方法，实际的数据填充没有统一的方法

一维对象

```python
import pandas as pd
import numpy as np
v=[10,20,None,40]
i=[1,2,3,4]
sr=pd.Series(v,index=i)
print(sr)
print(sr.fillna(0))#用0填充
print(sr.fillna(method='ffill'))#用前值填充
print(sr.fillna(method='bfill'))#用后值填充
print(sr.fillna(np.mean(sr)))#用平均值
```

二维对象

```python
import pandas as pd
import numpy as np
v=np.array([[None,"女"],[75,None],[78,"女"]])
i=[1,2,3]
c=["年龄","性别"]
df=pd.DataFrame(v,index=i,columns=c)
print(df)
print(df.fillna(0))
print(df["年龄"].fillna(np.mean(df["年龄"])))
```

## 导入excel文件

### 1.创建excel文件

### 2.放入项目文件夹

记好路径

### 3.导入项目信息

 [python1.xlsx](D:\Desktop\python1.xlsx) 

```python
import pandas as pd

# 读取Excel文件
file_path = r'D:\Desktop\python1.xlsx' # 替换为你的Excel文件路径
sheet_name = 'Sheet1'  # 替换为你的工作表名称
df = pd.read_excel(file_path, sheet_name=sheet_name)

# 打印数据框内容
print(df)
```



## 数据分析

### 1.导入信息

### 2.聚合方法

在输出df时，对其使用.head()方法，使其仅输出前五行

```python
import pandas as pd

# 读取Excel文件
file_path = r'D:\Desktop\python1.xlsx' # 替换为你的Excel文件路径
sheet_name = 'Sheet1'  # 替换为你的工作表名称
df = pd.read_excel(file_path, sheet_name=sheet_name)

# 打印数据框内容
print(df)
print(df.head())
```

在numpy中的聚合函数在pandas中都能使用

```python
print(df.max())
```



### 3.描述方法

在数据分析中，用以上分发挨个查看太麻烦，可以用.describe()方法

直接查看所有聚合函数的信息

```python
print(df.describe())
```

### 4.数据透视

两个特征内的数据透视

用.pivot_table()方法

这是以泰坦尼克号的数据为例

```python
import pandas as pd

file_path=r"D:\Desktop\train.xlsx"
sheet_name="train"
df=pd.read_excel(file_path,sheet_name=sheet_name)

print(df.head())
```

![image-20250219140515784](https://yuyingcun.oss-cn-guangzhou.aliyuncs.com/typora/202502191405896.png)

![image-20250219140550410](https://yuyingcun.oss-cn-guangzhou.aliyuncs.com/typora/202502191405521.png)



```python
import pandas as pd

file_path=r"D:\Desktop\train.xlsx"
sheet_name="train"
df=pd.read_excel(file_path,sheet_name=sheet_name)

print(df.head())
print(df.pivot_table("Survived",index="Sex"))
print(df.pivot_table("Survived",index="Sex",columns="Pclass"))
```



![image-20250219141011195](https://yuyingcun.oss-cn-guangzhou.aliyuncs.com/typora/202502191410262.png)

![image-20250219141206647](https://yuyingcun.oss-cn-guangzhou.aliyuncs.com/typora/202502191412714.png)



多个特征的数据透视

这里如果把年龄和费用都加进去，数据会很分散，之前的那个性别和船舱等级可以按照类分，现在这个就不可以了，因此需要涉及到数据透视表配套的两个重要函数，pd.cut()和pd.qcut()

```python
age=pd.cut(df["Age"],[0,25,120])
print(df.pivot_table("Survived",index=["Sex",Age],columns="Pclass"))
```

也可以自动分哇

pd.qcut()

不过不建议自动分，后面写要自己分的份数

