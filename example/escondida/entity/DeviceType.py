#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
from MyArray import *
reload(sys)   
sys.setdefaultencoding('utf8') 

def deviceType():
	id = 1
	for i in range(0,len(DeviceType)):
		if DeviceType[i][1] == 'Unknow':
			continue
		#print("{0}\t{1}\t{2}\t{3}\t{4}".format(id, 0, x.value, x.value+x.name, type))
		print('{0}\t{1}\t{2}\t{3}\t{4}'.format(id, 0, DeviceType[i][1][0:-3], DeviceType[i][1]+DeviceType[i][2], DeviceType[i][3]))
		id = id+1

if __name__ == '__main__':
	deviceType()