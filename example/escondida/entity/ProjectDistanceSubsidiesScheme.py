#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
from MyArray import *
reload(sys)   
sys.setdefaultencoding('utf8') 

def projectDistanceSubsidiesScheme(N):
	id = 1
	for i in range(0,N):
		print('{}\t{}\t{}\t{}\t{}\t{}米\t{}\t{}\t{}\t{}'.format(id,0,id*10000,10+i*2,0,id*100,1,0,100,10+id*2))
		id = id + 1
	pass
if __name__ == '__main__': 
	projectDistanceSubsidiesScheme(6)