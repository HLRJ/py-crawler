import requests
import json

if __name__ == '__main__':
    # 指定url
    post_url = "https://fanyi.baidu.com/sug"
    # post_url = "https://fanyi.baidu.com/v2transapi?from="
    # UA伪装
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/99.0.4844.82 Safari/537.36"
    }
    # post请求
    word = input("请输入翻译的语句 :")
    data = {
        "kw": word
    }
    # 请求发送
    response = requests.post(url=post_url, data=data, headers=headers)
    # 获取响应数据，查询得到的是json格式
    dic_obj = response.json()
    # 持久化存储
    word = word + ".json"
    fp = open(word, "w", encoding="utf8")
    json.dump(dic_obj, fp=fp, ensure_ascii=False)
    print("结束")
