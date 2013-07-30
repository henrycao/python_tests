#!/usr/bin/env python
from hashlib import md5
 
m = md5()           #获取一个MD5加密算法对象
m.update('string') #指定要加密的字符串
m.hexdigest()      #获取加密后的16进制字符串

from hashlib import md5
 
def md5_file(name):
    m = md5()
    a_file = open(name, 'rb')    #需要使用二进制格式读取文件内容
    m.update(a_file.read())
    a_file.close()
    return m.hexdigest()
 
if __main__ == '__init__':
    print md5_file('d:/test.txt')
