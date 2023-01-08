"""
url:https://itawenya.cn/

"""

# 爬取网页requests

import requests
url = "https://itawenya.cn/"
resp = requests.get(url)
# resp.encoding = 'gbk'    # 在中文网站，解码方式不一样会导致乱码，所以要手动把utf-8换成gbk
print(resp.status_code)  # 验证网页是否有反爬虫机制，如果结果是200，则没有。400就有。

html = resp.text
# print(html) 看看是否可以读取成功

# 解析网页BeautifulSoup
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
imgs = soup.find_all("img")
for img in imgs:
    src = img["src"]
    src = f"https://itawenya.cn/{src}" #f可以把两个字符串连接起来，{}把要连接的字符串包括起来
    print(src)

#保存图片
    import os
    filename = os.path.basename(src)
    with open(f"官网图片/{filename}", "wb") as f: #从网上下载文件图片用wb，因为都是二进制
        resp_img = requests.get(src) #重新请求网络，得到图片的二进制流
        f.write(resp_img.content) #如果的text是人工可以解读的文本，content是二进制流。所以如果是图片就用content
