#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
from MyArray import *
reload(sys)
sys.setdefaultencoding('utf8') 

# id
# name
# remark
# type
# deleted
#         var id: Long = 0,
#         var name: String = "",
#         var remark: String = "",
#         var type: CarTypeEnum = CarTypeEnum.Unknow,
#         var deleted: Boolean = false

#1	0	L01	哈哈	Unknow
def test():
	N = 4
	id = 1
	for x in CarTypeEnum:
		if x.name == 'AllType' or x.name == 'Unknow':
			continue
		for i in range(1,N):
			print('{0}\t{1}\t{2}00{3}\t{4}{2}00{3}\t{5}'.format(id,0,x.name[0:2],i, x.value, x.name))
			id = id+1

def test2():
	id = 1
	for x in CarTypeEnum:
		if x.name == 'AllType' or x.name == 'Unknow':
			continue
		print("{0}\t{1}\t{2}\t{2}{3}\t{3}".format(id, 0, x.value, x.name))
		id = id+1

if __name__ == '__main__':
	test2()
