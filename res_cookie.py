import requests
#  处理cookie的一个模板
# 会话
session = requests.session()
data = {
    "账号" : "########",
    "密码" : "########"
}
url = ""

res = session.post(url, data=data)

print(res.text)

res = session.get(url)

# resquests
header = {
    "user-agent" : "dddd",
    "Cookie" : "url"
}
resp = requests.get(url,headers=header)

print(resp.text)