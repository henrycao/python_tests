#!/usr/bin/env python
import sys, httplib, urllib, base64

params = "platformCode=Android&CUID=PIN&ORDER_TYPE=M&PAID=COPGAM05&payCode=00&authKey=null&productCode=com.popcap.pvzoriginal&ERP_ID=PINHALL&imei=352059050228121&AMOUNT=0&cpCode=GPS&MID=M1000170&RETUEN_BUTTON_STRING=test&CID=C001700000282&PCODE=300000&action=01&uid=null"
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/html", "chartset":"utf-8"}
conn = httplib.HTTPConnection('10.88.230.235:8080')
conn.set_debuglevel(3)
conn.connect()
conn.request('POST', '/mimigigi/MimigigiServlet', params,headers)
response = conn.getresponse()
print response.read()
conn.close()
