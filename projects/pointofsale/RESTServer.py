#!python3



from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
from RESTResource import RESTResource

from Utility import debug_print, verbose_print



# CONFIGURATION

port = 8881
hostname = 'localhost'





root_xml_data = """<?xml version="1.0" encoding="UTF-8?>
<root>
    <version value="0.0" />
</root>
"""


    




# creates test resources
def create_resources():
    debug_print("create_resources()")
    root = RESTResource("/")
    
    root.display_callback = lambda o: root_xml_data
    
    objects = RESTResource("objects")
    objects.display_callback = lambda o: "<objects></objects>"
    
    products = RESTResource("products")
    products.display_callback = lambda o: "<products></products>"
    
    
    root['objects'] = objects
    root['products'] = products
    
    
    debug_print(root.keys())
    
    return root


# --------------------------------------------------------------------------------
def traverse_resources(root_res,path_array):
    debug_print(path_array)
    current_res = root_res
    
    #remove / in path
    path_array.pop(0)
    
    end_slash = False
    
    
    for n in path_array:
        debug_print("current res: "+current_res.name)
        debug_print("current component: "+n)
        if n == "":
            # done, using current_res
            end_slash = True
        else:
            current_res = current_res[n]
        
    return current_res


# --------------------------------------------------------------------------------

class RequestHandler(BaseHTTPRequestHandler):
    
    #The HEAD method asks for a response identical to a GET request, but without the response body.
    # TODO: def do_HEAD(self):

    #The POST method submits an entity to the specified resource, often causing a change in state or side effects on the server.    
    # TODO: def do_POST(self):

    #The PUT method replaces all current representations of the target resource with the request payload.    
    # TODO: def do_PUT(self):

    #The DELETE method deletes the specified resource.    
    # TODO: def do_DELETE(self):

    #The CONNECT method establishes a tunnel to the server identified by the target resource.    
    # TODO: def do_CONNECT(self):

    #The OPTIONS method describes the communication options for the target resource.
    # TODO: def do_OPTIONS(self):

    #The TRACE method performs a message loop-back test along the path to the target resource.    
    # TODO: def do_TRACE(self):

    #The PATCH method applies partial modifications to a resource.    
    # TODO: def do_PATCH(self):

    #The GET method requests a representation of the specified resource. Requests using GET should only retrieve data.
    def do_GET(self):
        message = ""
        
        # extract path from URL
        path_parsed = urlparse(self.path)
        
        # create path heirarchy
        # path_array always begins with empty string
        # if path ends in a /, last element with be an empty string
        
        path_array = path_parsed.path.split('/')
        #print(path_array)
        
        
        #get root resource
        root_res = self.server.parent.root
        
        
        res = traverse_resources(root_res,path_array)
        message += res.display()
        
        
        
        self.protocol_version = "HTTP/1.1"
        self.send_response(200)
        
        # Must have for CORS
        self.send_header("Access-Control-Allow-Origin","*")
        
        
        self.send_header("Content-Length", len(message))
        self.end_headers()
        
        self.wfile.write(bytes(message, "utf8"))


    
# uses http.server with a custom HTTPRequestHandler
class RESTServer:
    def __init__(self):
        self.hostname = hostname
        self.port = port 

    def setup_resources(self):
        self.root = create_resources()

    def setup(self):
        self.server = (self.hostname,self.port)
        self.httpd = HTTPServer(self.server, RequestHandler)
        self.httpd.parent = self

    def run(self):
        verbose_print(f"Running server:  {self.hostname}:{self.port}...")
        
        # loop waiting for connections (terminate with Ctrl-C)
        self.httpd.serve_forever()

def main(): 
    print("===============================================================")
    print("===============================================================")
    print("===============================================================")
    
    
    s = RESTServer()
    s.setup_resources()
    s.setup()
    s.run()

if __name__ == '__main__':
    main()

