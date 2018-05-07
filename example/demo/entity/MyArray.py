#!/usr/bin/python
# -*- coding: utf-8 -*-
from enum import Enum, unique

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

# @unique
# class CarTypeEnum(Enum):

#Car
car_code = ["4421","9196","2015","5170","6600","4294","6301","4518","6091","7845","2808","2234","8286","2441","2567","2240","6061","7636","4046","2458","4042","2464","5466","3495","4908","7213","4684","6992","6347","8458","9987","8105","4811","1696","7882","3265","3460","5743","8557","9524","5188","3168","4897","5404","3703","4980","5491","6155","5118","6610"]
car_carNumber=["京C·U34M6","京A·P2HAD","京C·11N0S","京A·74WAG","京A·F3KCW","京B·JXQX5","京A·Y29KL","京A·LR50N","京C·YPVCQ","京A·YK2L0","京C·VQA7G","京C·1KSE0","京B·L4D5H","京C·H394X","京C·JKNDY","京A·3XPLD","京A·CKRDB","京B·AE24H","京A·JD2W1","京B·D5MCM","京B·GD4D7","京A·EUX4C","京C·4M25F","京A·RU0YU","京A·DQE9V","京C·GPQYQ","京A·H5L6X","京B·WJSH8","京C·FQU1S","京A·HM5VC","京B·673PL","京A·0C09D","京B·EUJFY","京C·P6A0S","京C·UG3KX","京C·4US03","京A·0K8N2","京B·BWXK2","京B·3GTB5","京A·9PFYE","京B·VUB23","京C·FD6KA","京C·01SW0","京B·JU5UP","京C·NCW79","京C·WWF69","京A·U9JAA","京A·TNEKU","京A·BTEW5","京B·PXQL0"]
car_height = [10,8,9,6,7,9,8,9,9,10,7,9,9,7,6,9,8,8,9,8,7,10,6,10,10,9,7,7,9,8,6,7,9,10,9,8,6,6,9,10,8,10,10,9,9,7,10,7,6,8]
car_length = [6,6,6,7,6,10,10,8,9,10,6,6,8,10,8,6,10,6,9,6,7,10,8,8,7,6,6,7,9,7,6,8,9,7,9,6,6,7,8,6,6,9,10,8,7,10,9,6,9,9]
car_width = [6,8,10,9,10,7,8,10,9,10,7,8,6,7,9,10,9,9,9,8,8,7,9,9,6,9,10,10,6,6,9,8,10,7,10,9,10,10,7,10,8,10,6,6,8,7,6,9,9,9]

projectCar_cubicHourCubic = ["7","10","9","9","9","6","7","6","7","6","7","8","10","7","6","7","9","7","6","7","7","9","7","7","9","10","8","6","9","10","6","8","7","6","7","7","10","6","8","6","6","8","6","6","10","6","8","10","7","7"]

data = [
		[1,"加油车","OilCar","Oil","Oil001",2],
		[2,"单勾","SingleHook","Sin","Sin001",7],
		[3,"压路机","Roller","Rol","Rol001",10],
		[4,"挖机","DiggingMachine","Dig","Dig001",3],
		[5,"推土机","Bulldozer","Bul","Bul001",5],
		[6,"水车","WaterWheel","Wat","Wat001",8],
		[7,"渣车","SlagCar","Sla","Sla001",4],
		[8,"炮锤","GunHammer","Gun","Gun001",6],
		[9,"钻机","DrillingMachine","Dri","Dri001",9],
		[10,"铲车","Forklift","For","For001",11],
]

loadMaterial = [
	[1,"煤渣"],
	[2,"铁渣"],
	[3,"矿渣"],
]




if __name__ == '__main__':
	print("")

