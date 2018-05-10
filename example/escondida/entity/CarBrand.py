#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
from MyArray import *
reload(sys)
sys.setdefaultencoding('utf8') 
# 1	1	0	P01	P哈	4	渣车	0
def test():
	id = 1
	for x in CarTypeEnum:
		if x.name == 'AllType' or x.name == 'Unknow':
			continue
		print("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}".format(id, 1, 0, x.name[0:3],x.name[0:3]+x.value, id, x.value, id))
		id = id+1
if __name__ == '__main__':
	test()
