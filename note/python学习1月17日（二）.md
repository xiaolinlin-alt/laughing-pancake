[TOC]



## **三.序列 **

#### **字符串**

##### 创建字符串

字符串本质：字符序列

python不支持单字符类型，单字符也是作为一个字符串使用的

字符串编码：支持Unicode

使用内置函数**ord()**可以把字符转换成对应的Unicode码

使用内置函数**chr()**可以把十进制数字转换成对应的字符

~~~~python
print(ord('a'))
print(chr(78))
~~~~



空字符串和len()函数

python中允许空字符串的存在，不包含任何字符且长度为0

len()用于计算字符串中含有多少字符

~~~~python
c=""
print(len(c))
~~~~



**创建字符串的方法**

1.单双引号创建

```python
a="xaxbax"
print(a)
b='my name is "linyuying"'
print(b)
```

如果字符串里面需要用到单/双引号，我们可以用双/单引号创建字符串，或者用转义字符

2.连续用三个单引号或三个双引号，可以帮助我们创建多行字符串，在长字符串中会保留原始的格式

~~~~python
s="""
    I 
        Love
            China
"""
print(s)
~~~~



##### 转义字符

我们用**\+特殊字符**，实现一些难以用字符表示的效果

| 转义字符     | 描述       |
| ------------ | ---------- |
| （在行尾时） | 续行符     |
| \            | 反斜杠符号 |
| \\'          | 单引号     |
| \\"          | 双引号     |
| \b           | 退格       |
| \n           | 换行       |
| \t           | 横向指表符 |
| \r           | 回车       |

##### 字符串拼接

可以用+将多个字符串拼接起来

如果+两边都是字符串，则拼接

如果+两边都是数字，则加法运算

如果两边类型不同，则抛出异常

~~~~python
a="13"
b="14"
c=a+b
print(c)
~~~~

##### 字符串复制

~~~~python
a="my"
print(a*3)
~~~~

##### 不换行打印

有时候我们并不想换行，但是会自动换行，这个时候就需要我们通过参数**end+"任意字符串"**实现末尾添加任何内容

~~~~
print("hello",end="")
print("hello")
~~~~

##### 从控制台读取字符串

**input()**

~~~~
name=input("your name")
print("hello",name)
~~~~

##### 字符串替换

**repalce()**

字符串不可以改变，但是我们有时候需要替换某些字符，这是，只能通过创建新的字符串来实现

~~~~python
a="sabxasucb"
b=a.replace("sabxasucb","ansxnaso")
print(a)
print(b)
~~~~

也可以实现某一个字符的替换

~~~~python
a="sabxasucb"
b=a.replace("s","sb")
print(a)
print(b)
~~~~

**str()实现数字转型字符串**

str()可以帮助我们将其他数据类型转换为字符串

~~~~python
a=str(123)	#a="123"而不是123
print(a)**使用[]提取字符**
~~~~

##### 使用[]提取字符

指定偏移量，提取该位置的单个字符

正向

反向

~~~~python
a="ucbquxbu"
print(a[0],a[len(a)-1])
print(a[-1],a[-2])
~~~~

##### 切片slice操作

切片slice操作可以让我们快速的提取子字符串，标准格式为

**[起始偏移量start:终止偏移量end:步长step:]**

| 操作和说明       | 示例                        | 结果     |
| ---------------- | --------------------------- | -------- |
| [:]              | "abcdef"[:]                 | "abcdef" |
| [start:]         | "abcdef"[2:]                | "cdef"   |
| [:end]           | "abcdef"[:2]                | "ab"     |
| [start:end]      | "abcdef"[2:4]（包头不包尾） | "cd"     |
| [start:end:step​] | "abcdef"[1:5:2]             | "bd"     |

| 示例                                | 说明                                 | 结果                         |
| ----------------------------------- | ------------------------------------ | ---------------------------- |
| "abcdefghijklmnopqrstuvwxyz"[-3:]   | 倒数三个                             | "xyz"                        |
| "abcdefghijklmnopqrstuvwxyz"[-8:-3] | 倒数第八个到倒数第三个（包头不包尾） | "stuvw"                      |
| "abcdefghijklmnopqrstuvwxyz"[::-1]  | 步长为负，从右到左反向提取           | "zyxwvutsrqponmlkjihgfedcba" |

