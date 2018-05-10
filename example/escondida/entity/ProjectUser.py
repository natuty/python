#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
from MyArray import *
reload(sys)   
sys.setdefaultencoding('utf8') 

def projectUser(N):
	id = 1
	for i in range(0,N):
		print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(id, '2018-05-07 13:41:34',0,1,1,userWork_idCard[i],0,userWork_name[i],1,userWork_workCode[i],userWork_phoneNumber[i]))
		id = id + 1
if __name__ == '__main__': 
	projectUser(50)