#!/usr/bin/python3
'''
   A module that defines a Base class
'''


class Base(object):
    ''' A Base class '''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
