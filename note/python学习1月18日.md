# python学习1月18日

[TOC]

## 控制语句与逻辑思维

控制语句：把语句组合成完成一定功能的小逻辑模块

三类：顺序、选择、循环

顺序结构：先执行a再执行b

选择结构：如果某条件成立，则

循环结构：如果某条件成立，则重复执行

### 选择结构

#### 含义

分为单分支，双分支，多分支

#### 单分支

if语句单分支表达式语法

**if  条件表达式:**

​	**语句/语句块**

#### 双分支

双分支结构的语法：

if 条件表达式：

​	语句1/语句块1

else:

​	语句2/语句块2

```python
num=input("输入一个数字：")
if int(num)<10:
    print(num)
else:
    print("数字太大")
```

三元条件运算符

条件为真时的值 if(条件表达式)else条件为假时的值

```python
num=input("输入一个数字：")
print(num if int(num)<10 else "数字太大")
```

#### 多分支

多分支选择结构语法：

if 条件表达式：

​	语句1/语句块1

elif 条件表达式2：

​	语句2/语句块2

elif 条件表达式3：

​	语句3/语句块3

else:

​	语句n/语句块n

```python
score=int(input("请输入一个整数（0-100）"))
grade=""
if(score<60):
    grade="不及格"
if(60<=score<80):
    grade="及格"
if(80<=score<90):
    grade="良好"
if(90<=score<=100):
    grade="优秀"
print("分数是{0}，等级是{1}".format(score,grade))
```

```python
score=int(input("请输入一个整数（0-100）"))
grade=""
if score<60:
    grade="不及格"
elif score<80:
    grade="及格"
elif score<90:
    grade="良好"
elif score<=100:
    grade="优秀"
print("分数是{0}，等级是{1}".format(score,grade))
```

#### 选择结构的嵌套

```python
score=int(input("请输入一个整数（0-100）"))
grade=""
if score>100 or score<0:
    score=int(input("输入错误！！请重新输入一个在0-100之间的数字"))
else:
    if score>=90:
        grade="A"
    elif score>=80:
        grade="B"
    elif score>=70:
        grade="C"
    elif score>=60:
        grade="D"
    else:
        grade="F"
print("score{0},grade{1}".format(score,grade))
```

### 循环结构

#### while

```python
num=0
while num<=10:
    print(num)
    num=num+1
```

```python
sum=0
num=1
while num<=100:
    sum=sum+num
    num+=1
print(sum)
```

#### for

可以用来遍历很多东西

字典啥的都可以

.keys().values().items()

```python
for x in range (10):
    print(x)
```

```python
for x in range (3,10,2):
    print(x)
```

```python
sum1=0
sum_even=0
sum_odd=0
for x in range (1,101):
    sum1=sum1+x
    if x%2==0:
        sum_even=sum_even+x
    else:
        sum_odd=sum_odd+x
print(sum1)
print(sum_even)
print(sum_odd)
```

#### 嵌套循环

```python
for x in range(5):
    for y in range(5):
        print(x,end="\t")
    print()
```

九九乘法表

```python
for x in range(1,10):
    for y in range(1,x+1):
        print("{0}*{1}={2}".format(x,y,x*y),end="\t")
    print()
```

打印表格数据

~~~~python
r1={"name":"lin","age":18}
r2={"name":"li","age":19}
r3={"name":"wang","age":20}

tb=[r1,r2,r3]
print(tb)
print(tb[1].get("name"))

for i in range(len(tb)):
    print(tb[i].get("name"),tb[i].get("age"))
~~~~

#### break语句

break语句可以用于while和for循环，用来结束整个循环，当有嵌套循环的时候，**break语句只能跳出最近的一层循环**

#### continue语句

用于结束本次循环，继续下一次，多层循环嵌套，应用于最近的一层循环

#### else 语句

while 佛如循环可以附带一个else语句，如果for while没有被break语句结束，则会执行else语句，否则不执行，语法格式：

**while 条件表达式：**

​	**循环体**

**else：**

​	**语句块**

**或者**

**for 变量 in 可迭代对象：**

​	**循环体**

**else：**

​	**语句块**

#### 循环代码优化

* 减少循环内部不必要的计算
* 嵌套循环中，减少内层循环的计算
* 局部变量查询较快，尽量使用局部变量

