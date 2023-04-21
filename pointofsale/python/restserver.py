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
        
        pass
        
    def create_socket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def set_socket_options(self):
        # Ensure that you can restart your server quickly when it terminates
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


    def bind_to_port(self):
        self.sock.bind(('', well_known_port))

    def set_as_listen(self):
        self.sock.listen(5)

    def run(self):
        # loop waiting for connections (terminate with Ctrl-C)
        try:
            while 1:
                newSocket, address = self.sock.accept(  )
                print("Connected from", address)
                # loop serving the new client
                while 1:
                    receivedData = newSocket.recv(1024)
                    if not receivedData: break
                    # Echo back the same data you just received
                    newSocket.send(receivedData)
                newSocket.close(  )
                print("Disconnected from", address)
        finally:
            self.sock.close(  )