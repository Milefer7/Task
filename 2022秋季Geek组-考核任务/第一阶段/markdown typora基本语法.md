# markdown学习（一级标题）

## 标题（二级标题）

### 三级标题

#### 四级标题

##### 五级标题

###### 六级标题（最多）



## 字体

 You are a kind person!(原版)

*You are a kind person!*

**You are a kind person!**（很2）

***You are a kind person!***

 ~~You are a kind person!~~



## 引用

> 把握时代潮流 加强团结合作 共创美好未来

> > 把握时代潮流 加强团结合作 共创美好未来
> >
> > > 把握时代潮流 加强团结合作 共创美好未来
> > >
> > > > 把握时代潮流 加强团结合作 共创美好未来



## 分割线

---



## 图片

### 本地图片导入
***本地图片的路径更改或丢失都会造成markdown文件调不出图***

![人物](C:\Users\hello\Desktop\pr学习\04-卡点插件的使用\图片素材\pexels-victor-freitas-772665.jpg)

>1. 将本地图片上传到github
首先在github中新建一个repo，然后git clone下来，然后把你想要的图片放到这个文件夹中然后上传，然后到GitHub中找到这个图片查看地址，在markdown中引用就好了。

>这种方法的优点就在于插入式很灵活，github没有墙，你的文章上传到各个平台，图片也都基本不会丢失或找不到，但缺点就在于图片的管理很不方便，图片一旦多起来，你的本地仓库将会变得很大，而且你的文章可能涉及很多方面，管理也不方便，不过，也算是一个比较理想的解决方案。

>2. 把图片存入markdown文件
用base64转码工具把图片转成一段字符串
把字符串填到基础格式中链接的那个位置。
由于图片转成base64编码，会非常的大，一般至少都要上千行，这个时候会发现插入的这一长串字符串会把整个文章分割开，非常影响编写文章时的体验。这时候就可以用参考式，把大段的base64字符串放在文章末尾，然后在文章中通过一个id来调用，文章就不会被分割的这么乱了。
这种方法的优点就是图片真的是不会丢啊，相当于直接将图片编码嵌入到文档中，但缺点也是显而易见的，就是base64编码实在是太长了啊，太长了，虽然可以放到文章结尾，但还是太长了，所以目前我还没找到更好的解决方法。

### 网页地址导入

![风景](https://ts1.cn.mm.bing.net/th/id/R-C.bf36b2266d98907d0854b198caaba385?rik=tRAqe3oVzQLYrA&riu=http%3a%2f%2fwww.ukutu.cn%2fupload%2f201603%2f23%2f201603230208535011.jpg&ehk=DGHUktoMUTdZ%2b9KWY%2fU8NrjqwrwhfpWEgMyNnKc%2fn%2bs%3d&risl=&pid=ImgRaw&r=0)



## 超链接 / 链接
### 超链接
[点击跳转到我的GitHub仓库：Tasks]([米勒弗7/任务 (github.com)](https://github.com/Milefer7/Tasks))
### 链接
只要是用尖括号包起来， Markdown 就会自动把它转成链接。 语法：
<http://example.com/>
效果如下：
http://example.com/

## 列表

### 有序排列

1. 7
2. 7
3. 7

### 无序排列

+ 
  + （按tab可以缩进）
    + （再按可以再缩进）
  + （shift+tab可返回上一级）



## 高亮

==jsoidfjsdf==



## 表格

| mon  | tue  | wen  | thu  | fri  |
| ---- | ---- | ---- | ---- | ---- |
| 1    | 2    | 3    | 4    | 5    |
|      |      |      |      |      |

~~但是我觉得还是右键选择插入表格更快一点~~  ==Ctrl+T==



## 代码

### 代码框   

```c
我是代码框
#include<stdio.h>
//比大小
int main()
{
	int a, b, c;

	printf("请输入a，b，c的值：\n");
	scanf("%d %d %d",&a,&b,&c);
	printf ("a为%d b为%d c为%d\n", a, b, c);
	
	int max = a;
	
	if (b >= c && b >= a)
	{
		max = b;
	}
	else if(c > a && c > b) 
	{
		max = c;
	}
	printf("最大的值是%d", max);
	return 0;
}
```

### 行代码

`printf("The correct answer is:%d", answer);`



## 上下标

### 上标

我是^上标^

### 下标

我是~下标~



## 常用快捷键（*我*不熟悉的）

+ 下划线：`Ctrl+U`
+ 下划线：`Ctrl+U`
+ 插入公式： `Ctrl + Shift + M`
+ 创建表格 ：`Ctrl+T`
+ 选中某句话 ：`Ctrl+L`
+ 选中某个单词 ：`Ctrl+D`
+ 搜索: `Ctrl+F`
+ 搜索并替换 ：`Ctrl+H`



## 表情

```text
以:开始，然后输入表情的英文单词,以：结尾，将直接输入该表情.例如：
:smile
:cry
:happy
```


## 字体字号
```text
<font face="黑体">我是黑体字</font>
<font face="微软雅黑">我是微软雅黑</font>
<font face="STCAIYUN">我是华文彩云</font>
<font color=red>我是红色</font>
<font color=#008000>我是绿色</font>
<font color=Blue>我是蓝色</font>
<font size=5>我是尺寸</font>
<font face="黑体" color=green size=5>我是黑体，绿色，尺寸为5</font>
```

<font face="黑体">我是黑体字</font>
<font face="微软雅黑">我是微软雅黑</font>
<font face="STCAIYUN">我是华文彩云</font>
<font color=red>我是红色</font>
<font color=#008000>我是绿色</font>
<font color=Blue>我是蓝色</font>
<font size=5>我是尺寸</font>
<font face="黑体" color=green size=5>我是黑体，绿色，尺寸为5</font>


## 公式使用
<https://xmind.cn/faq/question/equation/>
