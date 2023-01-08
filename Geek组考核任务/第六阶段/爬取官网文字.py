

# 爬取网页requests
import requests
url = "https://itawenya.cn/"
resp = requests.get(url)
html = resp.text

# 解析网页BeautifulSoup
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

par = soup.select('p')
print(par)
print("*" *10)

h1 = soup.select('h1')
print(h1)
print("*" *10)

h2 = soup.select('h2')
print(h2)
print("*" *10)

QA = soup.select('#QA-a')
print(QA)
print("*" *10)


#保存文字
import os
with open("文字.txt", "w", encoding='utf-8') as f:
    f.write(str(par))
    f.write(str(h1))
    f.write(str(h2))
    f.write(str(QA))
