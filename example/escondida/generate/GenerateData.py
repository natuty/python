#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, string, random
sys.path.append("..")
from entity.MyArray import *
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

def userWorkData(N):
	id = 1
	print('[')
	for i in range(0,N):
		print('\t[{0},"{1}","{2}","{3}"],'.format(id, userWork_name[i],userWork_phoneNumber[i],userWork_idCard[i]))
		id = id+1
	print(']')

def userWorkCode(N):
	id = 1
	for i in range(0,N):
		print('"E2018{:04.0f}",'.format(id))
		id = id+1

def projectRefuelLog_capacity(N):
	for i in range(0,N):
		print('{}'.format(random.randint(1,5)*100))


def getRandom(size):
	field=string.letters+string.digits
	return "".join(random.sample(field,size))
def generate(group,size):
	return "-".join([getRandom(size) for i in range(group)])
def cpuId(N):
	s = set()
	while len(s) <N :
		s.add(generate(4,4))
	return s

def pricingType(N):
	for i in range(0,N):
		type = 2
		if i>=32 :
			type=random.randint(1,3)
		if i>= 42 :
			type = 1
		print type


if __name__ == '__main__':
	#test()
	#test2()
	#test4()
	#userWorkData(50)
	#userWorkCode(50)
	#projectRefuelLog_capacity(50)
	#print cpuId(90)
	#pricingType(50)
	for i in range(1,100):
		print('{0}\t{0:02.0f}{0:02.0f}{0:02.0f}\t{1}'.format(i,random.randint(1000,9999)))