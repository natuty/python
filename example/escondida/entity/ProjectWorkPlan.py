#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
from MyArray import *
reload(sys)   
sys.setdefaultencoding('utf8') 

def projectWorkPlan():
	id = 1
	for i in range(0,len(ProjectWorkPlan)):
		d = ProjectWorkPlan[i]
		print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(id,"2017-05-01 08:00:00",1,d[4],0,d[3],d[3],d[6],d[1],1,d[2],d[2],d[5],0))
		id = id + 1
	pass
if __name__ == '__main__': 
	projectWorkPlan()


	''' 
1	2018-03-16 15:27:03	1	20180316	0	2018-03-16 18:29:21	2018-05-02 18:03:44	1	早班	1	2018-03-16 14:29:31	2018-05-02 18:03:35	1	7
2	2018-03-16 15:27:03	1	20180317	0	2018-03-17 18:29:21	2018-05-02 18:03:42	0	中班	1	2018-03-17 14:29:31	2018-05-02 18:03:39	1	10
3	2018-04-17 11:21:54	1	20180318	0	2018-04-17 11:23:00	2018-05-02 18:03:40	0	晚班	1	2018-04-17 11:21:00	2018-05-02 18:03:32	1	15
	'''