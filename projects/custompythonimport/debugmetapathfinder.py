#!/usr/bin/env python

import importlib
import importlib.abc

class DebugMetaFinder(importlib.abc.MetaPathFinder):
    def find_spec(self,fullname, path, target = None):
        print("MyMetaFinder")
        print(f"Looking for {fullname} in {path} for {target}")
        #return importlib.machinery.ModuleSpec('blank',None)
        #return super().find_spec(fullname, path, target)
        return None