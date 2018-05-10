#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
from MyArray import *
reload(sys)   
sys.setdefaultencoding('utf8') 

def carLoadMaterialSet(N):
	id = 1
	carId = 1
	for i in range(0,N):
		for j in range(0,len(loadMaterial)):
			type = i / 10 +1
			if type >= 6 :
				type = 6
			print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(id, car_height[i]-1, carId, 1, 0, j+1, car_height[i]-1))
			id = id+1
		carId = carId + 1

if __name__ == '__main__':
	carLoadMaterialSet(50)