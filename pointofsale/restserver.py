#!python3

import socket
import sqlite3

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

index_file = """<!DOCTYPE html>
<html>
</html>



"""




object_list = """<?xml version="1.0" encoding="UTF-8"?>
<objects>
    <object name="banana" plu="4022" />
</objects>"""


# resources are nested containers 
class RESTResource:
    # resources are mapped using a Dict
    
    def __init__(self,name=None):
        self.resources = {}
        
        if name is not None:
            self.name = name

    
    # the following defined on object instantiation ==========
    
    #def __getitem__(self,key)
    #def __setitem__(self,key,value)
    #def __delitem__(self,key)
    #def __missing__(self,key)
    #def __iter__(self)
    #def __reversed__(self)
    #def __contains__(self,item)
    #def keys(self):

    # ========================================================
    
    
        
    def append_resource(self,name,resource):
        self.resources[name] = resource
        

# creates a heirarchy of RESTResources
def create_resources():
    root = REST
    pass




class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        justpath = urlparse(self.path)
        path_array = justpath.path.split('/')
        
        
        
        message = ""
        
        
        
        
        # get resource using path
        #message += str(self.server.parent.root.resources[path_array])
        
        
        
        
        match path_array[1]:
            case "":
                message += "root"
            case "objects":
                message += object_list
            case _:
                message += "incorrect path"
        
        

        self.protocol_version = "HTTP/1.1"
        self.send_response(200)
        self.send_header("Content-Length", len(message))
        self.end_headers()
        
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
        self.hostname = 'localhost'
        self.port = 8881 

    def setup_resources(self):
        self.root = RESTResource()
        self.root.append_resource('objects',RESTResource())

    def setup(self):
        self.server = (self.hostname,self.port)
        self.httpd = HTTPServer(self.server, RequestHandler)
        self.httpd.parent = self

    def run(self):
        print(f"Running server:  {self.hostname}:{self.port}...")
        
        # loop waiting for connections (terminate with Ctrl-C)
        self.httpd.serve_forever()

def main():           
    s = Server()
    s.setup_resources()
    s.setup()
    s.run()

main()

