#!/usr/bin/env python
# -*- coding: utf8 -*-
import MySQLdb
conn = MySQLdb.connect(host='localhost', user='root',passwd='1234qwer,')
cursor = conn.cursor()
cursor.execute("""create database if not exists python default charset utf8""")
conn.select_db('python');
cursor.execute("""create table test(id int, src varchar(16), md5 varchar(32) """)
value = [1,"1","b026324c6904b2a9cb4b88d6d61c81d1"];
cursor.execute("insert into test values(%s,%s,%s)",value);
values=[]
