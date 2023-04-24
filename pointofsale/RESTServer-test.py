#!python3


from restserver import restserver

def test_traversal():
    root = create_resources()
    current_res = traverse_resources(root, "/products".split('/'))
    
    print(current_res.display())


