import csv
import json
import time

import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui, expected_conditions

#
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')  # 无头模式，服务器没有图形界面这个必须
chrome_options.add_argument('--disable-gpu')  # 不需要gpu加速
chrome_options.add_argument('--no-sandbox')  # 这个配置很重要
s = Service(executable_path='/usr/bin/chromedriver')  # 如果没有把chromedriver加入到PATH中，就需要指明路径
client = webdriver.Chrome(options=chrome_options, service=s)  # mac/linux 放在/usr/bin下 就不用写了


def start(cityName):
    url = f"https://zhaopin.baidu.com/?city={cityName}"
    client.get(url)
    input_search = client.find_element(by=By.CSS_SELECTOR, value='input[name="query"]')
    input_search.send_keys("python")
    # 向左滚动
    client.execute_script("var q=document.documentElement.scrollLeft=5000")
    # 点击搜索
    client.find_element(by=By.CSS_SELECTOR, value=".search-btn>i").click()
    time.sleep(10)
    client.execute_script("var q=document.documentElement.scrollTop=500")

    # 等待class_name 为listitem 的div元素出现
    ui.WebDriverWait(client, 60).until(
        expected_conditions.visibility_of_all_elements_located((By.CLASS_NAME, "listitem")),
        "listitem 的 div 元素没有出现"
    )
    # 向下滚动 10次
    for i in range(10):
        client.execute_script("var q=document.documentElement.scrollTop=50000")
        time.sleep(2)

    # 获取所有岗位信息
    items = client.find_elements(By.CSS_SELECTOR, ".listitem>a")
    #  1.创建文件对象
    f = open(f'{cityName}python招聘信息.csv', 'w', encoding='utf-8')

    #  2.基于文件对象构建csv写入对象
    csv_write = csv.writer(f)

    #  3.构建列表头
    csv_write.writerow(['招聘链接', "job_name", "salary"])

    #  4.写入csv文件
    for item in items:
        # 过滤广告
        data = item.find_element(By.TAG_NAME, "div").get_attribute("data-click")
        info_url = json.loads(data)["url"]  # 岗位详情链接
        title = item.find_element(By.CLASS_NAME, "title").text  # job名称
        salary = item.find_element(By.CSS_SELECTOR, ".salaryarea span").text  # 工资
        print(info_url, title, salary)
        csv_write.writerow([f'{info_url}', f'{title}', f'{salary}'])


if __name__ == '__main__':
    start("北京")
