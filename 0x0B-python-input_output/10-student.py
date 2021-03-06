#!/usr/bin/python3
""" student module """


class Student:
    '''Student class
    '''

    def __init__(self, first_name, last_name, age):
        '''defines a student
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return (self.__dict__)
        else:
            i = {}
            for names in attrs:
                if hasattr(self, names):
                    i[names] = getattr(self, names)
            return (i)
