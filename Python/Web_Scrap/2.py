'''
网页的组成
HTML 
    超文本语言，文字,图片,按钮

CSS
    对HTML语言进行美化

javaScript
    上传资源
    脚本语言，和HTML和CSS配合使用
    让页面有交互性
'''
'''
爬虫的基本原理
    互联网比作大网，爬虫就是网上爬行的蜘蛛
    把网的节点比作一个网页
    当蜘蛛爬到这个节点就是访问了这个网页，获取网页的信息

爬虫的概述
    1. 获取网页
        获取网页源代码，有用的信息
        向网页发送请求，返回的响应体就是网页源代码

    2. 提取信息
        分析网页源代码，从中提取想要的数据,正则表达式来提取
        beautiful soup, lxml

    3. 保存数据
        txt文本或者json文本，保存到数据库mysql,Mongodb当中，csv逗号分割符文件

    4. 自动化程序
        爬虫代替人完成这些操作
        动画

能抓取怎样的数据
源代码返回的一些文本，图片，链接，音频
有些网站不容易抓取
多以js加密，以js的逆向来获取数据

javaScript渲染页面

会话和cookies
需要登陆的情况，有些页面需要登陆才能访问，登陆之后可以连续网文多次

静态页面和动态页面
动态页面容易爬取一些
静态页面：html的文件，将这个文件放在服务器上，就会成为一个网站
    加载速度快，编写起来简单，但是不会灵活多变的显示数据

动态页面：灵活多变的显示页面，维护性强

ajax上传的


无状态HTTP
服务器不会记录发送请求获取响应的过程
保持HTTP连接状态

会话：
    用来存储特定用户的一些属性和配置信息，在进行页面的访问和页面之间的跳转时
    存储在会话对象中的数据就不只要请求了页面，用户还没有会话,服务器就会自动创建一个会话
    当会话国企或被放弃是，服务器就会终止这会话
    会话是保存在服务器上的，访问的是那个服务器的页面，那么会话就会存在哪一个服务器上
cookies:
cookies是储存在本地的,会话是保存在服务器的
为了让某些网站辨认用户身份，进行会话跟踪而存储在用户本地的数据


set-cookies就是用来设置存在本地的信息
会话的维持

代理的基本原型
按照协议区分
代理区分
按照匿名程度区分
高度匿名代理：会将数据原封不动的转发，服务端看起来就是普通的客户端在访问
普通匿名代理：会在数据做一些改动，服务器可能会发现这是一个代理ip
透明代理：会将数据原封不动的转发，服务器看起来是你的真是ip,能提高访问速度
间谍代理：组织或者个人用于记录用户传输的数据，然后进行研究和监控的代理服务器

'''

'''
基本库的使用
    urllib
'''

# QUESTIONS
'''
    js加密，如果关了js,能接触加密吗
    如果一个页面往下拉，它能加载更多的数据，可是它有一个极限，那么它是静态页面，还是动态页面
'''

import urllib.request

response1 = urllib.request.urlopen('https://www.baidu.com/')
response2 = urllib.request.urlopen('http://www.python.org/')

print(response2.read().decode('utf-8'))

#urlopen,模拟浏览器发送请求