#!/usr/bin/env python
from hashlib import md5

#get a md5 object 
m = md5()           
#define the string for md5
m.update('string') 
#get hexadecimal md5 result
m.hexdigest()      

from hashlib import md5
 
def md5_file(name):
    m = md5()
#get binary format to get file
    a_file = open(name, 'rb')    
    m.update(a_file.read())
    a_file.close()
    return m.hexdigest()
 
if __main__ == '__init__':
    print md5_file('d:/test.txt')
