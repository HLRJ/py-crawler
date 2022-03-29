import requests
import json

url = "https://movie.douban.com/j/chart/top_list"

# 关键词存入字典中
params = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": "20"
}

# 伪装成浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"
}

res = requests.get(url, params=params, headers=headers)
# 获取响应数据，查询得到的是json格式
dic_obj = res.json()
# 持久化存储

fp = open("movies.json", "w", encoding="utf8")
json.dump(dic_obj, fp=fp, ensure_ascii=False)
print("结束")
