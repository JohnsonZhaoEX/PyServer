#!/usr/bin/env python
import socket
import os
import sys
ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.connect(('127.0.0.2',7500))
re = os.open("Content.txt", os.O_RDONLY)

'''string = raw_input()
print string
w = os.write(re,string)'''

f = os.read(re,100)
ss.sendall(f)
os.close(re)
#f=open('aa','wb')
os.system('sleep 1')
ss.send('FOE')
data=ss.recv(1024)
print "server dafu %s"%data
ss.close
