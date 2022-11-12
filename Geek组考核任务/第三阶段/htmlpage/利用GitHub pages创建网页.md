# using **Github`Pages`展示页面**

* 我新建了另一个仓库`htmlpage`
* 里面存放了ccs，js，html的代码
* 通过setting-pages-branch-main-save搭建了一个page



## 关于js的使用

* 写网页时，关于js的部分参考了一下代码

```js
let myButton = document.querySelector('button');
let myHeading = document.querySelector('h1');

function setUserName() {
  let myName = prompt('请输入你的名字。');
  if(!myName) {
    setUserName();
  } else {
    localStorage.setItem('name', myName);
    myHeading.textContent = 'Mozilla 酷毙了，' + myName;
  }
}
```

**修改后，得到一下代码**

```js
let myButton = document.querySelector('button');
let myHeading = document.querySelector('h1');

function popOut() {
    let pop = prompt('准备好超越到侏罗纪世界了吗？yes/no');
    if(pop === 'yes')
        myHeading.textContent = '欢迎加入侏罗纪世界' ;
    else if(pop === 'no')
    myHeading.textContent = '都是成年人了，该成熟一点' ;
  }

myButton.onclick = function() {
    popOut();
 }
```

​	还是有一部分不理解

1. `pop === 'yes'`,这里pop不是`准备好超越到侏罗纪世界了吗？yes/no`吗？怎么会和`yes`相一致呢？
2. 还是有一些专有名词要多多了解