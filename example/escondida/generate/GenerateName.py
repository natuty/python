#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
reload(sys)   
sys.setdefaultencoding('utf8') 

# 生成名字
def generateName1():
	a1=['张','金','李','王','赵']
	a2=['玉','明','龙','芳','军','玲']
	a3=['','立','玲','','国','']
	for i in range(15):
		name=random.choice(a1)+random.choice(a2)+random.choice(a3)
		print(name)


def generateName2():
	xing=u'赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜'
	ming=u'豫章故郡洪都新府星分翼轸地接衡庐襟三江而带五湖'
	X=random.choice(xing)
	#print X.encode("utf8")
	M="".join(random.choice(ming) for i in range(2))
	# print ''.encode("gb2312")
	# print(X+M)
	# f = open("aaa.txt", "a+")
	# f.write(X+M+'\n')
	# f.close()
	return X+M

def generateName():
	id=1
	s = set()
	while len(s) <50 :
		s.add(generateName2())
	f = open("generateName.txt", "w")
	while len(s)>0:
		name = s.pop()
		print name
		f.write('"{0}",'.format(name))
		id = id + 1
	f.close()


if __name__ == '__main__':
	#generateName2()
	generateName()