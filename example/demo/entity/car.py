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

		#"1\t1000			0	1	10	10	M1	1	1	10	1	800	10"
		

		pos = 6
		if i>=32:
			pos=3
		if i>=42:
			pos=i-42
		if i>=45:
			pos=i-41
		if i>=47:
			pos=i-40

		print('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}\t{13}\t{14}'.format(id, capacity, car_carNumber[i],car_code[i], 0, id, height, length,data[pos][4],data[pos][0],id,standardHeight,data[pos][0],vehicleLoad,width))
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
	
	