其他优化手段

* 连接多个字符串，使用join()而不用+
* 列表进行元素插入和删除，尽量在列表尾部操作

```python
import time

start=time.time()
for i in range(1000):
    result=[]
    for m in range(10000):
        c=i*1000
        result.append(c+m*100)

end=time.time()
print("耗时：{0}".format(end-start))

print("简单循环优化后：")

start2=time.time()
for i in range(1000):
    result2=[]
    c=i*1000
    for m in range(10000):
        result2.append(c+m*100)

end2=time.time()
print("耗时：{0}".format(end2-start2))
```

#### zip()并行迭代

```python
names=("lin","li")
ages=(18,15)

for name,age in zip(names,ages):
    print(name,age)

for i in range(len(names)):
    print("{0}--{1}".format(names[i],ages[i]))
```

```python
names=("lin","li")
ages=(18,15)

for name,age in zip(names,ages):
    print("{0}--{1}".format(name,age))
```

### 推导式

推导式是从一个或者多个迭代器快速创建序列的一种方法，它可以将循环和条件判断结合从而避免冗长的代码

#### 推导式类型

| 推导式类型                           | 作用                           |
| ------------------------------------ | ------------------------------ |
| 列表推导式                           | 帮助我们生成列表               |
| 字典推导式                           | 帮助我们生成字典               |
| 集合推导式                           | 帮助我们生成集合               |
| 生成器推导式（注意：不直接生成元组） | 生成生成器，通过生成器遍历元组 |

##### 列表推导式

语法：

**[表达式 for item in 可迭代对象]**

**或者：{表达式 for item in 可迭代对象 if 条件判断}**

```python
a=[x for x in range(1,10)]
print(a)
b=[x for x in range(1,10) if x%2==0]
print(b)
c=[x*2 for x in range(1,10)]
print(c)
d=[x for x in "abcdef"]
print(d)

f=[]
for x in range(1,10):
    if x%2==0:
        f.append(x)
print(c)
```

```python
cells=[(row,col) for row,col in zip(range(1,10),range(1,10))]
for cell in cells:
    print(cell)
```

##### 字典推导式

语法：

**{key_expression:value_expression for 表达式 in 可迭代对象}**

类似于列表推导式，字典推导式也可以增加if条件判断，for循环

```python
values=["北京","上海","广州","深圳"]

cities={id:city for id,city in zip(range(1,5),values)}
print(cities)
```

统计文本中字符出现的次数

```python
my_text="I love you,I love python"
char_count={c:my_text.count(c) for c in my_text}
print(char_count)
```

##### 集合推导式

语法，和列表的差不多，只不过用花括号

{表达式 for item in 可迭代对象}

或者：{表达式 for item in 可迭代对象 if 条件判断}

```python
a={x for x in range(1,100)}
print(a)
```

##### 生成器推导式（不直接生成元组）

直接用小括号提示的是”一个生成器对象“，显然，元组没有推导式

一个生成器只能运行一次，第一次迭代可以得到数据，第二次迭代发现数据已经没有了

```python
a=(x for x in range(1,100) if x%9==0)
for x in a:
    print(x,end=" ")
for x in a:
    print(x,end=" ")
```

### 练习：

1.绘制不同颜色的同心圆

```python
import turtle

p=turtle.Pen()
radius=[x*10 for x in range(1,11)]
my_colors=("red","green","blue","yellow")
p.width(4)

for r,i in zip(radius,range(len(radius))):
    p.penup()
    p.goto(0,-r)
    p.pendown()
    p.color(my_colors[i%len(my_colors)])
    p.circle(r)
    
turtle.done()
```



## 函数

#### 定义

函数是可重用的程旭代码块

函数的作用实现代码的复用，代码一致性

实现功能

#### 分类

1.内置函数：直接拿来使用，str(),list(),len()等

2.标准库函数:用import语句导入库

3.第三方库函数：python社区提供，用import语句导入库

4.用户自定义函数：用户自己定义

#### 语法

**def 函数名 （[参数列表]):**

​	**"文档字符串"#说明函数用来做什么**

​	**函数体/若干语句**

def-->define定义

```python
def add(a,b,c):
    """实现三个数相加，并返回和"""
    sum=a+b+c
    print(sum)
    return sum

add(1,2,3)
```



