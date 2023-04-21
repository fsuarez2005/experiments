#!python3

import socket
import sqlite3

from http.server import BaseHTTPRequestHandler, HTTPServer


# resources are nested containers 
class RESTResource:
    # resources are mapped using a Dict
    
    def __init__(self):
        self.resources = {}
    
    def get_resources(self):
        return self.resources.keys()
        
    def append_resource(self,name,resource):
        self.resources[name] = resource
        


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = "Hello!"

        self.protocol_version = "HTTP/1.1"
        self.send_response(200)
        self.send_header("Content-Length", len(message))
        self.end_headers()
        
        # parse path
        path_array = self.path.split('/')
        
        #print(self.path)
        print(self.server.parent)

        self.wfile.write(bytes(message, "utf8"))
        return


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
    
    
# uses http.server with a custom HTTPRequestHandler
class Server:
    def __init__(self):
        self.hostname = ''
        self.port = 8881 

    def setup_resources(self):
        self.root = RESTResource()
        



    def setup(self):
        self.server = (self.hostname,self.port)
        self.httpd = HTTPServer(self.server, RequestHandler)
        self.httpd.parent = self


    def run(self):
        # loop waiting for connections (terminate with Ctrl-C)
        self.httpd.serve_forever()

            
s = Server()
s.setup()
s.run()


