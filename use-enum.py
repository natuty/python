#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
from enum import Enum, unique
reload(sys)   
sys.setdefaultencoding('utf8') 

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

@unique
class CarTypeEnum(Enum):
	Unknow = "未知类型"
	AllType = "全部类型"
	OilCar = "加油车"
	DiggingMachine = "挖机"
	SlagCar = "渣车"
	Bulldozer = "推土机"
	GunHammer = "炮锤"
	SingleHook = "单勾"
	WaterWheel = "水车"
	DrillingMachine = "钻机"
	Roller = "压路机"
	Forklift = "铲车"

def test():
	for i in range(0,50):
		print('"{0}",'.format(random.randint(6, 10)))

if __name__ == '__main__': 
	#test()
	a = CarTypeEnum.SlagCar
	print(a.name)
	print(a.value)

	# print(CarTypeEnum['SlagCar'].name)
	print(CarTypeEnum['SlagCar'].value)

	for x in CarTypeEnum:
		print('{0}\t{1}'.format(x.name,x.value))
		pass

	day1 = Weekday.Mon
	print('day1 =', day1)
	print('Weekday.Tue =', Weekday.Tue)
	print('Weekday[\'Tue\'] =', Weekday['Tue'])
	print('Weekday.Tue.value =', Weekday.Tue.value)
	print('day1 == Weekday.Mon ?', day1 == Weekday.Mon)
	print('day1 == Weekday.Tue ?', day1 == Weekday.Tue)
	print('day1 == Weekday(1) ?', day1 == Weekday(1))