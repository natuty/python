#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
reload(sys)   
sys.setdefaultencoding('utf8') 



# 有一个嵌套的列表，现在要把它里面的所有元素扁平化输出
list = [[
  [1, 2, 3],
  [4, 5, 6]
]]
# 使用列表推导式
flat_list = [x for list0 in list for list1 in list0 for x in list1]
# [1, 2, 3, 4, 5, 6]

# 可读性太差，易出错。这种时候更建议使用普通的循环
flat_list = []
for list0 in list:
    for list1 in list0:
        flat_list.extend(list1)