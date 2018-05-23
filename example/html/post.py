#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from poster.encode import multipart_encode 
from poster.streaminghttp import register_openers 
import json
import urllib2
reload(sys)   
sys.setdefaultencoding('utf8') 

def post():
	#url = "http://192.168.1.188:9000/api/mobile/shift/query?countType=0"
	#url = "http://192.168.1.188:9000/api/mobile/transport/query?current=1&pageSize=3"
	#url = "http://192.168.1.188:9000/api/mobile/schedule/query?current=0"
	url = "http://192.168.1.188:9000/api/mobile/abnormal/query"
	body_value = {"countType": "1","version_code": "66" }
	register_openers()
	body_value  = json.JSONEncoder().encode(body_value)
	request = urllib2.Request(url, body_value)
	request.add_header("projectid", 1)
	result = urllib2.urlopen(request ).read()
	print result	
	
if __name__ == '__main__': 
	post()