# matplotlib绘图库学习

[TOC]

```python
import matplotlib.pyplot as plt
```

## 绘图基础

### 1.绘制图像

绘制简单的直线图

```python
import matplotlib.pyplot as plt

f1=plt.figure()#创建新的图窗
x=[1,2,3,4,5]#数据的x值
y=[1,2,3,4,5]#数据的y值
plt.plot(x,y)#plot函数，先描点，再连线

plt.show()
```

### 2.保存图像

```python
import matplotlib.pyplot as plt

f1=plt.figure()#创建新的图窗
x=[1,2,3,4,5]#数据的x值
y=[1,2,3,4,5]#数据的y值
plt.plot(x,y)#plot函数，先描点，再连线
plt.savefig('plot.jpg')
plt.savefig(r"D:\python_image\plot.jpg")
plt.show()
```

### 3.两种画图方式

matlab方式和面向对象方式

一般用第一种，第二种知道就好了

```python
import matplotlib.pyplot as plt
#matlab方式
f1=plt.figure()#创建新的图窗
x=[1,2,3,4,5]#数据的x值
y=[1,2,3,4,5]#数据的y值
plt.plot(x,y)#plot函数，先描点，再连线
plt.show()

#面向对象方式
f2=plt.figure()#创建新的图窗
ax2=plt.axes()
ax2.plot(x,y)
plt.show()
```

两种方法



### 4.图窗与坐标轴

我们在画图之前一定要创建图窗

f1=plt.figure()#创建新的图窗

axes坐标轴



## 多图形绘制

### 1.绘制多线条

matlab方式

```python
import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y1=[1,2,3,4,5]
y2=[0,0,0,0,0]
y3=[-1,-2,-3,-4,-5]

#matlab方式
f2=plt.figure()
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)

plt.show()
```

面向对象方式

```python
import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y1=[1,2,3,4,5]
y2=[0,0,0,0,0]
y3=[-1,-2,-3,-4,-5]

f2=plt.figure()
ax2=plt.axes()
ax2.plot(x,y1)
ax2.plot(x,y2)
ax2.plot(x,y3)

plt.show()
```



### 2.绘制多子图

matlab

```python
import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y1=[1,2,3,4,5]
y2=[0,0,0,0,0]
y3=[-1,-2,-3,-4,-5]

#matlab方式
f1=plt.figure()
plt.subplot(3,1,1),plt.plot(x,y1)#子图是三行一列排布的，这个子图是第一个子图
plt.subplot(3,1,2),plt.plot(x,y2)
plt.subplot(3,1,3),plt.plot(x,y3)

plt.show()
```

面向对象

```python
import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y1=[1,2,3,4,5]
y2=[0,0,0,0,0]
y3=[-1,-2,-3,-4,-5]

f2,ax2=plt.subplots(3,1)
ax2[0].plot(x,y1)
ax2[1].plot(x,y2)
ax2[2].plot(x,y3)

plt.show()
```



## 图表类型

可以去官网上面看

### 1.图表类型

很多哇

### 2.二维图

二维图，只需要两个向量就可以绘制，其中，线性图可以替代其他所有二维图

```python
import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y1=[1,2,3,4,5]
y2=[0,0,0,0,0]
y3=[-1,-2,-3,-4,-5]

f1=plt.figure()
plt.plot(x,y1,color='r')
plt.plot(x,y2,color='b')
plt.plot(x,y3,color='g')

plt.show()
```

可以设置颜色



可以设置风格

linestyle()

```python
import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y1=[1,2,3,4,5]
y2=[2,3,4,5,6]
y3=[3,4,5,6,7]
y4=[4,5,6,7,8]
y5=[5,6,7,8,9]

f1=plt.figure()
plt.plot(x,y1,linestyle='-')
plt.plot(x,y2,linestyle='--')
plt.plot(x,y3,linestyle='-.')
plt.plot(x,y4,linestyle=':')
plt.plot(x,y5,linestyle='')

plt.show()
```

设置粗细

一般是0.5-3

```python
import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y1=[1,2,3,4,5]
y2=[2,3,4,5,6]
y3=[3,4,5,6,7]
y4=[4,5,6,7,8]
y5=[5,6,7,8,9]

f1=plt.figure()
plt.plot(x,y1,linewidth=0.5)
plt.plot(x,y2,linewidth=1)
plt.plot(x,y3,linewidth=1.5)
plt.plot(x,y4,linewidth=2)
plt.plot(x,y5,linewidth=3)

plt.show()
```

设置标记

用marker关键字

```python
import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y1=[1,2,3,4,5]
y2=[2,3,4,5,6]
y3=[3,4,5,6,7]
y4=[4,5,6,7,8]
y5=[5,6,7,8,9]

f1=plt.figure()
plt.plot(x,y1,marker='.')
plt.plot(x,y2,marker='o')
plt.plot(x,y3,marker='^')
plt.plot(x,y4,marker='s')
plt.plot(x,y5,marker='D')

plt.show()
```

