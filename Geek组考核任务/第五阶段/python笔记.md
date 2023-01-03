# 1.python基本语法

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

# 2.python的数据类型

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

# 3.学会创建对象，方法定义和调用, 掌握面向对象的特性

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

# 4.文件操作

* open()
  * 打开一个文件，并返回文件对象。

* close()
  * 关闭文件。关闭后文件不能再进行读写操作。
* ![image-20230103212044855](https://github.com/Milefer7/geek_website.github.io/blob/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE_20230103_212042.png?raw=true)

* ![image-20230103212114811](https://github.com/Milefer7/geek_website.github.io/blob/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE_20230103_212108.png?raw=true)

# 5.了解如何利用Python爬取网站资源

* 通过视频大致了解：[5分钟学会Python爬取整个网站_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1k4411y7pB/?spm_id_from=333.337.search-card.all.click&vd_source=ca9a16185d415ab7fede2ae9ba6875e3)
  * ![image-20230103224142885](https://github.com/Milefer7/geek_website.github.io/blob/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE_20230103_224112.png?raw=true)

* **Python使用urllib,urllib3,requests库+beautifulsoup爬取网页**
  * [(4条消息) Python使用urllib,urllib3,requests库+beautifulsoup爬取网页_Eritque arcus的博客-CSDN博客_用urllib3爬取网页](https://blog.csdn.net/qq_40832960/article/details/103854145)
  * 其中的一些细则还未研究明白
    * urllib的request模块可以非常方便地抓取URL内容
    * urllib3是一个功能强大且友好的Python HTTP客户端
    * requests是一个Python第三方库，处理URL资源特别方便。

* 对于python爬虫实战遇到的问题会继续补充在这个文档里。未完待续。。。
