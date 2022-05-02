import csv
import re
import time

import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui, expected_conditions

header = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
}


# 拿到城市名字和城市招聘的链接
def get_all_city():
    url = "https://www.zhaopin.com/citymap"
    resp = requests.get(url, headers=header)
    if resp.status_code == 200:
        html = resp.text
        with open("city.html", "w") as f:
            f.write(html)
            f.close()
    resp.encoding = "utf-8"
    # print(f.read())
    #       使用bs4拿到链接
    # main_page = BeautifulSoup(resp.text, "html.parser")
    # city_list = main_page.find_all("a", attrs={"style": "font-size:14px;"})  # 拿到城市链接
    # #
    # print(city_list)
    # for item in city_list:
    #     href = item.get("href")
    #     print(href)
    # 使用正则拿到链接
    # 样例
    # </a></li><li class="cities-show__list--li"><a href="//sou.zhaopin.com/Jobs/searchresult.
    # ashx?jl=498&amp;sm=0&amp;p=1&amp;sf=0" class="cities-show__list--href" style="font-size:14px;">匈牙利
    # 正则项
    obj = re.compile(r'</a></li><li class=.*?<a href="(?P<href>.*?)" class=.*?style="font-size:14px;">(?P<name>.*?) ',
                     re.S)
    #  1.创建文件对象
    f = open('招聘城市链接.csv', 'w', encoding='utf-8')

    #  2.基于文件对象构建csv写入对象
    csv_write = csv.writer(f)

    #  3.构建列表头
    csv_write.writerow(['city_name', '招聘链接'])

    #  4.写入csv文件
    # 查找正则
    res = obj.finditer(resp.text)
    # 写入表
    for item in res:
        # href = item.group("href")
        # print(href)
        # name = item.group("name")
        # print(name)
        csv_write.writerow([f'{item.group("name")}', f'{"https:" + item.group("href")}'])

    f.close()


#

# 拿到城市的工作信息
def get_city_jobs():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')  # 无头模式，服务器没有图形界面这个必须
    chrome_options.add_argument('--disable-gpu')  # 不需要gpu加速
    chrome_options.add_argument('--no-sandbox')  # 这个配置很重要
    s = Service(executable_path='/usr/bin/chromedriver')  # 如果没有把chromedriver加入到PATH中，就需要指明路径
    client = webdriver.Chrome(options=chrome_options, service=s)  # mac/linux 放在/usr/bin下 就不用写了
    with open("招聘城市链接.csv", "r", encoding="utf-8") as csv_file:
        f_csv = csv.reader(csv_file)
        # 获取表头
        headers = next(f_csv)
        # 循环获取每一行的内容 并用浏览器
        for row in f_csv:
            # 第二列为链接  启动浏览器
            client.get(row[1])
            # 根据class_name 查询webElement  使用新的方法
            # input_search = client.find_element_by_class_name()
            input_search = client.find_element(by=By.CLASS_NAME, value="zp-search__input")
            # 使用关键字搜索
            input_search.send_keys("python")
            # 点击搜索
            client.find_element(by=By.CLASS_NAME, value="zp-search__btn--blue").click()
            time.sleep(10)  # 缓一会儿 10秒
            # 当前浏览器打开第二个窗口
            w2 = client.window_handles[1]
            client.switch_to.window(w2)
            # 点击登录  选择其他方式登录
            client.find_element(by=By.CLASS_NAME, value="register__passport-link-new").click()
            time.sleep(10)  # 缓一会儿 10秒
            # 等待 class_name 为 "contentpile_content" div元素的出现
            ui.WebDriverWait(client, 60).until(
                expected_conditions.visibility_of_all_elements_located((By.CLASS_NAME, "contentpile_content"))
            )
            # 判断当前查询的结果是否不存在
            nocontent = client.find_element(by=By.CLASS_NAME, value="contentpile_jobcontent_notext")
            if not nocontent:
                print("当前城市为查找到python岗位")
            else:
                # 提取查询结果
                pass


if __name__ == '__main__':
    get_all_city()
    get_city_jobs()
