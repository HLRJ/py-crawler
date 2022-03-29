# 1.拿到页面源代码
# 2.编写正则，提取页面数据
# 3.保存数据
# 4.利用re对数据进行提取
import re
import csv
import requests

url = "https://movie.douban.com/top250"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
}
# 拿到网页内容
res = requests.get(url, headers=headers)
page_text = res.text
# print(page_text)

# 编写正则表达式
# re.S 可以让正则中的.匹配换行符

obj = re.compile(r'<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?'  # 电影名
                 r'<p class="">.*?导演: (?P<daoyan>.*?)&nbsp.*?'  # 导演
                 r'主演: (?P<zhuyan>.*?)<br>'  # 主演
                 r'(?P<year>.*?)&nbsp.*?'  # 年份
                 r'<span class="rating_num" property="v:average">(?P<pingfen>.*?)</span>.*?'  # 评价分数
                 r'<span>(?P<renshu>.*?)人评价</span>', re.S)  # 评价人数

#  1.创建文件对象
f = open('top250.csv', 'w', encoding='utf-8')

#  2.基于文件对象构建csv写入对象
csv_write = csv.writer(f)

#  3.构建列表头
csv_write.writerow(['电影名', '导演', '主演', '年份', '评价分数', '评价人数'])

#  4.写入csv文件

res = obj.finditer(page_text)
for item in res:
    # print(item.group("name"))
    # print(item.group("daoyan"))
    # print(item.group("zhuyan"))
    # print(item.group("year").strip())
    # print(item.group("pingfen"))
    # print(item.group("renshu"))
    csv_write.writerow([f'{item.group("name")}',f'{item.group("daoyan")}',f'{item.group("zhuyan")}',
                        f'{item.group("year").strip()}',f'{item.group("pingfen")}',f'{item.group("renshu")}'])
#  5.关闭文件
f.close()