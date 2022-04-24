from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')  # 无头模式，服务器没有图形界面这个必须
chrome_options.add_argument('--disable-gpu')  # 不需要gpu加速
chrome_options.add_argument('--no-sandbox')  # 这个配置很重要
s = Service(executable_path='/usr/bin/chromedriver')  # 如果没有把chromedriver加入到PATH中，就需要指明路径
client = webdriver.Chrome(options=chrome_options, service=s)

client.get("https://www.baidu.com")
print(client.page_source.encode('utf-8'))

client.quit()
