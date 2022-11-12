# JavaScript

## 学习JavaScript基本语法

1. 初始化变量：

* 可以用let或var声明一个变量，但**建议**`在代码中尽可能多地使用 let，而不是 var。`
* 命名变量一般应该**坚持使用**`拉丁字符 (0-9,a-z,A-Z) 和下划线字符`
  * 不要以下划线开头
  * 不要以数字开头
  * 使用 ["小写驼峰命名法"](https://en.wikipedia.org/wiki/CamelCase#Variations_and_synonyms)
* 行末分号是一种良好的编程习惯。

2. 基本的运算符

* 与C语言相同：
  * `+`,`-`,`*`,`/`
  * 赋值符`=`
  * 取非`!`
* 与C语言不同
  * 判断两值是否相等`===`
  * 不等于`!==`

3. 条件语句

* 与C语言的语法一致
  * `alert`意思为警告。在web中会跳出一个弹窗。

```js
let coolMan = 'handsome';
if (coolMan === 'handsome') {
  alert('charming man');
} else {
  alert('He is a nice person.');
}
```

3. 函数

* 与C语言的语法一致：如果代码中有**变量名后加小括号 **`()` ，很可能就是一个函数。

  * 引用内置函数

  ```js
  let myVariable = document.querySelector('h1');
  alert('hello!');
  ```

  * 自定义函数

```js
function plus(num1, num2) {
  let result = num1 + num2;
  return result;
}
```



3. 事件

`事件能为网页添加真实的交互能力。它可以捕捉浏览器操作并运行一些代码做为响应。`

* 浅浅的了解

  * ```JS
    document.querySelector('html').onclick = function() {
        alert('别戳我，我怕疼。');
    }
    ```

## 了解JavaScript数据类型

### 字符串（String）

* 字符串必须要用引号括起来（**单双引号**均可，这一点和c语言不大一样，`C语言是单个字符用单引号，多个字符用双引号`）
  * `let isLucky = 'geek yyds';`
  * `let isLucky = "geek yyds";`

### 数字（Number）

* 无需引号，直接赋值
  * `let isLucky = 667;`

### 布尔（Boolean）

* `true`/`false`是JS里的特殊关键词，无需引号。
  * `let isLucky = true;`
  * `let isLucky = false;`

### Null

* 在Boolean运算中被判定为`false`
* `null`表示丢失的对象

### Undefined

* `undefined`是未初始化的变量或对象属性的值
* `undefined`表示未初始化的状态

### 对象（Object）

* 对象是一个包含相关数据和方法的集合
* [现在没看很懂]([对象 - JavaScript |多核 (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object))这个网站以后再回过头来看

### 数组（Array）

* 其作用是可在单一引用中储存多个值
  * 赋值：`let isLucky = [1, 2, '哈哈哈'];`
  * 引用：`isLucky[0]`,` isLucky[1]`···

## 了解HTML/CSS/JavaScript三者之间的关系 

[(4条消息) HTML、 CSS、 JavaScript三者的关系_好剑者的博客-CSDN博客_html与css与js三者组合关系](https://blog.csdn.net/hemiaolin8393/article/details/80557781)**我觉得这个老哥讲的浅显易懂，我就copy下来了**

* 网页主要由三部分组成： 结构（ Structure） 、 表现（ Presentation） 和行为（ Behavior）
  * HTML —— 结构， 决定网页的结构和内容（ “是什么”）
  * CSS —— 表现（ 样式） ， 设定网页的表现样式（ “什么样子”）
  * JavaScript（ JS） —— 行为，  控制网页的行为（ “做什么”）

* html是主体，装载各种dom元素；css用来装饰dom元素；javascript控制dom元素。`用一扇门比喻三者间的关系是：html是门的门板，css是门上的油漆或花纹，javascript是门的开关`







