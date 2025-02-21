# numpy库学习

[TOC]



## 数组基础

### 1.数据类型

一个numpy数组只容纳一种数据类型，以节约内存

简单分为整数和浮点数

```python
import numpy as np
arr1=np.array([1,2,3,4,5])
print(arr1)
arr2=np.array([1.0,2,3,4,5])
print(arr2)
```

同化定理

在整数型数组中插入浮点数，该浮点数会自动被截断成整数

在浮点型数组中插入整数，该整数会被自动截断成浮点数

```python
import numpy as np
arr1=np.array([1,2,3,4,5])
arr1[0]=100.4
print(arr1)
arr2=np.array([1.0,2,3,4,5])
arr2[0]=1
print(arr2)
```

共同改变定理

整数型数组和浮点型数组互相转化，方法是使用.astype()

```python
import numpy as np
arr1=np.array([1,2,3,4,5])
print(arr1)
arr2=arr1.astype(float)
print(arr2)
```

```python
import numpy as np
arr1=np.array([1,2,3,4,5])
arr2=np.array([1.0,2.0,3.0,4.0,5.0])
print(arr1+arr2)
print(arr1+0.0)
print(arr1*1.0)
print(arr1/1)
```

### 2.数组维度

一维/二维

一维数组用一层中括号表示，形状参数：x/(x)

二维数组用二层中括号表示，形状参数：(x,y)

三维数组用三层中括号表示，形状参数：(x,y,z)

np.one()表示括号的

.shape()表示形状

```python
import numpy as np
arr1=np.ones(3)
print(arr1)
arr2=np.ones((1,3))
print(arr2)
arr3=np.ones((1,1,3))
print(arr3)
print(arr1.shape)
print(arr2.shape)
print(arr3.shape)
```

数组维度转换

数组重塑的方法.reshape()

将一维数组升为二维

```python
import numpy as np
arr1=np.arange(10)
print(arr1)
arr2=arr1.reshape((1,10))
print(arr2)
```

将二维降为一维

```python
import numpy as np
arr1=np.arange(10).reshape(2,-1)
print(arr1)
arr2=arr1.reshape(10)
print(arr2)
```

一维数组称为向量，二维数组称为矩阵

## 数组的创建

### 1.创建指定数组

知道数组中每一个元素的值时，可以用np.array()函数，将列表转换成数组

```python
import numpy as np
arr1=np.array([1,2,3,4,5])#一维数组
print(arr1)
arr2=np.array([[1,2,3,4,5]])#二维数组
print(arr2)
arr3=np.array([[1],[2],[3],[4],[5]])#二维数组列矩阵
print(arr3)
arr4=np.array([[1,2,3],[4,5,6]])#
print(arr4)
```

### 2.创建递增数组

使用np.arange()函数创建

```python
import numpy as np
arr1=np.arange(10)#arr1=np.arange(10.0)
print(arr1)
arr2=np.arange(1,10)
print(arr2)
arr3=np.arange(1,10,2)
print(arr3)
```

### 3.创建同值数组

创建同值数组，用np.zeros()函数以及np.ones()函数

```python
import numpy as np
arr1=np.zeros((3,3))#全零数组
print(arr1)
arr2=np.zeros(3)
print(arr2)
arr3=np.ones((3,3))#全一数组
print(arr3)
arr4=np.ones(3)
print(arr4)
#要指定数字，就这样子
arr5=3*np.ones(3)
print(arr5)
```

都输出的是浮点型数组

### 4.创建随机数组

创建随机数组，用np.random系列函数

创建0-1范围内的数组

直接np.random函数

创建某一个特定的范围内的数组

用范围之差乘np.random在加上左范围

创建整数型随机数组

用np.random.randint也可以用random的然后再取整即可

创建服从正态分布的随机数组

np.random.normal

数字顺序依次为：

均值--标准差--形状

```python
import numpy as np
arr1=np.random.random((2,5))#0-1均匀分布的浮点型随机数组
print(arr1)
arr2=(100-60)*np.random.random((3,3))+60#创建某一个范围内的随机数60-100 三行三列数组
print(arr2)
arr3=np.random.randint(0,100,(3,3))#创建一个范围是0-100，形状为（3，3）的矩阵
print(arr3)
arr4=(100-0)*np.random.random((3,3))+0
arr4=arr4.astype(int)
print(arr4)
arr5=np.random.normal(0,1,(3,3))#创建一个形状为（3，3）的随机正态分布随机数组
print(arr5)
```

