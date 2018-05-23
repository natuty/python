#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from poster.encode import multipart_encode 
from poster.streaminghttp import register_openers 
import json
import urllib2
import redis
import random
reload(sys)   
sys.setdefaultencoding('utf8') 


def test2():
	N = 50
	ranStr = ranApa()
	for i in range(0,N):
		#print( i*1+i*10+i*100+i*1000+i*10000+i*100000+i*1000000)
		#print(i+"	3	GHF4532	煤渣	3	"+i%4+"	1	"+i%5)
		zha=""
		ranNum = random.sample(range(1111,9999),N)
		for i in range(0,50):
			print('A{0}Z'.format(ranNum[i]))
		return
		ran = random.randint(0, 2)
		ran13 = random.randint(1, 3)
		ran14 = random.randint(2, 5)
		if ran==0:
			zha="煤渣"
		elif ran==1:
			zha="铁渣"
		elif ran==2:
			zha="矿渣"
		#print("%d	%d	%s%d\t%s\t%d\t%d\t1\t%d" %(i, i, ranStr.pop(),ranNum[i], zha, ran+1,ran13, ran14))
		print("%d	%d	%d\t%s\t%d\t%d\t1\t%d" %(i, i, ranNum[i], zha, ran+1,ran13, ran14))

def ranApa():
	apa = [chr(i) for i in range(65,91)]
	s = set()
	while len(s) <50 :
		one = random.randint(0,25)
		second = random.randint(0,25)
		three = random.randint(0,25)
		str = '{0}{1}{2}'.format(apa[one],apa[second],apa[three])
		if str not in s:
			s.add('{0}{1}{2}'.format(apa[one],apa[second],apa[three]))
	return s

if __name__ == '__main__': 
	test2()
	
	