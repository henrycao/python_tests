#!/usr/bin/env python
from socket import *
import threading
import time

def tcp_connect_1():
        HOST = '10.0.3.120'
        PORT = 4346
        BUFSIZE = 1024
        ADDR = (HOST,PORT)
        s = socket(AF_INET,SOCK_STREAM)
        s.connect(ADDR)
        s.send("123\n")
        recv = s.recv(BUFSIZE)
        s.close()

def tcp_connect_2():
        HOST = '10.0.3.109'
        PORT = 4346
        BUFSIZE = 1024
        ADDR = (HOST,PORT)
        s = socket(AF_INET,SOCK_STREAM)
        s.connect(ADDR)
        s.send("321\n")
        recv = s.recv(BUFSIZE)
        s.close

def loop():
        for i in range(1000):
                tcp_connect_1()
                tcp_connect_2()
                print i

def worker():
        loop()
        time.sleep(1)
        return

print time.time()

for i in xrange(100):
        t = threading.Thread(target=worker)
        t.start()

print time.time()

