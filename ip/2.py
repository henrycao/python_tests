#!/usr/bin/env python
import httplib

file=open("./ip","r")
for ip in file:
	conn = httplib.HTTPConnection("www.youdao.com")
	url="/smartresult-xml/search.s?type=ip&q="+ip
	print url
	conn.request("GET",url)
	r1 = conn.getresponse()
	print r1.read()
	conn.close()
