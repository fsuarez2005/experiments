#!python3

import socket
import sqlite3

class Database:
    
    
    def __init__(self):
        pass
        
    
    def connect(self,filename):
        self.db = sqlite3.connect(filename)
        
    def disconnect(self):
        self.db.close()
    
    #create
    
    
    
    #read
    #update
    #delete
    pass
    
    
    
class Server:
    def __init__(self):
        self.port = 8881
        
    def create_socket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def set_socket_options(self):
        # Ensure that you can restart your server quickly when it terminates
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


    def bind_to_port(self):
        self.sock.bind(('', self.port))

    def set_as_listen(self):
        self.sock.listen(5)

    def setup(self):
        self.create_socket()
        self.set_socket_options()
        self.bind_to_port()
        self.set_as_listen()
        
    def get_data(self):
        return ""
        

    def run(self):
        # loop waiting for connections (terminate with Ctrl-C)
        try:
            while 1:
                newSocket, address = self.sock.accept(  )
                print("Connected from", address)
                # get HTTP request
                header = ""
                while True:
                
                    header = newSocket.recv(1024)
                    print(header.decode())
                
                
                
                print("Sending data to client")
                newSocket.send(b"HTTP/1.1 200 OK\nContent-Type: text/plain\n\nhello")
                newSocket.close(  )
                print("Disconnected from", address)
        finally:
            self.sock.close(  )
            
            
s = Server()
s.setup()
s.run()


