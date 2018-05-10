#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
from MyArray import *
reload(sys)   
sys.setdefaultencoding('utf8') 

def userWork(N):
	id = 1
	for i in range(0,N):
		print('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}'.format(id, '2018-05-07 13:41:34',0,1,id,'2020-05-07 13:44:25',2,userWork_idCard[i],1,0,userWork_name[i],userWork_phoneNumber[i],'2018-05-07 13:49:41'))
		id = id + 1
if __name__ == '__main__': 
	userWork(50)
#1	2018-05-07 13:41:34	0	1	1	2020-05-07 13:44:25	2	230604194008261449	0	0	姜章襟	13392509588	2018-05-07 13:49:41