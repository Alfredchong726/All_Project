import requests

url = 'https://movie.douban.com/top250'

headers = {
    # 'Cookie': 'bid=nJ5mbBL3XUQ; __gads=ID=d4e33a95e1a5dad6-226538e329c600e1:T=1614424616:RT=1614424616:S=ALNI_MZ_Tj6BNEWUbp4D-BvvCiuahdGlNw; ll="118267"; __yadk_uid=RFh6Mvp3Q0kHQrj9HrxBbKJmG73HbVNK; gr_user_id=68d4d6d7-4109-4c05-9bfd-681a6915e8de; _vwo_uuid_v2=D4C3FBDACFA2E2318ADF6AC1B3BB844AE|4d0c5b80ba8c50e923415ca2315254f7; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1633957495%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DvG0rjIHdmdoiKFsm21WVM0kgbPY3YnFROyUgUXPzuE2XRSEHPMovpTzCsEkRs1sw%26wd%3D%26eqid%3Da435adef000172150000000661643674%22%5D; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.989597980.1611321780.1633701103.1633957495.31; __utmb=30149280.0.10.1633957495; __utmc=30149280; __utmz=30149280.1633957495.31.23.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.834357791.1611321780.1633698588.1633957495.22; __utmb=223695111.0.10.1633957495; __utmc=223695111; __utmz=223695111.1633957495.22.17.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_id.100001.4cf6=55c37287cf2a05f6.1611321773.22.1633958015.1633698588.',
    'Host': 'movie.douban.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
}

response = requests.post(url)
html_data = response.text

# response.request 查看请求体信息
print(response.request.url)  # 查看请求体中 url 地址
print(response.request.headers)  # 查看请求体中的请求头信息, requests请求的时候, 会自动的带上常见的请求头字段
print(response.request.method)  # 查看请求体中请求方法
