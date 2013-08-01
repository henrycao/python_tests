#!/usr/bin/env python
import pygeoip

gi4 = pygeoip.GeoIP('./GeoLiteCity.dat', pygeoip.MEMORY_CACHE)
fp=open("./ip","r")
for eachline in fp:
	#b=gi4.country_name_by_addr(eachline)
	b=gi4.record_by_addr(eachline)
	c=b['city'] + " " + b['country_name']
	print c.encode('ascii','ignore')