## 数组的索引

### 1.访问数组元素

与python列表一致，索引都是从0开始

访问向量

```python
import numpy as np
arr1=np.arange(1,10)
print(arr1)
print(arr1[3])#访问元素
print(arr1[-2])
arr1[4]=100#修改元素
print(arr1)
```

访问矩阵

```python
import numpy as np
arr1=np.array([[1,2,3],[4,5,6]])
print(arr1)
print(arr1[0,2])#访问元素
arr1[1,1]=100#修改元素
print(arr1)
```

### 2.花式索引

花式索引用两个中括号

```python
import numpy as np
arr1=np.arange(0,100,10)
print(arr1[[0,2]])#找到位置在0和2的两个元素
arr2=np.arange(1,17).reshape(4,4)
print(arr2)
print(arr2[[0,1],[1,2]])#找到在0行1列和1行2列的两个元素
print(arr2[[0,1,2],[1,2,3]])#找到三个元素，分别是0行1列，1行2列，2行3列
arr2[[0,1,2,3],[1,2,3,1]]=100#修改四个元素
print(arr2)
```

### 3.访问数组切片

向量的切片

```python
import numpy as np
arr1=np.arange(0,100)
print(arr1)
print(arr1[1:50])
print(arr1[1:50:2])
```

矩阵的切片

分行和列

```python
import numpy as np
arr1=np.arange(1,21).reshape(4,5)
print(arr1)
print(arr1[1:3,1:-1])#前面是行，后面是列
print(arr1[::3,::1])#跳跃切片
print(arr1[2,:])#提取整一行
print(arr1[1:3,:])#提取1到2行
print(arr1[:,1:3])#提取1到2列
print(arr1[:,1])#提取1列
cut=arr1[:,1]
cut=cut.reshape(-1,1)
print(cut)#变成列的
```

如果只提取一列出来，那么这一列是向量，如果要变成矩阵，还要进一步操作

和列表的切片差不多

### 4.数组切片仅是视图

numpy切片并不会创建新的变量

```python
import numpy as np
arr1=np.arange(10)
print(arr1)
cut=arr1[1:3]
print(cut)
cut[0]=100
print(cut)
print(arr1)
```

如果需要切片来创建新的变量，那么我们可以使用.copy()方法

```python
import numpy as np
arr1=np.arange(10)
print(arr1)
cut=arr1[1:3].copy()
print(cut)
cut[0]=100
print(cut)
print(arr1)
```

### 5.数组赋值仅是绑定

numpy数组之间的赋值并不会创建新的变量

```python
import numpy as np
arr1=np.arange(10)
print(arr1)
arr2=arr1
arr2[0]=100
print(arr1)
print(arr2)
```

这样做是为了节约空间，如果不想这样子，也是和上面一样，用.copy()方法

```python
import numpy as np
arr1=np.arange(10)
print(arr1)
arr2=arr1.copy()
arr2[0]=100
print(arr1)
print(arr2)
```

其实就是深拷贝和浅拷贝的内容



## 数组的变形

### 1.数组的转置

数组的转置.T只对矩阵有效,**遇到向量要先将其转化为矩阵**

向量的转置

```python
import numpy as np
arr1=np.arange(1,4)
print(arr1)
arr1=arr1.reshape(1,-1)#arr1=arr1.reshape(-1,1)一步到位
print(arr1)
arr1=arr1.T
print(arr1)
```

矩阵的转置

```python
import numpy as np
arr1=np.arange(1,17).reshape(4,4)
print(arr1)
arr1=arr1.T
print(arr1)
```

### 2.数组的翻转

数组的翻转有两个，

一个是上下翻转的np.flipud(),表示up-down，

一个是左右翻转的np.fliplr(),表示left-right

向量只能使用np.flipud()，因为在数学中，向量并不是横着排，，而是竖着排的

向量的翻转

```python
import numpy as np
arr1=np.arange(1,10)
print(arr1)
arr1=np.flipud(arr1)
print(arr1)
```

矩阵的翻转

```python
import numpy as np
arr1=np.arange(1,17).reshape(4,4)
arr1_ud=np.flipud(arr1)
arr1_lr=np.fliplr(arr1)
print(arr1)
print(arr1_ud)
print(arr1_lr
```

