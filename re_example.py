import re

res = re.findall("a+", "i am a mvp")
print(res)

res = re.findall(r"\d+", "我一天学习6个小时,上课4个小时，睡觉8个小时，吃饭2个小时，娱乐4个小时")
print(res)

res = re.finditer(r"\d{2}", "我学习6个小时,上课4个小时，睡觉80个小时，吃饭20个小时，娱乐40个小时")
for item in res:  # 从迭代器中拿到内容
    print(item.group())  # 从匹配的结果中拿到数据

print("1==" * 50)
# search 只寻找一次
res = re.search(r"\d+", "我学习6个小时,上课4个小时，睡觉80个小时，吃饭20个小时，娱乐40个小时")
print(res.group())
print("2==" * 50)
# match 相当于search 函数 在正则匹配项前加了^  即对匹配项行首匹配
res = re.match(r"\D+", "我学习6个小时,上课4个小时，睡觉80个小时，吃饭20个小时，娱乐40个小时")
print(res.group())
print("3==" * 50)
# match 相当于search 函数 在正则匹配项前加了^  即对匹配项行首匹配
res = re.match(r"^\D+", "我学习6个小时,上课4个小时，睡觉80个小时，吃饭20个小时，娱乐40个小时")
print(res.group())
print("4==" * 50)
res = re.search(r"^\D+", "我学习6个小时,上课4个小时，睡觉80个小时，吃饭20个小时，娱乐40个小时")
print(res.group())

# 预加载 compile 提前把正则对象加载完成
print("预加载" * 30)
obj = re.compile(r"\d+")
res = obj.search("我学习6个小时,上课4个小时，睡觉80个小时，吃饭20个小时，娱乐40个小时")
print(res.group())

# 分组爬取数据
print("分割线" * 30)
#  如果我们从get、post中返回了一个字符串  ，我们可以通过这种方式将其提取出来
# (?P<>正则)
s = """
<div class='西游记'><span id='10010'>中国联通</span></div>
<div class='西游记'><span id='10010'>中国移动</span></div>
"""
obj = re.compile(r"<span id='\d+'>.*?</span>")
res = obj.findall(s)
print(res)
print("将数据单独拿出来========")
obj = re.compile(r"<span id='(\d+)'>(.*?)</span>")
res = obj.findall(s)
print(res)
print("分组到编号===========")
obj = re.compile(r"<span id='(?P<id>\d+)'>(?P<name>.*?)</span>")
res = obj.finditer(s)
for item in res:
    id = item.group("id")
    print(id)
    name = item.group("name")
    print(name)
