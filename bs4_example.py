import requests
from bs4 import BeautifulSoup
import time
# import httpx
url = "https://cc0.cn/tags/bingqilin/"

header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 "
                  "Safari/537.36 "
}

# client = httpx.Client(http2=True)
# response = client.get(url, headers=header)
# print(response.text)
res = requests.get(url, headers=header)
res.encoding = "utf-8"
# print(res.text)
main_page = BeautifulSoup(res.text, "html.parser")
img_list = main_page.find_all("a", attrs={"target": "_blank"})
n = 1
for item in img_list:
    href = item.get("href")
    # print(href)
    res1 = requests.get(href, headers=header)
    res1.encoding = "utf-8"
    sub_pape = BeautifulSoup(res1.text, "html.parser")
    img_url = sub_pape.find("a", attrs={"target": "_blank"}).get("href")
    print(img_url)
    res2 = requests.get(img_url, headers=header).content
    path = "./img/" + f"{n}.jpg"
    f = open(path, 'wb')
    f.write(res2)
    time.sleep(2)  # 缓一会儿 2秒
    f.close()
    print(f"第{n}张冰激凌图片下载好了")
    n = n + 1
    # break
