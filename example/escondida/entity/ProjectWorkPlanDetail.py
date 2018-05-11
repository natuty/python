#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
from MyArray import *
reload(sys)   
sys.setdefaultencoding('utf8') 

def projectWorkDetail(N):
	id = 1
	slagId = 1
	digId = 33
	siteId = 1
	f = open("projectWorkDetail.txt", "w")
	for i in range(0,len(ProjectWorkPlanSet)):
		pwps = ProjectWorkPlanSet[i]
		workPlanId = i+1
		for j in range(1,random.randint(3,4)):
			lm = loadMaterial[random.randint(0,2)]
			f.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(id, '2018-05-11 12:08:40',digId,pwps[1],0,20180511+i,0,0,0,pwps[3],pwps[3],0,0,0,pwps[2],lm[0],projectCar_pricingType[digId-1],1,0,pwps[2],pwps[2],siteId,slagId,0,0,workPlanId,car_code[slagId-1],"",lm[1],pwps[1]))
			id = id + 1
			for k in range(2,6):
				f.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(id, '2018-05-11 12:08:40',slagId,pwps[1],0,20180511+i,0,digId,0,pwps[3],pwps[3],0,0,0,pwps[2],lm[0],2,1,0,pwps[2],pwps[2],siteId,slagId,0,0,workPlanId,car_code[slagId-1],car_code[digId-1],lm[1],pwps[1]))
				#print(id,i,j,k)
				id = id + 1
				slagId = slagId + 1
				pass
			digId = digId + 1
			siteId = siteId + 1
			pass
	f.close()
	pass
if __name__ == '__main__': 
	projectWorkDetail(50)


'''
1260	2018-05-03 13:32:35	1	晚班	0	20180318	0	33	0	2018-04-17 11:23:00		0	0	0		1	2	1	0	2018-04-17 11:21:00		0	1	4	0	3	4421	4811	煤渣	
1261	2018-05-03 13:32:35	2	晚班	0	20180318	0	33	0	2018-04-17 11:23:00		0	0	0		1	2	1	0	2018-04-17 11:21:00		0	2	4	0	3	9196	4811	煤渣	
1262	2018-05-03 13:32:35	33	晚班	0	20180318	0	0	0	2018-04-17 11:23:00		0	0	0		1	1	1	0	2018-04-17 11:21:00		0	33	4	0	3	4811		煤渣	
1263	2018-05-19 13:32:35	3	晚班	0	20180419	0	34	0	2018-04-19 11:23:00		0	0	0		1	2	1	0	2018-04-19 11:21:00		0	1	4	0	2	2015	1696	煤渣	
1264	2018-05-19 13:32:35	4	晚班	0	20180419	0	34	0	2018-04-19 11:23:00		0	0	0		1	2	1	0	2018-04-19 11:21:00		0	2	4	0	2	5170	1696	煤渣	
1265	2018-05-19 13:32:35	34	晚班	0	20180419	0	0	0	2018-04-19 11:23:00		0	0	0		1	1	1	0	2018-04-19 11:21:00		0	33	4	0	2	1696		煤渣	
'''