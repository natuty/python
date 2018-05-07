#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
from test_import import * 
from enum import Enum, unique
reload(sys)   
sys.setdefaultencoding('utf8') 

def test():
	a=[[1,2,3],[4,5,6]]
	print(a[0][1])
	print(a[1])


if __name__ == '__main__': 
	test()
	