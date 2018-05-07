# -*- coding: UTF-8 -*-
import sys,os
import re
reload(sys)   
sys.setdefaultencoding('utf8') 

def mod(pathName):
    f = open(pathName,'r',encoding='utf-8')
    f_new = open(pathName+".bak",'w',encoding='utf-8')
    for line in f:
        p = re.compile('<[^>]+>')
        if "Good day is good day" in line:
            line = line.replace('Good day is good day','hello,yanyan')
    f_new.write(line)
    f.close()
    f_new.close()

def t(path, b):
	#path="./"
	for root,dirs,files in os.walk(path):
		for name in files:
			print name
			if name.endswith(".kt"):
				#print root,dirs,name 
				filename=root+"/"+name
				f=open(filename,"r")
				filecontent=""
				line=f.readline()
				while line:
					if b:
						pattern1 = 'day:\s*Int,'
						pattern2 = ',\s*day:\s*Int\)'
						temp=re.sub(pattern1,"", line)
						l=re.sub(pattern2,")", temp)
						filecontent=filecontent+l
						line=f.readline()
					else:
						'''
						pattern1 = 'day\s*=\s*[a-z\.*A-Z]+,'
						pattern2 = ',\s*day\s*=\s*[a-z\.A-Z]+\)'
						temp=re.sub(pattern1,"", line)
						l=re.sub(pattern2,")", temp)
						filecontent=filecontent+l
						line=f.readline()
						'''
						'''
						pattern1 = 'package entity'
						l=re.sub(pattern1,"package com.example.demo.entity", line)
						filecontent=filecontent+l
						line=f.readline()
						'''

						'''
						pattern1 = "import entity"
						l=re.sub(pattern1,"import com.example.demo.entity", line)
						filecontent=filecontent+l
						line=f.readline()
						'''
						'''
						pattern1 = ".*com.example.demo.bo..*"
						l=re.sub(pattern1,"", line)
						filecontent=filecontent+l
						line=f.readline()
						'''
						'''
						pattern1 = ".*fun getBo.*"
						l=re.sub(pattern1,"", line)
						filecontent=filecontent+l
						line=f.readline()
						'''
						'''
						pattern1 = "package com.sytech.escondida"
						l=re.sub(pattern1,"package com.example.demo", line)
						filecontent=filecontent+l
						line=f.readline()
						'''
						'''
						pattern1 = "import com.sytech.escondida"
						l=re.sub(pattern1,"import com.example.demo", line)
						filecontent=filecontent+l
						line=f.readline()
						'''
						'''
						pattern1 = "import \)entity"
						l=re.sub(pattern1,"import com.example.demo.entity", line)
						filecontent=filecontent+l
						line=f.readline()
						'''
						pattern1 = "import \)enum"
						l=re.sub(pattern1,"import com.example.demo.enum", line)
						filecontent=filecontent+l
						line=f.readline()







				f.close()
				f=file(filename,"w")
				f.writelines(filecontent)
				f.close()

if __name__ == '__main__':    
    path='F:\\workspace\\webserver\\escondida\\src\\main\\kotlin\\com\\sytech\\escondida\\'
    path2='F:\\workspace\\webserverMy2\\src\\main\\kotlin\\com\example\\demo\\entity\\repository'
    #t(path+'service')
    #t(path+'service\\impl')
    #
    #t(path+'entity\\repository')
    #t(path+'controller')
    #t(path+'service')
    #t(path+'dao\\impl')
    #t(path+'dao')
    #t(path+'service\\impl')
    #t(path+'mq',False)

    #t(path+'')
    #
    t(path2,False)