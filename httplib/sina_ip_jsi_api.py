#!/usr/bin/env python
import httplib

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
	url="/iplookup/iplookup.php?format=jsi&ip=58.247.192.223"
	conn = httplib.HTTPConnection("int.dpool.sina.com.cn")
	conn.connect()
	conn.request("GET",url)
	r1 = conn.getresponse()
	print r1.read()
	conn.close()
	
loop_request()
#single_request()
