# -*- coding: utf-8 -*-
import json,sys
import gnsq
from gnsq import Nsqd, Reader, states

#guangdong_domain_c2_count5_20170313.json
#





nsq_ip = '127.0.0.1'
nsq_port = 9051

topic = 'technology'
channel = 'hrb'



#nsqPost = gnsq.Nsqd(address=nsq_ip, http_port=nsq_port, timeout=60.0)
#nsqPost.create_topic(topic)
#nsqPost.read()
#
#
#




'''
reader = gnsq.Reader(topic, channel, '120.76.170.106:9051')
#print dir(reader)
@reader.on_message.connect
def handler(reader, message):
    print 'got message:'

reader.start()
'''






class nsqAPI(object):
    def put(self, topic, channels, message):
        try:
            nsqPost = gnsq.Nsqd(address=nsq_ip, http_port=nsq_port, timeout=60.0)
            
            nsqPost.create_topic(topic)

            if isinstance(channels, list):
                for channel in channels:
                    nsqPost.create_channel(topic, channel)
            else:
                nsqPost.create_channel(topic, channels)
            
            nsqPost.publish(topic, message)
        except Exception as e:
            print e
            return

def loadFont(filename):
    f = open(filename,'r')
    setting = json.load(f)
    for a in setting:
        print a['know']['IP_location']
        print(a)
        sys.exit()

def send(filename):
    f = open(filename,'r')
    setting = json.load(f)
    #print setting
    #print json.dumps(setting)
    #
    message = json.dumps(setting)
    nsq = nsqAPI()
    nsq.put(topic,channel,message)

#send('jsonread.json')


nsq = nsqAPI()

def send2(filename):
    f = open(filename,'r')
    setting = json.load(f)
    k=0
    for a in setting:
        #print setting
        #print json.dumps(a,indent=5)
        message = json.dumps(a)
        print nsq.put(topic,channel,message)
        k+= 1
    print k
#send2("test2.json")
send2("1_jsonTojson_result_v2.json")
#1_jsonTojson_result_v2.json

