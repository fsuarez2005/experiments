#!/usr/bin/env python

import sys
#import pdb; pdb.set_trace()
import logging

logger = logging.getLogger(__name__)

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
                raise TypeError(f"Value must be of type"
                                +self.clazz.__name__)
            
            exec(self.name+" = "+str(value))
            
            
        def getenvironment(self):
            
            return eval(self.name)
        
        def clearenvironment(self):
            # set environment to default value of class
            # using no-arg constructor
            cmd = f"{self.name}.__class__()"
            print(f"setenvironment({cmd})")
            self.setenvironment(eval(self.name+".__class__()"))
        
        def __str__(self):
            return f"<"+self.__class__.__name__+f" ({self.name},{self.clazz})>"
    
    # -------------------------------------------------------
    
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
    
    def save_all_locations(self):
        "Save variables and cache used by importer"
        for x in self.locations:
            print(f"Saving {self.locations[x].name} to {x}")
            self.data[x] = self.locations[x].getenvironment()

    def clear_all_locations(self):
        for n in self.locations:
            print("clearenvironment cmd = ")
            cmd = f"{self.locations[n].name} = None"
            print(f"exec({cmd})")
            
            #exec(cmd)
            


# #######################################################

import unittest

class TestLocation(unittest.TestCase):
    def setUp(self):
        self.tmoduleName = "sys.modules" 
        self.tmoduleClass = dict
        
        self.tlocation = ImporterState.Location(self.tmoduleName)
    
    @unittest.skip    
    def test_setenvironment(self):
        loc = self.tlocation
        value = {}
        # set to blank
        loc.setenvironment(value)

    @unittest.skip
    def test_getenvironment(self):
        loc = self.tlocation
        
        value = loc.getenvironment()
        self.assertEqual(value.__class__,dict)
    
    #@unittest.skip    
    def test_clearenvironment(self):
        self.tlocation.clearenvironment()
        #print(f"\n{self.tmoduleName} = {eval(self.tmoduleName)}")

    @unittest.skip    
    def test_getclass(self):
        clazz = self.tlocation.clazz
        
        self.assertEqual(clazz,self.tmoduleClass)
        



def main():
    logger.debug('main')
    unittest.main()

if __name__ == '__main__':
    main()
    



