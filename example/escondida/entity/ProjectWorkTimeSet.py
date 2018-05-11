#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
from MyArray import *
reload(sys)   
sys.setdefaultencoding('utf8') 

def ProjectWorkTimeSet(N):
	id = 1
	for i in range(0,len(ProjectWorkPlanSet)):
		d = ProjectWorkPlanSet[i]
		print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(d[0],0,d[5],d[3],d[7],d[1],1,d[4],d[2],d[6]))
		id = id + 1
	pass
if __name__ == '__main__': 
	ProjectWorkTimeSet(6)