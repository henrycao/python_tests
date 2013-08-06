#!/usr/bin/env python
import httplib

def loop_request():
	file=open("./url","r")
	for url in file:
		conn = httplib.HTTPConnection("int.dpool.sina.com.cn")
		conn.set_debuglevel(3)
		conn.connect()
		conn.request("GET",url)
		r1 = conn.getresponse()
		print r1.read()
		conn.close()

def single_request():
	conn = httplib.HTTPConnection("int.dpool.sina.com.cn")
	conn.set_debuglevel(3)
	conn.connect()
	conn.request("GET","/iplookup/iplookup.php?format=jsi&ip=58.247.192.223")
	r1 = conn.getresponse()
	print r1.read()
	conn.close()
	
#loop_request()
single_request()
