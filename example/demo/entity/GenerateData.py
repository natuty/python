#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
from MyArray import *
reload(sys)   
sys.setdefaultencoding('utf8') 

def test():
	id = 1
	print('[')
	for x in CarTypeEnum:
		if x.name == 'AllType' or x.name == 'Unknow':
			continue
		print('\t[{0},"{1}","{2}","{3}","{4}"],'.format(id, x.value, x.name, x.name[0:3], x.name[0:3]+"001",))
		id = id+1
	print(']')

def test2():
	tt = [
		[1,"加油车","OilCar","Oil","Oil001"],
		[2,"单勾","SingleHook","Sin","Sin001"],
		[3,"压路机","Roller","Rol","Rol001"],
		[4,"挖机","DiggingMachine","Dig","Dig001"],
		[5,"推土机","Bulldozer","Bul","Bul001"],
		[6,"水车","WaterWheel","Wat","Wat001"],
		[7,"渣车","SlagCar","Sla","Sla001"],
		[8,"炮锤","GunHammer","Gun","Gun001"],
		[9,"钻机","DrillingMachine","Dri","Dri001"],
		[10,"铲车","Forklift","For","For001"],
	]
	print(tt[0][1])

def test3():
	N = 50
	for i in range(0,N):
		one = random.randint(6,10)
		print('"{0}",'.format(one))

def test4():
	N = 32
	for i in range(0,N):
		one = random.randint(6,10)
		print('{0}{1}{2}\\t'.format('{',i,'}'))

if __name__ == '__main__':
	#test()
	#test2()
	#test4()