#### 要点：

* 我们用def来定义一个函数，然后就是一个空格和函数名

python执行def时，会创建一个函数对象，并绑定到函数名变量上

* 参数列表

  圆括号是形参，有多个参数用逗号隔开

  定义时形参不需要声明类型，也不需要指定函数返回值类型

  调用函数时实参要和形参一一对应

  ```python
  def print_max(a,b):
      """"比较两个数中的较大值，并且打印较大值"""
      if a>b:
          print(a)
          return a
      else:
          print(b)
          return b
  
  print_max(15,34)
  help(print_max)
  print(print_max.__doc__)#获得文档字符串的内容
  ```

* return返回值

  如果函数中包含return语句，则结束函数执行并返回值

  然后函数体中不包含return语句，则返回None值

  要返回多个值，使用列表，元组，字典，集合将多个值存起来即可

  打印星号

  ~~~~python
  def print_star(n):
      print('*'*n)
  
  print_star(3)
  ~~~~

  平均数

  ~~~~python
  def avg(a,b):
      return (a+b)/2
  
  a=avg(10,20)
  print(a)
  ~~~~

  返回一个列表

  ~~~~python
  def print_shape(n):
      s1="#"*n
      s2="&"*n
      return [s1,s2]
  
  c=print_shape(5)
  print(c)
  
  print(type(c))
  print(type(print_shape(5)))
  print(type(print_shape))
  ~~~~

* 调用函数之前，必须要先定义函数，即调用def创建函数对象

  内置函数对象会自动创建

  标准库和第三方库函数，通过import导入模块，会执行模块中的def语句

  

#### 变量作用域

nonlocal、global

* 全局变量

  在函数和类定义之外声明的变量，作用域为定义的模块，从定义位置知道模块结束

  全局变量降低了函数的通用性和可读性，应尽量避免全局变量的使用

  要在函数内改变全局变量的值，使用global声明一下

* 局部变量

​	在函数体中声明的变量

​	局部变量的引用比全局变量快，优先考虑使用

​	如果局部变量和全局变量同名，则在函数内隐藏全局变量，只使用同名的局部变量

找局部变量和全局变量的函数

```python
a=100

def func(a,b,c):
    print(a,b,c)
    print(locals())#打印输出的局部变量
    print(globals())#打印输出的全局变量

func(1,2,3)
```

#### 参数的传递

函数的参数传递本质上是从实参到形参的赋值操作

python中一切皆对象，所有赋值操作都是引用的赋值

所有参数都是引用传递，不是值传递

具体操作两类：

1.对可变对象进行写操作，直接作用于原对象本身

2.对不可变对象进行写操作，会产生一个新的对象空间，并用新的值填充这块空间

可变对象有：字典，列表，集合，自定义的对象等

不可变对象有：数字，字符串，元组，函数等

**传递不可变对象时，不可变对象里面包含的子对象是可变的，则方法内修改了这个可变对象，源对象也发生了变化**

~~~~python
a=(10,20,[5,6])
print("a:",id(a))

def test01(m):
    print("m:",id(m))
    m[2][0]=888
    print(m)
    print("m:",id(m))

test01(a)
print(a)
~~~~



```
import copy

def test_copy():
    a=[10,20,[5,6]]
    b=copy.copy(a)
    print(a)
    print(b)
    b.append(30)
    b[2].append(7)
    print(a)
    print(b)

def test_deepcopy():
    a=[10,20,[5,6]]
    b=copy.deepcopy(a)
    print(a)
    print(b)
    b.append(30)
    b[2].append(7)
    print(a)
    print(b)

test_copy()
test_deepcopy()
```



##### 浅拷贝和深拷贝

浅拷贝：拷贝对象，但不拷贝子对象的内容，只是拷贝子对象的引用

深拷贝：拷贝对象，并且会连子对象的内存也全部拷贝一份，对子对象的修改不会影响源对象

```python
import copy

def test_copy():
    a=[10,20,[5,6]]
    b=copy.copy(a)
    print(a)
    print(b)
    b.append(30)
    b[2].append(7)
    print(a)
    print(b)

def test_deepcopy():
    a=[10,20,[5,6]]
    b=copy.deepcopy(a)
    print(a)
    print(b)
    b.append(30)
    b[2].append(7)
    print(a)
    print(b)

test_copy()
test_deepcopy()
```

