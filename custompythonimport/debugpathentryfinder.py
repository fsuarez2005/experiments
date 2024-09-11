#!/usr/bin/env python

import importlib
import importlib.abc


class MyPathEntryFinder(importlib.abc.PathEntryFinder):
    def find_spec(self,fullname, target = None):
        print("path entry finder")
        return super().find_spec(fullname, target)