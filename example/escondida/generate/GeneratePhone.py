#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys,os
import random
reload(sys)   
sys.setdefaultencoding('utf8') 

def createPhone():
	prelist=["130","131","132","133","134","135","136","137","138","139","147","150","151","152","153","155","156","157","158","159","186","187","188"]
	return random.choice(prelist)+"".join(random.choice("0123456789") for i in range(8))
def createNum(n):
	s = set()
	while len(s) < n :
		s.add(createPhone())
	return s
if __name__ == '__main__':
	print createNum(90)