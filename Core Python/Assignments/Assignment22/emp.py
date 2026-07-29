# (Pickling and Unpickling)
import pickle
import os

class Emp:

    def __init__(self, eid, ename, basic):
        self.eid = eid
        self.ename = ename
        self.basic = basic

    def __str__(self):
        return f'''
        ID      : {self.eid}
        NAME    : {self.ename}
        BASIC   : {self.basic}'''