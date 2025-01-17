# python学习1月17日（一）

[TOC]

## **一.基础语法与缩进**

#### 注释

​       加#号/‘’‘或者”“”注释内容’‘’或者“”“”/直接用快捷键选中内容**ctrl+？键**

#### **python程序的构成**

程序--->模块--->语句

#### 缩进

用tab键缩进

![image-20250116170110577](https://yuyingcun.oss-cn-guangzhou.aliyuncs.com/typora/202501161701636.png)

#### 行连接符

用这个**/**

![image-20250116170347724](https://yuyingcun.oss-cn-guangzhou.aliyuncs.com/typora/202501161703748.png)

#### 对象

对象--->标识id（地址）+类型type（数据类型）+值value（数据信息）

对象本质：一个内存块，拥有特定的值，支持特定类型的相关操作

~~~~python
a=3
print(a)
print(id(a))
print(type(a))
b='ws'
print(b)
print(id(b))
print(type(b))
~~~~

![image-20250116171552627](https://yuyingcun.oss-cn-guangzhou.aliyuncs.com/typora/202501161715653.png)

#### 引用

引用（变量）（引用了对象的地址）**（不需要声明类型）**

变量位于栈内存

对象位于堆内存

#### 标识符

区分大小写

第一个字母必须是字母、下划线，其后是**字母、数字、下划线**

不能用关键字

关键字查询

~~~~python
help()
~~~~

keywords

![image-20250116172534160](https://yuyingcun.oss-cn-guangzhou.aliyuncs.com/typora/202501161725192.png)

#### **变量和简单赋值语句**

变量必须初始化之后才能被使用

变量删除与垃圾回收机制

~~~~python
a=3
del a
print(a)
~~~~

会报错

#### 常量

常量一般用大写

~~~~python
MAX=100
print(MAX)
MAX=120
print(MAX)
~~~~

#### 赋值

链式赋值

~~~~
X=Y=100
~~~~

系列解包赋值（可以用来实现变量值交换）

~~~~python
a,b=100,10
print(a,b)
a,b=b,a
print(a,b)
~~~~

<img src="https://yuyingcun.oss-cn-guangzhou.aliyuncs.com/typora/202501161748645.png" alt="image-20250116174835619" style="zoom:150%;" />

----

## **二.数字类型 **

#### **四种基本的类型**

python中变量没有类型，但是对象都有类型

| int  | float            | bool          | str                  |
| ---- | ---------------- | ------------- | -------------------- |
| 整数 | 小数 3.14/314e-2 | True or False | 单引号，双引号都可以 |

#### 数字和基本运算符

| 运算符   | 说明             | 示例               |
| -------- | :--------------- | ------------------ |
| +        | 加法             | 3+2=5              |
| -        | 减法             | 3-2=1              |
| *        | 乘法             | 1*2=2              |
| **/**    | **浮点数除法**   | **8/2=4.0**        |
| **//**   | **整数除法**     | **7//2=3**         |
| %        | 取余             | 7%4=3              |
| ******   | **幂**           | 2**3=8             |
| divmod() | 同时得到商和余数 | divmod(13,3)=(4,1) |

#### 整数进制

| 二进制          | 0b/0B     |
| --------------- | --------- |
| **十进制**      |           |
| **八进制0x/0X** | **0x/0X** |
| **十六进制**    | **0o/0O** |

**使用int()实现类型转换**

int(9.9)--->9

int(True)--->1

int("456")--->456

但是字符串应该2符合整数格式int("456abc")错误

#### 浮点数

使用**float()**实现类型转换

整数和浮点数运算结果是浮点数

round(value)可以返回四舍五入的值，但是不会改变原有的值，而是产生新的值

#### 增强赋值运算符

+=

比如a+=2等同于a=a+2



#### 时间的表示

从1970年1月1日0点0分开始

time.time显示的是时间，带小数点

如果改为int(timie.time())就是不带小数点的

~~~~python
import time
b=int(time.time())
print(b)
totalMinutes=b//60
print(totalMinutes)
totalHours=totalMinutes//60
print(totalHours)
totalDays=totalHours//24
print(totalDays)
totalYears=totalDays//365
print(totalYears)
~~~~

#### 海龟绘图，计算两点之间的距离

~~~~python
import turtle
import math

x1,y1=100,100
x2,y2=100,-100
x3,y3=-100,-100
x4,y4=-100,100

#绘制
turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.goto(x2,y2)
turtle.goto(x3,y3)
turtle.goto(x4,y4)

#计算起始点距离
distance=math.sqrt((x1-x4)**2+(y1-y4)**2)
turtle.write(distance)

turtle.done()

~~~~



#### 布尔值本质

在python中，true和false可以看成1/0，甚至可以进行相加减

有一些特殊的布尔类型值为False，例如

False，0，0.0，空值None，空序列对象（空列表，空元组，空集合，空字典，空字符串），空range对象，空迭代对象，其他情况则均为Ture

~~~~python
print(bool(""))	#False
print(bool(0))	#False
print(bool([]))	#False
print(bool(None))	#False
print(bool("False"))	#True
~~~~

#### **运算符**

##### 逻辑运算符

| 运算符 | 格式    | 说明                     |
| :----- | ------- | ------------------------ |
| and    | x and y | 两个一样才为真，否则为假 |
| or     | x or y  | 一个真就为真             |
| not    | not x   | 真变假，假变真           |

##### 比较运算符

==

!=

</>

<=/>=

在python里面，可以这样子

3<a<10

##### 位运算符

| 运算符 | 描述                                                         |
| ------ | ------------------------------------------------------------ |
| &      | 按位与运算符：参与运算的两个值，如果两个相应位都为1，则该位的结果为1，否则为0 |
| \|     | 按位或运算符：只要对应的二个二进制有一个为1时，结果就为1     |
| ^      | 按位异或运算符：当两对应的二进制相异时，结果为1              |
| ~      | 按位取反运算符：对数据的每个二进制取反，即把0变成1，1变成0   |
| <<     | 左移动运算符：运算数中的每个二进制全部左移若干位，由<<右边的数据指定移动的位数，高位丢弃，低位补0 |
| >>     | 右移动运算符：把>>左边运算数的每个二进制位全部右移若干位，>>右边的数指定移动的位数 |

~~~~python
a=0b1101
b=0b1001
c=a&b

print(bin(c))	#bin()表示成二进制
~~~~

##### 加法操作补充

数字相加	3+2=5

字符串拼接	"3"+"2"="32"

列表、元组等合并	[10,20,30]+[5,10,100]=[10,20,30,5,10,100]

##### 乘法操作补充

数字相乘	3*2=6

字符串复制	"sxt"*3="sxtsxtsxt"

列表、元组等复制	[10,20,30]*3=[10,20,30,10,20,30,10,20,30]

##### 同一运算符

is--->判断两个标识符是不是引用同一个对象

is not--->判断两个标识符是不是引用不同对象

is 与==的区别

is用于判断两个变量引用对象是否为同一个，既比较**对象的地址**

==用于判断**引用变量引用对象的值**是否相等

##### 成员运算符

in 如果在指定的序列中找到值返回True,否则返回False

int not 不在，则返回True

~~~~python
a=[10,20,30]
b=10
print(b in a)
~~~~

##### 运算符优先级问题

小括号多用

一般顺序

**位运算和算术运算>比较运算符>赋值运算符>逻辑运算符**















