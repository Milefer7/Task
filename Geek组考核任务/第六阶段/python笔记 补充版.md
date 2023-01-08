# python学习
***补充在第六点***
## 1.python基本语法

* 注释 

  * 单条注释：c语言不同`/~~~/`，python 的注释是以`#`号开头

  * 多行注释：

    ```'''
    '''
    这是第一条注释
    '''
    
    or
    
    """
    这是第二条注释
    """
    ```

    

* 代码块

  * 与c语言不同的是，python不用`{}`来表示代码块

  * 只要靠缩进来表示代码块

    * 但是代码块内不同的缩进格数会导致运行错误

    * ```python
      if true:
          print("it is wonderful!")
      else:
          print("it is terrible.")
          print("correct answer:")
      错误的版本：
      if true:
          print("it is wonderful!")
      else:
          print("it is terrible.")
         print("correct answer:")#这里错了，没对齐
      

* 多行语句

  * 用[],{},().

    * ```
      arr=[1,2,3,
           4,5,6] 
      ```

  * 用反斜杠`\`

    * ```python
      a = 1 + 2 + \
          3 + 4 
      ```

* 数字类型
  * python中数字有四种类型
    * 整数
    * 布尔型 , 如 True
    * 浮点数，如 1.5
    * 复数
* 字符串 #引用菜鸟教程
  * **变量[头下标:尾下标:步长]**
  * 反斜杠可以用来转义，使用 **r** 可以让反斜杠不发生转义。 如 **r"this is a line with \n"** 则 **\n** 会显示，并不是换行。
  * 字符串可以用 **+** 运算符连接在一起，用 ***** 运算符重复。

```python
#引用菜鸟教程

1.word = '字符串'      
sentence = "这是一个句子。"
#Python 中单引号 ' 和双引号 " 使用完全相同。


2.paragraph = 
			"""
			这是一个段落，
			可以由多行组成
			"""
#使用三引号(''' 或 """)可以指定一个多行字符串。

```

* 在同一行使用多条语句，用`;`隔开就可以

## 2.python的数据类型

* Number（数字）

  * **int**

  * **float**

  * **bool**

  * **complex**（复数）

  * 在数字运算中，python特别有

    ```python
    数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数。

