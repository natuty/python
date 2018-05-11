#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
from MyArray import *
reload(sys)   
sys.setdefaultencoding('utf8') 

def projectRefuelLog(N):
	id = 1
	for i in range(0,N):
		print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(id, '2018-02-10 14:36:00',43,ProjectRefuelLog_capacity[i],id,id,1,0,id,ProjectRefuelLog_capacity[i]*ProjectOilPrice,43,ProjectOilPrice,1))
		id = id + 1
	pass
if __name__ == '__main__': 
	projectRefuelLog(50)