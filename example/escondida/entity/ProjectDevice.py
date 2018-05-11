#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
from MyArray import *
reload(sys)   
sys.setdefaultencoding('utf8') 

def device(N):
	id = 1
	for i in range(0,N):
		type = i / 10 +1
		if type >= 6 :
			type = 6
		print('{}\t{}\tD{:03.0f}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(id, Device_cardNumber[i], id, 0, id, DeviceType[type][3], 1, "2018-01-31 14:07:47","2018-01-31 14:07:47", 0.00, 0.00, 0,21,0,ProjectSite_uid[i]))
		id = id+1

if __name__ == '__main__':
	device(90)