#!/usr/bin/env python

DEBUG=False

modules = {
    'sys': __import__('sys'),
    'os': __import__('os'),
    'importlib': __import__('importlib')
}



import importlib
import importlib.abc
import importlib.machinery
import sys

class ImporterState:
    class Location:
        def __init__(self,name):
            
            # test if name exists
            
            self.name = name
            self.value = None
            self.clazz = eval(self.name+".__class__")
        def save(self):
            
            self.value = self.getenvironment()
        def loadsaved(self):
            
            self.setenvironment(self.value)
        def setenvironment(self,value):
            
            if not isinstance(value,self.clazz):
                raise TypeError(f"Value must be of type "+self.clazz.__name__)
            
            
            
            exec(self.name+" = "+str(value))
        def getenvironment(self):
            
            return eval(self.name)
        def clearenvironment(self):
            # set environment to default value of class
            # using no-arg constructor
            cmd = f"{self.name}.__class__()"
            print(cmd)
            self.setenvironment(eval(self.name+".__class__()"))
        def __str__(self):
            return f"<"+self.__class__.__name__+f" ({self.name},{self.clazz})>"
    
    locations = {
        "modules": Location("sys.modules"),
        "builtins": Location("__builtins__"),
        "mainloader": Location("__loader__"),
        "meta_path": Location("sys.meta_path"),
        "path_hooks": Location("sys.path_hooks"),
        "path": Location("sys.path")
    }
    
    def __init__(self):
        self.data = {}
    
    def save(self):
        "Save variables and cache used by importer"
        for x in self.locations:
            print(f"Saving {self.locations[x].name} to {x}")
            #self.data[x] = self.locations[x].getenvironment()

    def clearenvironment(self):
        for n in self.locations:
            print("clearenvironment cmd = ")
            cmd = f"{self.locations[n]} = None"
            print(f"exec({cmd})")
            
            #exec(cmd)
            



class MyMetaFinder(importlib.abc.MetaPathFinder):
    def find_spec(self,fullname, path, target = None):
        print("MyMetaFinder")
        print(f"Looking for {fullname} in {path} for {target}")
        #return importlib.machinery.ModuleSpec('blank',None)
        #return super().find_spec(fullname, path, target)
        return None

class MyPathEntryFinder(importlib.abc.PathEntryFinder):
    def find_spec(self,fullname, target = None):
        print("path entry finder")
        return super().find_spec(fullname, target)

def print_builtin_importer_info():
    x = sys.meta_path[0]
    print(dir(x))

def print_meta_path():
    print(f"{sys.meta_path = }")
    
    
def print_info():
    print_meta_path()
    print_builtin_importer_info()

# #######################################################

import unittest

class TestLocation(unittest.TestCase):
    def setUp(self):
        self.tmoduleName = "sys.modules" 
        self.tmoduleClass = dict
        
        self.tlocation = ImporterState.Location(self.tmoduleName)
    
    @unittest.skip    
    def test_Location(self):
        print(f"\n{self.tlocation = }")
        print(self.timporterState.locations)
    
    
    def test_setenvironment(self):
        loc = self.tlocation
        value = {}
        # set to blank
        loc.setenvironment(value)
    
    def test_getenvironment(self):
        loc = self.tlocation
        
        value = loc.getenvironment()
        self.assertEqual(value.__class__,dict)
        
        
    #@unittest.skip    
    def test_clearenvironment(self):
        self.tlocation.clearenvironment()
        #print(f"\n{self.tmoduleName} = {eval(self.tmoduleName)}")

    #@unittest.skip    
    def test_getclass(self):
        cls = self.tlocation.clazz
        
        self.assertEqual(cls,self.tmoduleClass)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
    



