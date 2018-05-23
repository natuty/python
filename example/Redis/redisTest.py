#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import redis
reload(sys)   
sys.setdefaultencoding('utf8') 
def redisTest():
	r = redis.Redis(host='192.168.56.102', port=6379)
	r.set('name', '張三')  
	print (r.get('name'))
	print (r.get('entity:projectCurrentWorkPlan:1'))
	r.delete('entity:projectCurrentWorkPlan:1')
	print (r.get('entity:projectCurrentWorkPlan:1'))

if __name__ == '__main__': 
	redisTest()