# -*- coding: utf-8 -*- 
import sys
reload(sys)   
sys.setdefaultencoding('utf8') 
from pyquery import PyQuery as pq
# #引入 PyQuery 
# doc = pq(filename='example.html')
# # 传入文件 example.html 
# print doc.html() 
# # html()方法获取当前选中的 html 块 
# print doc('.item-1') 
# # 相当于 class 选择器，选取 class 为 item-1 的 html 块 
# data = doc('tr') # 选取 <tr> 元素 
# for tr in data.items():# 遍历 data 中的 <tr> 元素 
# 	temp = tr('td').eq(2).text() # 选取第3个 <td> 元素中的文本块 
# 	print(temp)


# p=pq("<head><title>Hello World!</title></head>")

# print p('head').html()# 获取相应的 HTML 块
# print p('head').text()# 获取相应的文本内容


# d = pq("<div><p id='item-0'>test 1</p><p class='item-1'>test 2</p></div>") 
# print d('div').find('p') # 查找 <div> 内的 p 元素 
# print d('div').find('p').eq(0) # 查找 <div> 内的 p 元素，输出第一个 p 元素

#d = pq(url='http://news.sina.com.cn/china/')
d = pq(url='http://news.sina.com.cn/china/',encoding="utf-8")
lis = d('.blk122').find('a')
for li in lis.items():
    print li.html()
    print li.attr('href')