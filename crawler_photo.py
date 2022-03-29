import requests

if __name__ == '__main__':
    url = "http://n.sinaimg.cn/photo/transform/700/w1000h500/20211002/3c9c-4fecc919c8af637a9f6cc7c82b4cf3bc.jpg"

    img_data = requests.get(url= url).content
    with open("./photo.jpg", "wb") as fp:
        fp.write(img_data)