#### 参数

类型：

位置参数、默认值参数、命名参数、可变参数（*param、**param）、强制命名参数

位置参数：函数调用时，实参默认按位置顺序传递，需要个数和形参匹配，按位置传递的参数，叫位置参数

默认值参数：我们可以给一些参数设置默认值，这些参数在传递的时候就是可选的，称为默认值参数，放在位置参数后面

```python
def a1(a,b,c=10,d=20):
    print(a,b,c,d)
a1(10,20)
```

命名参数（关键字参数）：给名字的

```python
def a1(a,b,c):
    print(a,b,c)
a1(c=20,b=10,a=10)
```

可变参数：可变数量的参数

1.*param（一个星号），将多个参数收集到一个元组对象中

2.**param（两个星号），将多个参数收集到一个字典对象中

```python
def a1(a,b,*c):
    print(a,b,c)

def a2(a,b,**c):
    print(a,b,c)

a1(7,8,9,10)
a2(7,8,name="lin",age=18)
```

强制命名参数：

如果上面把带星号的放前面了，需要强制命名



#### map，lambda，fitter函数的使用

**map函数**

map 函数用于将一个函数应用于可迭代对象（如列表、元组等）的每个元素，并返回一个包含结果的迭代器。在 Python 中，`map` 函数的基本语法为 `map(function, iterable, ...)`。其中，`function` 是要应用的函数，`iterable` 是要处理的可迭代对象。

```python
# 使用自定义函数
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)
print(list(squared_numbers))  # 输出: [1, 4, 9, 16, 25]

# 使用 lambda 表达式
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x ** 2, numbers)
print(list(squared_numbers))  # 输出: [1, 4, 9, 16, 25]
```

- `map` 函数返回的是一个迭代器，如果需要列表，需要使用 `list()` 函数进行转换。
- `map` 函数可以接受多个可迭代对象作为参数，此时函数需要接受相应数量的参数。

**lambda函数**

lambda表达式可以用来声明匿名函数，是一种简单的在同一行中定义函数的方法，lambda函数实际生成了一个函数对象

lambda表达式只允许包含一个表达式，不能包含复杂语句，该表达式的计算结果就是函数的返回值

**基本语法：**

**lambda arg1，arg2，arg3...:   <表达式>**

arg1，arg2，arg3为函数的参数

<表达式>相当于函数体，运算结果是表达式的运算结果

```python
f=lambda x,y:x+y
print(f(1,2))
```

**fitter函数**

`filter` 函数用于从可迭代对象中**筛选出满足特定条件的元素**，并返回一个包含这些元素的迭代器。`filter` 函数的基本语法为 `filter(function, iterable)`。其中，`function` 是一个返回布尔值的函数，用于判断元素是否满足条件，`iterable` 是要处理的可迭代对象。

```python
# 使用自定义函数
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5]
even_numbers = filter(is_even, numbers)
print(list(even_numbers))  # 输出: [2, 4]

# 使用 lambda 表达式
numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # 输出: [2, 4]
```

#### 递归函数

自己调用自己

必须包含

1.终止条件

表示递归什么时候结束，一般用于返回值，不再调用自己

2.递归步骤

把第n步与第n-1步联系

```python
#阶乘
def a(n):
    if n==1:
        return 1
    else:
        return n * a(n-1)

a(5)
print(a(5))
```

#### 嵌套函数

在函数内部定义的函数



**函数内要用nonlocal声明局部变量，global声明全局变量**



#### LEGB规则

LEGB规则是Python中变量查找和作用域解析的核心规则，用于确定变量在代码中的定义位置和作用域。LEGB分别代表四个作用域层次，其查找顺序为：

1. **Local（局部作用域）** ：在当前函数或表达式内部定义的变量。
2. **Enclosing（嵌套作用域）** ：如果当前函数内部有其他嵌套函数，则这些嵌套函数的局部变量也属于当前作用域的一部分。
3. **Global（全局作用域）** ：在模块顶层定义的变量。
4. **Built-in（内置作用域）** ：Python内置的特殊变量和函数，如`len()`、`print()`等。





