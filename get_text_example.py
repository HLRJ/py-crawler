# User-Agent(请求载体的身份标识)
# UA伪装:让爬虫对应的请求载体身份标识伪装成某一款浏览器

import requests

if __name__ == '__main__':
    # 将伪装信息封装到一个字典中
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/99.0.4844.82 Safari/537.36 "
    }
    kw = input("enter a word: ")

    url = f"https://www.baidu.com/s?wd={kw}"
    # 处理url携带的参数, 动态封装到字典中


    # 请求返回一个网页对象
    response = requests.get(url=url, headers=headers)

    page_text = response.text
    fileName = kw + ".html"

    with open(fileName, "w", encoding="utf8") as fp:
        fp.write(page_text)
    print(fileName, "保存成功！！！")

