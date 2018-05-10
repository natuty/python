#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
from MyArray import *
reload(sys)   
sys.setdefaultencoding('utf8') 

def carLoadMaterialSet(N):
	#pwd: 123456
	#1	super	2018-01-30 17:40:32		1	1	超级管理员		$2a$10$9j4fEEcchtojQMOGKe7FSOwmeCo/N0EUWbKvC7ASbjskkfoJyvQlK
	print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(51, "super", "2018-01-30 17:40:32","",1,1,"超级管理员","","$2a$10$9j4fEEcchtojQMOGKe7FSOwmeCo/N0EUWbKvC7ASbjskkfoJyvQlK"))
	id = 1
	for i in range(0,N):
		print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(id, userWork_workCode[i], "2018-01-30 17:40:32","",1,1,userWork_workCode[i],userWork_phoneNumber[i],"$2a$10$MSt2b0a4.jsxot9JyTh3Qesvn4AF3w.0s6LVBwyagxsvW09CXvVxa"))
		id = id + 1


if __name__ == '__main__':
	carLoadMaterialSet(50)