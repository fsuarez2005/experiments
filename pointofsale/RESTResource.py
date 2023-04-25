#!python3

from Utility import debug_print, verbose_print, var_print
from urllib.parse import urlparse

# Path rules
# /dir1/dir2/dir3/resource?query_string
# * if resource is suffixed by a slash, treat resource as directory
#   else treat resource as object


# resources are nested containers
# display depends on whether the container is viewed or the contents are viewed
class RESTResource:
    "Resources are mapped using a Dict."
    path_separator = '/'
    
    
    def __init__(self):
        self.resources = {}
        
        self.display_callback = None
        
    
    def display(self):
        "Returns data to be sent to client."
        data = ""
        if self.display_callback != None:
            data += self.display_callback(self)
        else:
            # no callback, must have default action
            pass
        return data
    
    def traverse(self,path_array,qs):
        ""
        
        #path_parsed = urlparse(path_qs)
        #path_array = path_parsed.path.split('/')
        
        
        var_print('path_array',path_array)
        
        if len(path_array) > 0:
            var_print('next_dir',next_dir)
            next_dir = path_array.pop()
            
        
        
        
        
    
    # ############ Dict Methods ############
    
    def __getitem__(self,key):
        return self.resources[key]
        
    
    def __setitem__(self,key,value):
        debug_print("__setitem__("+str(key)+")")
        self.resources[key] = value
        
        
    def __delitem__(self,key):
        del self.resources[key]
    
    
    
    
    #def __missing__(self,key)
    # NOTE: still raises KeyError. should I override?
    
    # TODO:
    # NOTE: using self.resources iterator
    def __iter__(self):
        return self.resources.__iter__()
    
    # TODO:
    #def __next__(self):
    #   
    
    
    # TODO:
    #def __reversed__(self)
    
    
    def __contains__(self,item):
        return (item in self.resources)
    
    
    # TODO: returns view object, but should it?
    def keys(self):
        return self.resources.keys()
        
        
        
    # ############ /Dict Methods ############




