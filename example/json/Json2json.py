
import json,sys
from IPSearch import *
'''
fw = open('all_ip.txt','a')
def readIP(pathname):
    f=open(pathname,'r')
    read = json.load(f)
    for a in read:
        ip = a['feature'].split(':')[0]
        fw.write(ip+'\n')


for path in os.listdir('./all'):
    pathname='./all/'+path
    #print pathname
    #readIP(pathname)
fw.close()
'''




def jsonformat(a):
    #f=open("test.json","w")
    #
    adict = {}
    adict["comment"]=a["comment"]
    adict["featuretype"]=a["featuretype"]
    adict["matchingmode"]=a["matchingmode"]
    adict["author"]=a["author"]
    adict["feature"]=a["feature"]
    know={}
    know["hacker"]=a["know"]["hacker"]
    know["threattype"]=a["know"]["threattype"]
    know["description"]=a["know"]["description"]
    know["family"]=a["know"]["family"]
    know["judge"]=a["know"]["judge"]
    know["killchain"]=a["know"]["killchain"]
    know["threatname"]=a["know"]["threatname"]
    

    decision_source=[]
    #decision_source.append("static_decryption")
    #decision_source.append("tainted")
    #decision_source.append("protocol_identification")
    #decision_source.append("network_feature")
    know["decision_source"]=decision_source

    know["output_time"]=None
    know["accuracy"]=None

    IP_location=[]
    ipl={}
    ipl["ip"]=a['feature'].split(':')[0]
    ipS = IPSearch()
    ipl["location"]=(ipS.getIPLocation(ipl["ip"]))[0].decode('gbk')
    IP_location.append(ipl)
    know["IP_location"]=IP_location

    '''
    drefer={}
    lurl=[]
    lmd5=[]
    lmd5.append("d36e84e04ead6814e9e6946f127d9d78")
    lmd5.append("89daa29dbd850002aae19c2c054c8ca8")
    drefer["url"]=lurl
    drefer["md5"]=lmd5
    adict["refer"]=drefer
    '''
    know["refer"]=a["know"]["refer"]
    adict["know"]=know
    return adict

    #print adict
    #f.write(json.dumps(adict))

    #print json.dumps(adict,indent=5)

fwj=open("test.json","w")
port=[]
for path in os.listdir('./all'):
    pathname='./all/'+path
    fr=open(pathname,"r")
    for a in json.load(fr):
        if a['feature'].split(':')[0] =="127.0.0.1" :
            print "127.0.0.1"
            continue
        port.append(jsonformat(a))
        #print json.dumps(a,indent=5)
        #sys.exit()
fwj.write(json.dumps(port))

'''
for a in json.load(fr):
    print jsonformat(a)
    #print json.dumps(a,indent=5)
    sys.exit()
'''
