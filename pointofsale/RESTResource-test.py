#!python3

from RESTResource import RESTResource


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
    print(x)
    

def test_module():
    print("test_module()")
    test_callback()
    test_dict_functions()

if __name__ == "__main__":
    test_module()