### 3.数组的重塑

想要重塑数组的形状，可以用**.reshape()**方法

给定了其他维度的数值，剩下一个维度可以填-1，剩下的让自己去算

向量的变形

矩阵的变形

### 4.数组的拼接

向量的拼接

两个向量拼接，可以得到一个加长版的向量

np.concatenate()

```python
import numpy as np
arr1=np.array([1,2,3])
print(arr1)
arr2=np.array([4,5,6])
print(arr2)
arr3=np.concatenate((arr1,arr2))
print(arr3)
```

矩阵的拼接

两个矩阵可以按不同的维度进行拼接，但是拼接的时候，要注意维度的吻合

```python
import numpy as np
arr1=np.array([[1,2,3],[4,5,6]])
print(arr1)
arr2=np.array([[7,8,9],[10,11,12]])
print(arr2)
arr3=np.concatenate((arr1,arr2))#这里默认axis=0，既是按行拼接
print(arr3)
arr4=np.concatenate((arr1,arr2),axis=1)#这里改为1，既是按列拼接
print(arr4)
```

向量和矩阵之间不能进行拼接，在拼接之前，我们必须把向量升级为矩阵

### 5.数组的分裂

向量的分裂

```python
import numpy as np
arr=np.arange(0,100,10)
print(arr)
arr1,arr2,arr3=np.split(arr,[2,8])
print(arr1)
print(arr2)
print(arr3)
```

矩阵的分裂

```python
import numpy as np
arr=np.arange(1,17).reshape(4,4)
print(arr)
arr1,arr2,arr3=np.split(arr,[1,3])#默认axis=0，既是按行分裂，若axis=1，既是按列分裂
print(arr1,'\n','\n',arr2,'\n','\n',arr3)
```

## 数组的运算

### 1.数组与系数之间的运算

其实是对每一个元素进行操作

```python
import numpy as np
arr=np.arange(1,9).reshape(2,4)
print(arr)
print(arr-10)
print(arr+10)
print(arr*10)
print(arr/10)
print(arr**2)
print(arr%10)
print(arr//6)
```

### 2.数组与数组之间的运算

也是对每一个元素进行操作，逐一

```python
import numpy as np
arr1=np.arange(-1,-9,-1).reshape(2,4)
arr2=-arr1
print(arr1)
print(arr2)
print(arr1+arr2)
print(arr1-arr2)
print(arr1*arr2)
print(arr1/arr2)
```

### 3.广播

不同形状的数组之间的运算

只讨论二维数组之内的情况

如果是向量和矩阵之间做运算，向量自动升级为行矩阵

如果某矩阵是行矩阵或者列矩阵，则其被广播，以适配另一个矩阵的形状

向量被广播

当一个形状为（x，y）的矩阵与一个向量做运算时，要求该向量的形状必须为y，运算时向量会自动升级成形状为（1，y）的行矩阵，该形状为（1，y）的行矩阵会自动被广播为形状为（x，y）的矩阵，这样就和另一个矩阵形状适配了

```python
import numpy as np
arr1=np.array([-100,0,100])
print(arr1)
arr2=np.random.random((10,3))
print(arr2)
print(arr1*arr2)
```

列矩阵被广播

```python
import numpy as np
arr1=np.arange(3).reshape(3,1)
print(arr1)
arr2=np.ones((3,5))
print(arr2)
print(arr1*arr2)
```

行矩阵列矩阵同时被广播

```python
import numpy as np
arr1=np.arange(3)
print(arr1)
arr2=np.arange(3).reshape(3,1)
print(arr2)
print(arr1*arr2)
```

## 数组的函数

### 1.矩阵乘积

np.dot()函数

向量与向量的乘积

```python
import numpy as np
arr1=np.arange(5)
print(arr1)
arr2=np.arange(5)
print(arr2)
print(np.dot(arr1,arr2))
```

向量和矩阵的乘积

从矩阵乘法角度上面看，按照线性代数中矩阵乘法的方法

```python
import numpy as np
arr1=np.arange(5)
print(arr1)
arr2=np.arange(15).reshape(5,3)
print(arr2)
print(np.dot(arr1,arr2))
```

矩阵和向量的乘积，同理

```python
import numpy as np
arr1=np.arange(15).reshape(3,5)
print(arr1)
arr2=np.arange(5)
print(arr2)
print(np.dot(arr1,arr2))
```

