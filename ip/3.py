#!/usr/bin/env python
import httplib

file=open("./ip","r")
url="/iplookup/iplookup.php?format=jsi&ip="
for ip in file:
	realurl = url + ip
	print realurl
#	conn = httplib.HTTPConnection("int.dpool.sina.com.cn")
#	url="/iplookup/iplookup.php?format=js&ip="+ip
#	print url
#	conn.request("GET",url)
#	r1 = conn.getresponse()
#	print r1.read()
#	conn.close()
	conn = httplib.HTTPConnection("int.dpool.sina.com.cn")
#	url="/iplookup/iplookup.php?format=jsi&ip="
#	url="/iplookup/iplookup.php?format=jsi&ip=123.117.230.53"
#	print url
#	print ip
	conn.request("GET","/iplookup/iplookup.php?format=jsi&ip=",ip)
	r1 = conn.getresponse()
	print r1.read()
	conn.close()
