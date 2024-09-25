import urllib.request
import urllib.parse

# 1、去Chrome浏览器借助抓包找到对应的地址
url = "https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20"

# 2、封装请求头
# Cookie可以在线获取
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "Cookie" : "ll=\"108288\"; bid=dUUR_4rz-nE; douban-fav-remind=1; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1727252817%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DD-412vKcad1M1gCCen_yq9ZPI3007Nlj1sAx7_XuNjdJmlMCu1FhMfbX8-A8HPtQ%26wd%3D%26eqid%3D9d459797005b736e0000000266f3c94b%22%5D; _pk_id.100001.4cf6=92d5aa5a7642cb51.1727252817.; _pk_ses.100001.4cf6=1; __utma=30149280.1121891901.1727252817.1727252817.1727252817.1; __utmb=30149280.0.10.1727252817; __utmc=30149280; __utmz=30149280.1727252817.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.1564404208.1727252817.1727252817.1727252817.1; __utmb=223695111.0.10.1727252817; __utmc=223695111; __utmz=223695111.1727252817.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _vwo_uuid_v2=DA96D36D90DBD6CD455271A1D208DD301|16d01d1ad0caadffd6ad495c83073431"
}

# 3、创建request对象
request = urllib.request.Request(url=url, headers=headers)

# 4、请求对应内容、获得浏览器响应
response = urllib.request.urlopen(request)

# 5、编解码获取对应内容
content = response.read().decode('utf-8')

# 6、打印 / 以文件形式保存
# print(content)

with open("douban.json", 'w', encoding='utf-8') as f:
    f.write(content)