##### split()分割和join()合并

~~~~python
a=("I love you")
b=a.split()
print(b)
~~~~

~~~~~python
a=("I love you")
b=a.split("e")
print(b)
~~~~~

~~~~python
a=["aa","bb","cc"]
d="".join(a)
print(d)
~~~~

~~~~python
a=["aa","bb","cc"]
d="**".join(a)
print(d)
~~~~



##### 字符串驻留机制与字符串的比较

**字符串驻留：常量字符串只保留一份**

~~~~python
c="dd#"
d="dd#"
print(c is d)
~~~~

**字符串比较**

我们可以直接用==/！=对字符串进行比较，是否含有相同的字符

我们使用is/not is判断对象是否为同一个对象，比较的是对象的地址，id

成员运算符判断子字符串

in/not in判断某个字符是否在字符串中

##### 字符串常用方法汇总

* 查找

  ~~~~python
  a="uweibcsabxasxnskcbabxcjksaasxsa"
  ~~~~

  

  | 方法和使用示例     | 说明                         | 结果 |
  | ------------------ | ---------------------------- | ---- |
  | len(a)             | 字符串长度                   | 31   |
  | a.startswith("uw") | 以指定字符串开头             | True |
  | a.endswith("a")    | 以指定字符串结尾             | True |
  | a.find("b")        | 第一次出现指定字符串的位置   | 4    |
  | a.rfind("b")       | 最后一次出现指定字符串的位置 | 19   |
  | a.count("a")       | 指定字符串出现了几次         | 6    |
  | a.isalnum()        | 所有字符全是字母或数字       | True |

* 去除首尾信息

​	我们可以通过**strip()**去除字符串首尾指定的信息，通过**lstrip()**去除字符串左边指定信息，通过**rstrip(**)去除字符串右边指定信息

~~~~python
print("  love u  ".strip())
~~~~

* 大小写转换

  ~~~~python
  a="sayuvxas  gGICISDA"
  ~~~~

  | 示例           | 说明                 | 结果               |
  | -------------- | -------------------- | ------------------ |
  | a.capitalize() | 首字母大写           | Sayuvxas  ggicisda |
  | a.title()      | 每个单词都首字母大写 | Sayuvxas  Ggicisda |
  | a.upper()      | 所有字符转成大写     | SAYUVXAS  GGICISDA |
  | a.lower        | 所有字符转成小写     | sayuvxas  ggicisda |
  | a.swapcase()   | 所有字母大小写转换   | SAYUVXAS  Ggicisda |

* 格式排版

  center(),ljust(),rjust()这三个函数用于对字符串实现排版

  ~~~~python
  c="hello"
  print(c.ljust(20,"?"))
  ~~~~

* 特征判断方法

  | 方法      | 说明                                 |
  | --------- | ------------------------------------ |
  | isalnum() | 是否为字母或数字                     |
  | isalpha() | 检测字符串是否只由字母组成（含汉字） |
  | isdigit() | 检测字符串是否只由数字组成           |
  | isspace() | 检测是否为空白符                     |
  | isupper() | 是否为大写字母                       |
  | islower() | 是否为小写字母                       |

  ~~~~python
  a="fuwfuidcwb".isalnum()
  print(a)
  ~~~~

##### 字符串的格式化

**format()**

~~~~python
a="名字是：{0}，年龄是：{1}"
b=a.format("yy",18)
print(b)
~~~~

~~~~python
a="名字是：{name}，年龄是：{age}"
b=a.format(age=18,name="yy")
print(b)
~~~~

##### 填充与对齐

填充要跟对齐一起使用

^,<,>分别是居中，左对齐，右对齐，后面带宽度

：号后面带填充的字符，只能是一个字符，不指定的话默认是用空格填

##### 数字格式化

浮点数通过f，整数通过d进行需要的格式化

~~~~python
a="我是{0}，我的存款是{1:.2f}"
b=a.format("yy",12.3455)
print(b)
~~~~

##### 可变字符串

python中，字符串属于不可变对象，不支持原地修改，如果需要修改其中的值，只能创建新的字符串对象

确实需要修改，可以用**io.StringIO对象或array模块**

~~~~python
import io
s="ecbsuibcusd"
sio=io.StringIO(s)
print(sio.getvalue())
sio.seek(3)
sio.write("****")
print(sio.getvalue())
~~~~

