#!/usr/bin/python
# -*- coding: utf-8 -*-
import json,sys
import paho.mqtt.publish as publish
from Tkinter import *
reload(sys)   
sys.setdefaultencoding('utf8') 
HOST = "192.168.1.188"

class CarLog(json.JSONEncoder):
	def __init__(self,cmdInd,pktID,eventId,projectID,timeLoad,carCode,timeCheck,carID,timeDischarge,slagfieldID,excavatCurrent,excavatNext,m1fare,loader,uid,heightAvg,heightMax):
		self.cmdInd = cmdInd
		self.pktID = pktID
		self.eventId = eventId
		self.projectID = projectID
		self.timeLoad = timeLoad
		self.carCode = carCode
		self.timeCheck = timeCheck
		self.carID = carID
		self.timeDischarge = timeDischarge
		self.slagfieldID = slagfieldID
		self.excavatCurrent = excavatCurrent
		self.excavatNext = excavatNext
		self.m1fare = m1fare
		self.loader = loader
		self.uid = uid
		self.heightAvg = heightAvg
		self.heightMax = heightMax
class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.nameInput = Entry(self)
		self.nameInput.pack()
		#self.alertButton = Button(self, text='Hello', command=self.hello)
		#self.alertButton.pack()
		self.loadButton = Button(self, text='装载', command=self.load)
		self.loadButton.pack()
		self.checkButton = Button(self, text='检测', command=self.check)
		self.checkButton.pack()
		self.unloadButton = Button(self, text='卸载', command=self.unload)
		self.unloadButton.pack()

	def hello(self):
		name = self.nameInput.get() or 'world'
		print('Message', 'Hello, {}'.format(name))
	def load(self):
		publish.single("smartmining/excavator/device/45efad52/request", LoadTime(1), hostname=HOST)
	def check(self):
		publish.single("smartmining/detector/device/45efad52/request", LoadTime(2), hostname=HOST)
	def unload(self):
		publish.single("smartmining/slagfield/device/45efad52/request", LoadTime(3), hostname=HOST)





def LoadTime(time):
	carLog = CarLog(
	cmdInd = "carLog",
	pktID = 1,
	eventId = 1,
	projectID = 1,
	timeLoad = time,
	carCode = "",
	timeCheck = time,
	carID = 2,
	timeDischarge = time,
	slagfieldID = 0,
	excavatCurrent = 0,
	excavatNext = 0,
	m1fare = 0,
	loader = 0,
	uid = 0,
	heightAvg = 0,
	heightMax = 0)
	return json.dumps(carLog,default=lambda o: o.__dict__)
if __name__ == '__main__': 
	
	#publish.single("smartmining/excavator/device/45efad52/request", LoadTime(1), hostname=HOST)
	#publish.single("smartmining/detector/device/45efad52/request", LoadTime(2), hostname=HOST)
	#publish.single("smartmining/slagfield/device/45efad52/request", LoadTime(3), hostname=HOST)
	
	app = Application()
	app.master.title('Hello World')
	app.mainloop()