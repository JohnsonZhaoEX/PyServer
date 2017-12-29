import socket  
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
sock.connect(('localhost', 21567))  
data = '5'  
sock.send(data)  
receivedData = sock.recv(1024)  
print receivedData  
sock.close()  
