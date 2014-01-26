#!/usr/bin/env python
#list = ['1','2','3','4','5','6','7','8','9','0']
list = ['!','@','#','$','%','^','&','*','(',')','_','+']
from hashlib import md5


loop_time=1

def calc_md5(string):
	m = md5()
	m.update(string)
	return m.hexdigest()	

def write_file(string):
	file_obj = open('./md5_result','a')
	file_obj.write(string + " " + calc_md5(string) + "\n")
	file_obj.close()

def sequence(n):
#    base=['1','2','3','4','5','6','7','8','9','0'];
#    print map(lambda x:[x] *n,[base])[0];
    result = reduce(lambda x,y:[(a+b) for a in x for b in y],map(lambda x:[x]*n,[list])[0])
    for item in result:
        write_file(item)

for i in range (1,10):
	sequence(i)
