
from SocketServer import TCPServer, ThreadingMixIn, StreamRequestHandler  
  
class Server(ThreadingMixIn, TCPServer):  
    pass  
class Handler(StreamRequestHandler):  
    def handle(self):  
        while True:  
            data = self.request.recv(1024)  
            if not data:  
                break  
            result = 0  
            for i in range(1,int(data)+1):  
                result = result + reduce(lambda x,y:x*y,range(1,i+1))  
            self.request.send('the result is %i'%result)  
          
server = Server(('localhost', 21567), Handler)  
server.serve_forever()  
