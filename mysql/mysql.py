#!/usr/bin/env python
import MySQLdb
 
try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='1234qwer,',port=3306)
    cur=conn.cursor()
    conn.select_db('python');
    cur.execute("""create table test2(id int,info varchar(100))""")
#value=[0,"1","b026324c6904b2a9cb4b88d6d61c81d1"];
value = [1,"inserted ?"];
    cur.execute(""insert into test values(%s,%s)"",value);
values=[]
    cur.close()
    conn.close()
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])