* String（字符串）

  * 第一块已经叙述过，下面补充一张图片，选自菜鸟教程
  * ![image-20230103152052953](https://github.com/Milefer7/geek_website.github.io/blob/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE_20230103_152050.png?raw=true)

* List（列表）

  * ![image-20230103160434784](https://github.com/Milefer7/geek_website.github.io/blob/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE_20230103_160429.png?raw=true)
  * List写在方括号之间，元素用逗号隔开。
  * List可以使用+操作符进行拼接。
  * List中的元素是可以改变的。**与tuple不同**

* Tuple（元组）

  * 元组的元素不能修改
  * 组写在小括号 **（）** 里
  * 元素之间用逗号隔开
  * 其中的一些细则与字符串类似

* Set（集合）

  * 可以使用大括号 **{ }** 或者 **set()** 函数创建集合
  * 创建一个空集合必须用 **set()** 而不是 **{ }**，因为 **{ }** 是用来创建一个空字典。

* Dictionary（字典）

  * 字典是一种映射类型，字典用 **{ }** 标识
  * 它是一个无序的 **键(key) : 值(value)** 的集合。

## 3.学会创建对象，方法定义和调用, 掌握面向对象的特性

* 创建对象

  * 对象包括两个数据成员（类变量和实例变量）和方法。
    * 类：类是相同的属性和方法的对象的集合
    * 方法：方法是类中定义的函数
  * 在使用类时，需要先定义类，然后再创建类的实例

* 方法定义

  * 定义类

    ```python
    class ClassName
    	'''类的帮助信息'''
    	statement
    ```

  * 创建类的实例

    ```python
    ClassName(paramenterlist)
    ```

  * 创建__init__()方法

    ```python
    def __init__(self, realpart, imagpart):
            self.r = realpart
            self.i = imagpart
    ```

* 类的私有属性

  * **__private_attrs**：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 **self.__private_attrs**。

## 4.文件操作

* open()
  * 打开一个文件，并返回文件对象。

* close()
  * 关闭文件。关闭后文件不能再进行读写操作。
* ![image-20230103212044855](https://github.com/Milefer7/geek_website.github.io/blob/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE_20230103_212042.png?raw=true)

* ![image-20230103212114811](https://github.com/Milefer7/geek_website.github.io/blob/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE_20230103_212108.png?raw=true)

## 5.了解如何利用Python爬取网站资源

* 通过视频大致了解：[5分钟学会Python爬取整个网站_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1k4411y7pB/?spm_id_from=333.337.search-card.all.click&vd_source=ca9a16185d415ab7fede2ae9ba6875e3)
  * ![image-20230103224142885](https://github.com/Milefer7/geek_website.github.io/blob/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE_20230103_224112.png?raw=true)

* **Python使用urllib,urllib3,requests库+beautifulsoup爬取网页**
  * [(4条消息) Python使用urllib,urllib3,requests库+beautifulsoup爬取网页_Eritque arcus的博客-CSDN博客_用urllib3爬取网页](https://blog.csdn.net/qq_40832960/article/details/103854145)
  * 其中的一些细则还未研究明白
    * urllib的request模块可以非常方便地抓取URL内容
    * urllib3是一个功能强大且友好的Python HTTP客户端
    * requests是一个Python第三方库，处理URL资源特别方便。

* 对于python爬虫实战遇到的问题会继续补充在这个文档里。未完待续。。。

## 6.实战补充

### 6.1 imput

* import语句用来导入其他python文件
* imput 导入的文件可以达到代码复用的目的
* 从某个模块中导入某个函数,格式为：`from somemodule import somefunction**`
  * `from bs4 import BeautifulSoup`
  * 这里也可以直接`import bs4`，但代码中每次用的时候都要写上包名bs4，如：bs4.BeautifulSoup 会更麻烦一些
  * python中“.”	表示层级调用


### 6.2 def

* def 是define的缩写
* def用来定义函数

#### 6.2.1函数定义

```python
def 函数名(参数,参数):
	函数主体
    函数主体
    函数主体
    return ~~
# 如果没有return python会自动返回none
```

#### 6.2.2函数调用

传参方式

* 位置传参定义

  def fun(x,y）调用 fun(1,2),按照参数定义顺序传入实参.

* 关键词传参

  def fun(x, y)，调用使用 fun(x=1, y=3)

  可不在意顺序

### 6.3 requests

* ![image-20230107160125864](https://github.com/Milefer7/geek_website.github.io/blob/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE_20230107_155832.png?raw=true)
* ![img](https://github.com/Milefer7/geek_website.github.io/blob/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE_20230107_155704.png?raw=true)

### 6.4 BeautifulSoup（解析文件）

1. 创建对象：`from bs4 import BeautifulSoup`

   ​					`soup = BeautifulSoup(`

   ​											   	 `html_doc,`		 # HTML文档字符串

   ​													`"html.parser",`	 #HTML解析器

   ​													`fome_encoding='utf8'`#HTML文档的编码

   ​		                                            `)   `                						                             

2. 搜索节点：

   * find_all(name,attrs,string)
     * name是节点的名称
     * attrs是节点的属性
     * string是节点的内容
       * 这三个可以对节点进行过滤
   * find

1. 访问节点：

![image-20230107220721178](C:\Users\hello\AppData\Roaming\Typora\typora-user-images\image-20230107220721178.png)

### 6.5 Anacanda3

* anacanda是一个安装、管理python相关包的软件
* 下载完之后进入系统高级设置path进行环境配置

### 6.6 os

* os库可以提供与操作系统的交互功能
* 使用os模块中提供的接口，可以实现跨平台访问

### 6.7 学习总结

* 与在学期中学习c语言的方式不同，在实验室的任务中，html，css，js，python等等语言的学习都不是先学习完模块全部内容，再进行实战练习，而是目的导向，在实战的过程中发现未知的知识点，再去学习，掌握它。
* 两种学习方法带来的成效是不一样的。第二种学习模式我更加喜欢。因为在探索中主动学习，不仅学习的效果更好，而且主动学习带来的学习感受与老师带着你走感觉大不相同。并且自主探索式学习带来的学习印象是十分深刻的。
* 实验室的学习任务让我收获颇多，感谢！