矩阵与矩阵之间的乘积

同理

### 2.数学函数

绝对值函数

三角函数

指数函数

对数函数

```python
import numpy as np
arr1=np.array([-100,100])
print(arr1)
print(np.abs(arr1))
theta=np.arange(3)*np.pi
print(theta)
print(np.sin(theta))
print(np.cos(theta))
print(np.tan(theta))
x=np.arange(1,4)
print(x)
print("e^x=",np.exp(x))
print("2^x=",np.power(2,x))
print("10^x=",10**x)
y=np.array([1,10,100,1000])
print(y)
print("ln(x)=",np.log(y))
print("log2(x)=",np.log(x)/np.log(2))
```



### 3.聚合函数

聚合很有用，向量与矩阵的用法一致，但是没有axis参数

最大值函数和最小值函数

max and min

求和函数和求积函数

sum and prod

均值函数和标准差函数

mean and std

```python
print(arr1)
print("按照维度1求最大值：",np.max(arr1,axis=0))
print("按照维度2求最大值：",np.max(arr1,axis=1))
print("求整体的：",np.max(arr1))
arr2=np.arange(10).reshape(2,-1)
print("按照维度1求和：",np.sum(arr2,axis=0))
print("按照维度1求和：",np.sum(arr2,axis=1))
print("求整体的：",np.sum(arr2))
print("按照维度1求积：",np.prod(arr2,axis=0))
print("按照维度1求积：",np.prod(arr2,axis=1))
print("求整体的：",np.prod(arr2))
print("按照维度1求均值：",np.mean(arr2,axis=0))
print("按照维度1求均值：",np.mean(arr2,axis=1))
print("求整体的：",np.mean(arr2))
```

考虑到大型数组可能有缺失值，于是我们在运用这些聚合函数的时候，可以在函数名前面加一个nan

例如：sum->nansum

## 布尔型数组

### 1.创建布尔型数组

布尔型数组产生离不开>,>=等符号

```python
import numpy as np
arr1=np.arange(1,7).reshape((2,3))
print(arr1)
print(arr1>4)
arr2=np.arange(1,7)
print(arr2)
arr3=np.flipud(arr2)
print(arr3)
print(arr2>arr3)
```

还可以同时比较多个条件

python中，同时检查多个条件的有：与，非，或是and not or

但是numpy里面 与 或 非分别是& | ~

```python
import numpy as np
arr=np.arange(1,10)
print(arr)
print((arr<4)|(arr>6))
```

### 2.布尔型数组中True的数量

有三个关于True数量的有用函数

分别是：np.sum() , np.any() , np.all()

sum用来统计所有符合条件的数量

```python
import numpy as np
arr1=np.random.normal(0,1,10000)
num=np.sum(np.abs(arr1)<1)
print(num)
```

any就是只要布尔型数组中含有一个及以上的True，就返回True

```python
import numpy as np
arr1=np.arange(1,10)
arr2=np.flipud(arr1)
print(np.any(arr1==arr2))
```

all就是要当布尔型数组中全是True的时候，才返回True

```python
import numpy as np
arr1=np.arange(1,10)
arr2=np.flipud(arr1)
print(np.all(arr1==arr2))
```

### 3.布尔型数组作为掩码

若一个普通数组和一个布尔型数组的维度相同，可以将布尔型数组作为普通数组的掩码，这样子可以对普通数组中的元素做筛选

筛选出数组中大于，等于或者小于某个数字的元素

```python
import numpy as np
arr=np.arange(1,13).reshape(3,4)
print(arr)
print(arr>4)
print(arr[arr>4])
```

这个矩阵进行掩码操作之后，退化为向量了

同维数组

```python
import numpy as np
arr1=np.arange(1,10)
arr2=np.flipud(arr1)
print(arr1>arr2)
print(arr1[arr1>arr2])
print(arr2[arr1>arr2])
```

### 4.满足条件的元素所在的位置

假设一个很长的数组，想知道满足某个条件的元素们所在的索引位置，使用np.where()函数

np.where()的输出看起来比较怪异，它是输出了一个元组，元组第一个元素是“满足条件所在位置”，第二个元素是数组类型，一般忽略

```python
import numpy as np
arr1=np.random.normal(500,70,1000)
print(np.where(arr1>650))
print(np.where(arr1==np.max(arr1)))
```









