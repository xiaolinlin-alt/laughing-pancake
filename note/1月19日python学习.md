# 1月19日python学习

[TOC]

### 面向对象

python中一切皆是对象

设计者

 #### 类与实例化 

##### 定义

我们叫做class

对象：我们叫做object、instance

属性和方法：

我们通过类定义数据类型的属性（数据）和方法（行为），类将状态和行为打包在一起

属性（变量）-->状态

每个对象维持自己的属性

方法（函数）-->行为

同一个类创建的所有对象共享

**语法格式**

class 类名

​	类体

要点：

类名必须符合”标识符“的命名规则，一般规定，首字母大写，多个单词用驼峰原则

类体中我们可以定义属性和方法

属性用来描述数据，方法用来描述这些数据的相关操作

##### init构造方法和new方法

init（）的要点如下：
 名称固定，必须为：`__init__()`
 第一个参数固定，必须为：self。self指的就是刚刚创建好的实例对象
 构造函数通常用来初始化实例对象的实例属性，如下代码就是初始化实例属性：name和 score

```python
def __init__(self, name, age):
    self.name = name
    self.age = age
```

 通过“类名（参数列表）”来调用构造函数。调用后，将创建好的对象返回给相应的变量。
比如：s1 =Student("张三"，80）
`__init__()`方法：初始化创建好的对象，初始化指的是：“给实例属性赋值”
`__new__()` 方法：用于创建对象，但我们一般无需重定义该方法
 如果我们不定义 `__init__` 方法，系统会提供一个默认的`__init__` 方法

如果我们定义了带参的`__init__`  方法，系统不创建默认的`__init__` 方法

##### 实例方法

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def call_name(self):
        print(self.name)

s1=Student("lin",18)
print(s1.name,s1.age)
s1.call_name()
```

其他操作：

`dir(obj)`可以获得的所有属性、方法

`obj._dict_`对象的属性字典

`pass`空语句

`isinstance（对象，类型）`判断对象是不是指定类型

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def call_name(self,c):
        print(c)
        print(self.name)

s1=Student("lin",18)
print(s1.name,s1.age)
s1.call_name(68)
print(dir(s1))
print(s1.__dict__)
print(isinstance(s1,Student))
```

#### 类变量以及方法 

类对象 静态方法

```python
class Student:
    pass

print(type(Student))
print(id(Student))
print(Student)

stu=Student()
print(stu)
```

类属性

```python
class Student(object):
    university="gdut"	#类属性
    count=0
    def __init__(self,name,age):
        self.name=name	#实例属性
        self.age=age
        Student.count+=1

    def say_age(self):	#实例方法
        print("my university is:",Student.university)
        print("my age is ",self.age)

s1=Student("lin",18)	#实例对象
s2=Student("li",19)
s1.say_age()
s2.say_age()
print("一共创建{0}个Student对象".format(Student.count))
```

类方法

语法：

@classsmethod

def 类方法名(cls [,形参列表])：

​	方法体



静态方法

语法：

@staticmethod

def 静态方法名(形参列表)

​	方法体

与列对象无关，但是用的时候还是要通过它去调用

`__del__`函数删除对象

`__call__`

####  私有变量和私有方法 

双下划线开头的属性是私有的，其他是公开的

python对于类的成员没有严格的访问控制限制

类内部可以访问私有属性（方法）

类外部不能直接访问私有属性（方法）

类外部可以通过_类名__私有属性（方法）名访问私有属性（方法）

```python
class Employee:
    __company= "TXT"

print(dir(Employee))
print(Employee._Employee__company)
```

@property装饰器

可以将一个方法调用方式变成属性调用

主要用于帮助我们处理属性的读操作，写操作

直接操作数据不安全

```python
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        print("年龄是：",self.__age)
        return self.__age

emp1=Employee("John", 25)
print(emp1.age)
```



#### 封装 继承 多态

##### 继承

支持多重继承，一个子类可以继承多个父类



语法

class 子类类名(父类1)

##### 多态

