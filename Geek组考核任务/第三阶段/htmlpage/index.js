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