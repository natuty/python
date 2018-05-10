#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, datetime,time
reload(sys)   
sys.setdefaultencoding('utf8') 

def dif_time_day(startDatetime, endDatetime):
	d1 = datetime.datetime.strptime(startDatetime, '%Y-%m-%d %H:%M:%S')
	d2 = datetime.datetime.strptime(endDatetime, '%Y-%m-%d %H:%M:%S')
	"""计算天数差值"""
	day = (d2 - d1).days
	second = (d2 - d1).seconds
	"""计算两个日期之间相隔的秒数"""
	total_seconds = (d2 - d1).total_seconds()
	print day
	print second
	print total_seconds
	print total_seconds/60

def main(N):
	dif_time_day('2017-10-16 19:21:22','2017-10-17 19:23:22')
	dif_time_day('2018-05-01 18:00:00','2018-05-02 17:02:03')
	pass
if __name__ == '__main__': 
	main(50)