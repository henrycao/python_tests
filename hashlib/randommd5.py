#!/usr/bin/env python

list_1 = ['1','2','3','4','5','6','7','8','9','0']
list_2 = ['!','@','#','$','%','^','&','*','(',')']
list_3 = ['a','b','c','d','e','f','g','h','i','j']
list_4 = ['k','l','m','n','o','p','q','r','s','y']
list_5 = ['u','v','w','x','y','z','A','B','C','D']
list_6 = ['E','F','G','H','I','J','K','L','M','N']
list_7 = ['O','P','Q','R','S','T','U','V','W','X']
list_8 = ['Y','Z',',','.','/','<','>','?','[',']']
list_9 = ['{','}','|','\\','-','=','_','+']

list_all = [list_1,list_2,list_3,list_4,list_5,list_6,list_7,list_8,list_9]

from hashlib import md5
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

for i in range(0,9):
	for j in range (i+1,9):
		list = list_all[i] + list_all[j]
        	for x in range (6,14):
       	        	sequence(x)