标记尺寸可以用markersize关键字调整，其值3-9之间

### 3.网格图

需要一个矩阵

演示imshow函数

还可以配置颜色条

```python
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,10,1000)
l=np.sin(x)*np.cos(x).reshape(-1,1)

f1=plt.figure()
plt.imshow(l)
plt.colorbar()

plt.show()
```



### 4.统计图

仅演示hist函数，只因其它函数主要出现在数据分析领域。  

为避免将直方图hist 与条形图 bar 弄混，现说明：条形图bar 可用plot替 代；**hist 则是统计学的函数**，是为了看清某分布的均值与标准差。

```python
import matplotlib.pyplot as plt
import numpy as np
# 创建10000个标准正态分布的样本
data=np.random.randn(10000)

f1=plt.figure()
plt.hist(data)

plt.show()
```

在上述示例中，对该直方图求积分，其结果是个体的总数，即10000

区间个数

用  bins 参数即区间划分的数量，默认为10，现将其改为为30。

Alpha 参数表示透明度，默认为1，现将其改为为0.5。

color 表示直方图的颜色，这里进行更改。 

edgecolor 表示直方图边缘的颜色，这里改为白色。

图表类型  histtype 表示类型，默认为'bar'，现将其改为为'stepfilled'，图形浑然一体

```python
import matplotlib.pyplot as plt
import numpy as np
# 创建10000个标准正态分布的样本
data=np.random.randn(10000)

f1=plt.figure()
plt.hist(data,bins=30,alpha=0.5,color='#A2A2D0',edgecolor='#FFFFFF',histtype="stepfilled")#区间个数bins,透明的alpha,颜色color,边缘颜色edgecolor

plt.show()
```



## 图窗属性

### 1.坐标上下限

尽管Matplotlib会自动调整图窗为最佳的坐标轴上下限，但很多时候仍需手动设置，才能适应当时的情况。

现设置其坐标轴上下限，有两种方法：lim法与axis法。

lim法

```python
import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[1,2,3,4,5]

f1=plt.figure()
plt.plot(x,y)
plt.xlim([1,5])
plt.ylim([1,5])

plt.show()
```

axis 法

```python
import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[1,2,3,4,5]

f1=plt.figure()
plt.plot(x,y)
plt.axis([1,5,1,5])
plt.show()
```

还可以使用plt.axis('equal')使 x 轴与 y 轴的比例达到1:1，长度等长。 



### 2.标题与轴名称

```python
import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[1,2,3,4,5]

f1=plt.figure()
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')

plt.show()
```

当然，面向对象方式统一了这五个函数，结合成了一个，即  ax2.set( xlim=( ), ylim=( ), title=' ', xlabel=' ', ylabel=' ' ) 

### 3.图例

一般图例会出现在二维图与统计图中，网格图则用的是颜色条。

plt.legend() 

```python
import matplotlib.pyplot as plt

x = [ 1, 2, 3, 4, 5 ]
y1 = [ 1, 2, 3, 4, 5 ]
y2 = [ 0, 0, 0, 0, 0 ]
y3 = [ -1, -2, -3, -4, -5 ]

f1=plt.figure()
plt.plot(x,y1,label='y=x')
plt.plot(x,y2,label='y=0')
plt.plot(x,y3,label='y=-x')
plt.legend()

plt.show()
```

也可以这样子用

```python
import matplotlib.pyplot as plt

x = [ 1, 2, 3, 4, 5 ]
y1 = [ 1, 2, 3, 4, 5 ]
y2 = [ 0, 0, 0, 0, 0 ]
y3 = [ -1, -2, -3, -4, -5 ]

f1=plt.figure()
plt.plot(x,y1,)
plt.plot(x,y2)
plt.plot(x,y3)
plt.legend(['y1=x','y2=0','y3=-x'])

plt.show()
```

不要到label

legend 还有三个常用的关键字参数：loc、frameon和ncol。

 loc 用于表示图例位置，该关键字在upper、center、lower中选一个，在 left、center、right 中选一个，用法如 loc='upper right'，也可以 loc='best'。  

 frameon 用于表示图例边框，去边框是frameon=False。  

 ncol 用于表示图例的列数，默认是1列，也可以通过ncol=2调为2列



### 4.网格

给图形加上网格，美观又好看

当然，grid()函数还有color 与linestyle 两个参数，这与plot 里用法一致。

```python
import matplotlib.pyplot as plt

x = [ 1, 2, 3, 4, 5 ]
y1 = [ 1, 2, 3, 4, 5 ]
y2 = [ 0, 0, 0, 0, 0 ]
y3 = [ -1, -2, -3, -4, -5 ]

f1=plt.figure()
plt.plot(x,y1,)
plt.plot(x,y2)
plt.plot(x,y3)
plt.grid()

plt.show()
```

```python
plt.grid(color='#000000',linestyle='--') 
```



