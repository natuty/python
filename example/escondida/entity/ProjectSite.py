#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
from MyArray import *
reload(sys)   
sys.setdefaultencoding('utf8') 

def projectSite():
	id = 1
	for i in range(0,10):
		deviceId = i+21
		code = 'D{:03.0f}'.format(i+41)
		print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(id,deviceId,ProjectSite_uid[i],ProjectSite_distance[i],1,ProjectSite_name[i],1,ProjectSite_name[i],code))
		id = id+1

if __name__ == '__main__':
	projectSite()