---

#### **列表**

##### 介绍

列表是用于存储**任意数目，任意类型的数据**集合

列表是内置可变序列，是包含多个元素的有序连续的内存空间，列表的标准语法格式

a=[10,20,30,40]

10，20，30，40称为列表a的元素

a=[10,20,"abcd]

列表大小可变，根据需要随时增加或减小

| 方法                 | 要点         | 描述                                                        |
| -------------------- | ------------ | ----------------------------------------------------------- |
| list.append(x)       | 增加元素     | 将元素x增加到列表尾部                                       |
| list.extend(aList)   | 增加元素     | 将列表alist所有元素加到列表list尾部                         |
| list.insert(index,x) | 增加元素     | 在列表list指定位置index处插入元素x                          |
| list.remove(x)       | 删除元素     | 在列表list中删除首次出现的指定元素x                         |
| list.pop([index])    | 删除元素     | 删除并返回列表list指定为止index处的元素，默认是最后一个元素 |
| list.clear()         | 删除所有元素 | 删除列表所有元素，并不是删除列表对象                        |
| list.index(x)        | 访问元素     | 返回第一个x的索引位置，若不存在x元素抛出异常                |
| list.count(x)        | 计数         | 返回指定元素x在列表list中出现的次数                         |
| len(list)            | 列表长度     | 返回列表中包含元素的个数                                    |
| list.reverse         | 翻转列表     | 所有元素原地翻转                                            |
| list.sort            | 排序         | 所有元素原地排序                                            |
| list.copy            | 浅拷贝       | 返回列表对象的浅拷贝                                        |

##### 列表的创建

* 基本语法[]创建

  ~~~~python
  a=[10,20,"dwjkbd"]
  ~~~~

* list()创建

  range()创建整数列表

  语法格式：

  range([start,]end[,step])

  ~~~~python
  a=list(range(3,20,2))
  print(a)
  ~~~~

* 推导式生成列表

  涉及for和if语句

  ~~~~python
  b=[x*2 for x in range(100) if x%9==0]
  ~~~~

##### 列表元素的增加

一般在尾部添加，效率高

* **append()**

  ~~~~python
  a=[10,20]
  a.append(30)
  print(a)
  ~~~~

* +运算符操作

  但是并不推荐，因为创建了新的列表对象

  ```python
  a=[10,20]
  print(id(a))
  a=a+[50]
  print(id(a))
  ```

* **extend()**

  将目标列表的所有元素添加到本列表的尾部，属于原地操作，不创建新的列表对象

  ```python
  a=[10,20]
  b=[40,50]
  a.extend(b)
  print(a)
  ```

* **insert()**

  插入元素,将指定的元素插入到列表对象的任意制定位置，这样子会让插入位置后面所有的元素进行移动，影响处理速度

  ```python
  a=[10,20,30,50]
  a.insert(3,40)
  print(a)
  ```

* **乘法**

  ```python
  a=[10,20,30,50]
  b=a*3
  print(b)
  ```

##### 列表元素的删除

* **del删除**

  删除列表中指定位置的元素

  ```python
  a=[10,20,30,50]
  del a[2]
  print(a)
  ```

* **pop()**

​	pop()删除并返回指定位置元素，如果未指定位置则默认操作列表最后一个元素

```python
a=[10,20,30,40,50]
b1=a.pop()
print(a,b1)
b2=a.pop(2)
print(a,b2)
```

* **remove()**

  删除首次出现的元素，若不存在该元素抛出异常

  ```python
  a=[10,20,30,20,40,50]
  a.remove(20)
  print(a)
  ```

##### 访问元素

* **通过索引直接访问元素**

  索引区间不能超过长度

  ```python
  a=[10,20,30,20,40,50]
  print(a[2])
  ```

* index()

  获得指定元素在列表中首次出现的索引

  语法格式：index(value,[start,[end]])

  其中，start和end指定了搜索的范围

  ```python
  a=[10,10,10,20,40,30,50,50,20]
  a.index(20)	#3
  a.index(20,3)#3
  a.index(50,2,7)#6
  print(a.index(20))
  print(a.index(20,3))
  print(a.index(50,2,7))
  ```

#####  元素出现次数统计

**count()**

可以返回指定元素在列表中出现的次数

```python
a=[10,10,10,20,40,30,50,50,20]
print(a.count(10))#3
```

##### 列表长度统计

**len()**

可以返回列表长度，列表中包含元素的个数

```python
a=[10,10,10,20,40,30,50,50,20]
print(len(a))#9
```

##### 成员资格判断

可以用**count**方法，返回0则表示不存在，返回大于0则表示存在

也可以用in来判断，直接返回True或者False

```python
a=[10,10,10,20,40,30,50,50,20]
print(10 in a)
```

##### 切片

格式：

**[起始偏移量start:终止偏移量end:步长step:]**

```python
a=[10,10,10,20,40,30,50,50,20]
print(a[:])#[10, 10, 10, 20, 40, 30, 50, 50, 20]
print(a[1:4])#[10, 10, 20]
print(a[1:6:2])#[10, 20, 30]
print(a[::-1])#[20, 50, 50, 30, 40, 20, 10, 10, 10]
print(a[-5:-3])#[40, 30]
```

超过列表长度没关系

##### 列表的遍历

要用到循环，后面掌握也可以

```python
a=[10,20,30,40,50]
for i in a:
    print(i)
```

##### 复制列表所有元素到新列表对象

二者是不同的

```python
list1=[10,20,30]
list2=list1
print(id(list1))
print(id(list2))
```

```python
list1=[10,20,30]
list2=[]+list1
print(id(list1))
print(id(list2))
```

##### 列表排序

* 修改原列表，不建立新列表的排序

  ```python
  import random
  a=[20,10,30,40]
  print(a)
  a.sort()#升序排序
  print(a)
  a.sort(reverse=True)#降序排序
  print(a)
  random.shuffle(a)#随机排序
  print(a)
  ```

  

* 建立新列表的排序

  ```python
  a=[20,10,30,40]
  b=sorted(a)
  c=sorted(a,reverse=True)#注意格式
  print(a)
  print(b)
  print(c)
  ```

* reversed()返回迭代器

  了解

##### 其他内置函数

max,min，sum

用于返回列表中的最大最小值和总和

```python
a=[20,10,30,40]
print(max(a))
print(min(a))
print(sum(a))
```

##### 多维列表

```python
a=[
    [1,99,98],
    [2,97,100],
    [3,98,99],
]

for i in range(3):
    for j in range(3):
        print(a[i][j],end="\t")
    print()
```

#### **元组**

##### 介绍

元组和列表差不多

只不过

列表属于可变序列，可以任意修改列表中的元素

元组属于不可变序列，不能修改元组中的元素，因此，元组中没有增加，删除元素相关的方法

##### 元组的创建

* **通过()创建元组**

```python
a=(10,20,30)
b=10,20,30
print(type(a))
print(type(b))
```

* **通过tuple()创建元组**

  ```python
  a=tuple(range(3))
  b=tuple("abc")
  print(a)
  print(b
  ```

* **生成器推导式来创建元组**

  只用一次

  ```python
  a=(x for x in range(10))
  b=tuple(a)
  print(b)
  ```

​	用__ _next_ _ _()

##### 元组的元素访问计数和排序

* 和列表的基本上一致

  ```python
  a=(10,20,30)
  print(a[2])
  print(a.index(10))
  print(a.count(10))
  print(a[1:4])
  ```

* 列表关于排序的方法list.sorted()是修改原列表对象，元组没有此方法，如果要对元组进行排序，只能使用内置函数sorted(tupleObj)

  并生成新的列表对象

  ```python
  a=(10,20,30)
  b=sorted(a)
  print(b)
  ```

* zip()

  zip(列表1，列表2，列表3)将多个列表对应位置的元素组合成为元组，并返回这个zip对象

  ```python
  a=(10,20,30)
  b=(40,50,60)
  c=(70,80,90)
  d=zip(a,b,c)
  print(d)#zip object
  e=list(d)
  print(e)
  ```

#### **字典**

##### 介绍

字典是“键值对”的**无序可变序列**，字典中的每一个元素都是一个“键值对”，包含“键对象”和“值对象”

可以通过“键对象”实现快速获取，删除，更新对应的“值对象”

键是任意不可变的数据，如整数，浮点数，字符串，元组，不可重复

值可以是任意的数据，并且可以重复

##### 字典创建

* {}，dict{}来创建字典对象

  ```python
  a={"name":"lin","age":18}
  print(a)
  ```

  ```python
  a=dict(name="lin",age=18)
  print(a)
  ```

* zip()创建字典对象

  ```python
  k=["name","age"]
  v=["lin",18]
  a=dict(zip(k,v))
  print(a)
  ```

* fromkeys创建值为空的字典

  ```python
  a=dict.fromkeys(['a','b','c','d','e'])
  print(a)
  ```

##### 字典元素的访问

* 通过键获得值，若键不存在，抛出异常
* 通过**get()**方法获得值，推荐使用，指定键1不存在，返回None，也可以设定指定的键不存在时默认返回的对象
* 列出所有的键值对

* 列出所有的键/值

  ```python
  a={"name":"lin","age":18}
  print(a["name"])
  print(a.get("name"))
  print(a.items())
  print(a.keys())
  print(a.values())
  ```

* len()键值对的个数

* 检测一个”键"是否在字典中

  ```python
  print(len(a))
  print("name" in a)
  ```

##### 字典元素的添加，修改，删除

给字典新增“键值对”，如果键已经存在，则覆盖旧的键值对，如果键不存在，则新增“键值对”

```python
a={"name":"lin","age":18}
a["address"]="guangdong"
a["age"]=19
print(a)
```

使用update()将新字典中所有的键值对全部添加到旧字典中，如果key有重复，则直接覆盖

```python
a={"name":"lin","age":18}
b={"name":"chen","height":180}
a.update(b)
print(a)
```

字典中元素的删除，可以使用del()方法，或者clear()删除所有键值对，pop()删除指定键值对，并返回对应的值对象

```python
a={"name":"lin","age":18}
del a["age"]
print(a)
```

```python
a={"name":"lin","age":18}
a.clear()
print(a)
```

```python
a={"name":"lin","age":18}
a.pop("age")
print(a)
```

popitem():随机删除并返回该键值对，字典是无序可变序列，因此没有第一个元素，最后一个元素的概念，popitem弹出随机的项，因此字典并没有最后的元素或者其他顺序的概念，若想一个接一个的移除并处理项，这个方法十分有效

```python
a={"name":"lin","age":18}
a.popitem()
print(a)
```

##### 序列解包

序列解包可以用于元组，列表，字典，序列解包方便我们对多个变量赋值

```python
x,y,z=(10,20,30)
(a,b,c)=(10,20,30)
[m,n,p]=[10,20,30]
print(x,y,z,a,b,c,m,n,p)
```

序列解包用于字典时，默认是对键进行操作，如果需要对键值对操作的，则需要使用items(),如果需要对值进行操作，则需要使用values()

```python
a={"name":"lin","age":18}
x,y=a
print(x,y)
```

```python
a={"name":"lin","age":18}
x,y=a.values()
print(x,y)
```

```python
a={"name":"lin","age":18}
x,y=a.keys()
print(x,y)
```

```python
a={"name":"lin","age":18}
x,y=a.items()
print(x,y)
```

##### 表格数据使用字典和列表进行存储和访问

```python
r1={"name":"lin","age":18}
r2={"name":"li","age":19}
r3={"name":"wang","age":20}

tb=[r1,r2,r3]
print(tb)
print(tb[1].get("name"))

for i in range(len(tb)):
    print(tb[i].get("name"),tb[i].get("age"))
```

#### **集合**

##### 含义

集合是无序可变，元素不能重复，实际上，集合底层是字典实现，集合的所有元素都是字典中的**键对象，**因此是不能重复且唯一的

##### 集合的创建和删除

* 使用{}创建集合对象，并使用add()方法添加元素

  ```python
  a={3,5,7}
  a.add(9)
  print(a)
  ```

* 使用set(),将列表，元组等可迭代对象转换成集合，如果原来数据存在重复数据，则只保留一个

  ```python
  a={"a","b","c","b"}
  b=set(a)
  print(b)
  ```

* remove()删除指定元素，clear()清空整个集合

  ```python
  a={3,5,7,9}
  a.remove(5)
  print(a)
  ```

##### 集合运算

集合中也和高中集合的概念差不多，提供了并集，交集，差集等运算

```python
a= {1,3,"sxt"}
b={'he','it','sxt'}
print(a|b)#并集
print(a&b)#交集
print(a-b)#差集
```





