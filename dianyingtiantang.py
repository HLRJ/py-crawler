# 1.提取到主页面中的每一个电影的背后的那个url地址
#       1.拿到"bikan"那一块的HTML代码
#       2.从刚才拿到的HTML代码中提取到href的值
# 2.访问子页面，提取到电影的名称以及下载地址
import csv
import re

import requests

url = "https://www.dy2018.com/"

header = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
}
res = requests.get(url, headers=header)
res.encoding = "gbk"
# print(res.text)

#1.提取必看热片部分的HTML代码
obj1 = re.compile(r"2022必看热片.*?<ul>(?P<html>.*?)</ul>", re.S)

res1 = obj1.search(res.text)
html = res1.group("html")
# print(html.strip())
#2.提取标签的href的值
obj2 = re.compile(r"<li><a href='(?P<href>.*?)' title")
res2 = obj2.finditer(html)

obj3 = re.compile(r'<div id="Zoom">.*?<br />◎片　　名　(?P<pianming>.*?)<br />.*?'
                  r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<magnet>.*?)">', re.S)
#  1.创建文件对象
f = open('电影热片.csv', 'w', encoding='utf-8')

#  2.基于文件对象构建csv写入对象
csv_write = csv.writer(f)

#  3.构建列表头
csv_write.writerow(['片名', '下载链接'])

# 遍历网页
for item in res2:
#    print(f"{url}"+item.group("href"))
    child_url = url.strip("/") + item.group("href")
    child_resp = requests.get(child_url, headers=header)
    child_resp.encoding = 'gbk'

    res3 = obj3.search(child_resp.text)
    movie = res3.group("pianming")
    magnet = res3.group("magnet")
    # 写入文件
    csv_write.writerow([movie, magnet])

# 关闭文件
f.close()
