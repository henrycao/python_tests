#!/usr/bin/env python
from hashlib import md5
 
m = md5()           #获取一个MD5加密算法对象
m.update('string') #指定要加密的字符串
m.hexdigest()      #获取加密后的16进制字符串
