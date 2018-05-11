#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
from MyArray import *
reload(sys)   
sys.setdefaultencoding('utf8') 



def test2():
	N = 50
	ranStr = ranApa()
	for i in range(0,N):
		#print( i*1+i*10+i*100+i*1000+i*10000+i*100000+i*1000000)
		#print(i+"	3	GHF4532	煤渣	3	"+i%4+"	1	"+i%5)
		zha=""
		ranNum = random.sample(range(11111,99999),N)
		ran = random.randint(0, 2)
		ran13 = random.randint(1, 3)
		ran14 = random.randint(2, 5)
		if ran==0:
			zha="煤渣"
		elif ran==1:
			zha="铁渣"
		elif ran==2:
			zha="矿渣"

		id = i+1
		capacity = car_height[i] * car_length[i] * car_width[i]
		carNumber = car_carNumber[i]
		code = car_code[i]
		deleted = 0
		driverId =i+1
		height = car_height[i]
		length = car_length[i]
		modelDetailId = i+1
		ownerId = i+1
		standardHeight = car_height[i]-1
		vehicleLoad = standardHeight * car_length[i] * car_width[i]
		width = car_width[i]

		# 1	1	P01	0	0	4421	1	1	1	0	0		900	10	2018-02-23 18:18:06	0	2018-04-03 15:21:19	900	1	X01	1	2	emp1	1	1	123	0	4	0	10000	900
		

		pos = 6
		if i>=32:
			pos=3
		if i>=42:
			pos=i-42
		if i>=45:
			pos=i-41
		if i>=47:
			pos=i-40

		# pricingType=0
		# if pos == 3:
		# 	pricingType = 1
		# else:
		# 	pricingType=2
		pricingType = projectCar_pricingType[i]

		print('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}\t{13}\t{14}\t{15}\t{16}\t{17}\t{18}\t{19}\t{20}\t{21}\t{22}\t{23}\t{24}\t{25}\t{26}\t{27}\t{28}\t{29}\t{30}'.format(id, pos, data[pos][3], id, 1, car_code[i], projectCar_cubicHourCubic[i], 10, 20, 0, id, userWork_name[i], car_height[i], 30, "2018-02-22 18:18:02", 0, "2018-02-22 18:18:02", length, data[pos][0], data[pos][4], 0, id, userWork_name[i], pricingType, 1, 100, 0, data[pos][5], data[pos][5], vehicleLoad, width))
		#print("%d\t%d%s%d\t%s\t%d\t%d\t1\t%d" %(i, capacity, ranStr.pop(),ranNum[i], zha, ran+1,ran13, ran14))

def ranApa():
	apa = [chr(i) for i in range(65,91)]
	s = set()
	while len(s) <50 :
		one = random.randint(0,25)
		second = random.randint(0,25)
		three = random.randint(0,25)
		if(one != second and one !=three and second != three):
			str = '{0}{1}{2}'.format(apa[one],apa[second],apa[three])
			if str not in s:
				s.add('{0}{1}{2}'.format(apa[one],apa[second],apa[three]))
	return s

def test3():
	a = ["a","c","b"]
	print a[0],car_carNumber[1]

if __name__ == '__main__': 
	test2()
	#test3()
	
	