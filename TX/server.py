#!/usr/bin/python

import socket
import sys
import os
host ='127.0.0.2' #Server default IP is 0.0.0.0
port =7500
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(2)
#result=os.open('output.txt',os.O_RDWR|os.O_CREAT)
try:
	while True:
		conn,add=s.accept()
		while True:
			data2=''
			data1=conn.recv(100)
			if data1=='EOF':
				conn.send('hello client1')
				break
			if data1=='FOE':
				conn.send('hello client2')
				break
				data2+=data1
#			os.write(result,data2)
				print data1
#	sys.stdout=fd
except KeyboardInterrupt:
	print "you have CTRL+C,Now quit"
	os.close(result)
	s.close()
	s.close()
