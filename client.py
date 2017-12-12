#!/usr/bin/env python
import socket
import os
ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.connect(('YOUR_ADDRESS',7500))
#f=open('aa','wb')
ss.sendall('Your text here')
os.system('sleep 1')
ss.send('FOE')
data=ss.recv(1024)
print "server dafu %s"%data
ss.close
