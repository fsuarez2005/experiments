#!python3

from Utility import debug_print, verbose_print


# resources are nested containers
# display depends on whether the container is viewed or the contents are viewed
class RESTResource:
    # resources are mapped using a Dict
    
    def __init__(self,name=None):
        self.resources = {}
        
        if name is not None:
            self.name = name
        
        self.display_callback = None
    
    
    # return data to be sent to client
    def display(self):
        data = ""
        if self.display_callback != None:
            data += self.display_callback(self)
        else:
            # no callback, must have default action
            pass
        return data
    
    def __getitem__(self,key):
        return self.resources[key]
        
    
    def __setitem__(self,key,value):
        debug_print("__setitem__("+key+")")
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


