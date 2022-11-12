# CSS

## 学习理解CSS的作用

* CSS是**描述 HTML 文档样式的语言。**
* 它的作用是**描述应该如何显示 HTML 元素。**
* 它可以解决内容与表现分离的问题->可以极大提高工作效率

## 学习理解CSS选择器 【`此阶段学习通用选择器、元素选择器、类选择器、ID选择器即可`】

### 通用选择器

* 使用语法：

  ```css
  *
  {
      属性：值;
  }
  ```

* 用法：可选择所以元素/选择另一元素内的所有元素

### 元素选择器

* 使用语法：

  ```css
  p
  {
      属性：值;
  }
  ```

* 用法：可选择指定元素名称的所有元素。

### 类选择器

* 使用语法：

```css
.名字(自己取)
{
    属性：值;
}
```

* 用法：class选择器可以指定类的所有元素的样式。

### ID选择器

* 使用语法：

  ```css
  #名字
  {
      属性：值;
  }
  ```

  * 名字是你自己取得，如hello。

* 用法：id选择器可以为指定具有id的元素改变其样式。

## 能够利用CSS设置元素的基础样式，如大小、颜色、文字字体等

* padding:内边距

  margin：外边距

  * margin:  auto;

  * 可设置两个值，第一个代表上下；第二个代表左右
  * auto表示自动居中

* border：边框

  * `border: 10px solid red`表示设置为10像素红色实线边框。


![示意图](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics/box-model.png)

* width:页面宽
  * `width: 600px;`表示页面永远保持600像素宽

* background:改变页面颜色

  * ```css
    html{
        background-color: #00539F;
    }
    ```

  * `#00539F`表示的是颜色的代码

* color

  * 十六进制值`color: #FF0000`
  * RGB值`color:rgb(0,255,0)`
  * 颜色的名称`color:red;`

* text-shadow:可为文本提供阴影

  * 可设置4个值

    * 第一个值设置**水平偏移值**

    * 第二个值设置**垂直偏移值**

    * 第三个值设置**迷糊半径**

    * 第四个值设阴影的**基色**

* 文字字体：有以下若干属性

  * **字体大小**
    * `font-size:40px`
    * 1em=16px
  * **字体样式**
    * 正常`font-style:normal;`
    * 斜体`font-style:italic;`
  * **字体粗细**
    * 标准`font-weight:normal;`即为400
    * 粗体`font-weight:bold`即为700
    * 更粗`font-weight:bolder`
    * 更细`font-weight:lighter`

  

## 学习理解CSS的盒模型 

* 页面里大部分html元素都可以被看作若干层叠的盒子。

* 每一个元素的盒子里可以包括：边距，边框，填充和实际内容

  ![eg](https://www.runoob.com/images/box-model.gif)

  

##  CSS的5种position定位

1. **static**定位
   * 即没有定位，遵循正常的文档流对象
   * `position:static;`

2. **fixed**定位

   * 元素的位置相对于浏览器窗口是固定位置,即使窗口是滚动的它也不会移动.

   * ```css
     p.fixed
     {
         position:fixed;
         top:30px;
         right: 5px;        
     }
     ```

3. **relative**定位

   * 相对定位元素的定位是相对其正常位置。

   * ```css
     position:ralative;
     left:-20px;
     ```

   * 代码表示相对于原来元素的位置，向左移动20像素的位置。

   * left;right;top;bottom

4. **absolute**定位

   * 绝对定位的元素的位置相对于最近的已定位父元素

   * ```css
     position:absolute;
     left:100px;
     top:150px;
     ```

5. **sticky**定位

   * 其意思为粘性定位—根据用户的滚轮滚动会固定在目标位置

   * ```css
      position: sticky;
      top: 0px;
     ```

## `了解CSS常用的布局方式`

![yes](https://www.runoob.com/wp-content/uploads/2019/04/DBD1E737-47C5-445E-BFEC-7547210D88D5.jpg)

## `CSS的伪类`

* 伪类的语法：`selector:pseudo-class {property:value;}`
  * 实例：`a.red:visited {color:#FF0000;}`