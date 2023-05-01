#!python3

from RESTResource import RESTResource
from Utility import debug_print, verbose_print, var_print
from urllib.parse import urlparse

def test_dict_functions():
    print("test_dict_functions()")
    a = RESTResource(name="/")
    
    #a[0] = "frank"
    a[1] = "suarez"
    #a[1]
    #del a[0]
    print(1 in a)
    print(2 in a)
    print(a.keys())
    print(a.resources)
    
    
    for n in a:
        print(n)

def test_callback():
    print("test_callback()")
    
    a = RESTResource()
    
    a.display_callback = lambda o: "<test></test>"
    
    x = a.display()
    var_print("x",x)
    

def test_traverse():
    print("test_traverse()")
    
    a = RESTResource()
    
    a["objects"] = RESTResource()
    
    a["objects"][123] = RESTResource()
    
    path = 'objects/123'
    path_parsed = urlparse(path)
    path_array = path_parsed.path.split('/')
    query_string = ''
    
    
    a.traverse(path_array,query_string)
    



def test_module():
    print("test_module()")
    #test_callback()
    #test_dict_functions()

if __name__ == "__main__":
    breakpoint()
    test_module()
    
    test_traverse()
    
    
    