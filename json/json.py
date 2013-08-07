#!/usr/bin/env python
import httplib
import json

def loop_request():
	file=open("./ip","r")
	for ip in file:
		ip = ip.rstrip()
		url="/iplookup/iplookup.php?format=jsi&ip=%s " % (ip)	
		conn = httplib.HTTPConnection("int.dpool.sina.com.cn")
		conn.connect()
		conn.request("GET",url)
		r1 = conn.getresponse()
		print r1.read()
		conn.close()

def single_request():
	uri="/iplookup/iplookup.php?format=js&ip=58.247.192.223"
	conn = httplib.HTTPConnection("int.dpool.sina.com.cn")
	conn.connect()
	conn.request("GET",uri)
	r1 = conn.getresponse()
	data_string = r1.read()
	conn.close()
	print type(data_string)
	print data_string 
	json_data = data_string.split('= ')[1].split(';')[0]
	print type(json_data)
        j=list(json_data)
        print j
        print type(j)

#	print type(json_data)
#	list(json_data)
#	print json_data
#	print type(json_data)
#	encoded = json.dumps(json)
	#decoded = json.loads(encoded)
	#print decoded
	
	
	
#loop_request()
single_request()
