#!/usr/bin/python3
'''super class'''
from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    '''main class'''

    def __init__(self, *args, **kwargs):
        '''constructor method'''

        if len(kwargs):
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                if key == "created_at" or key == "update_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        '''print formal representation of Base model isntance'''
        strout = '['
        strout += str(self.__class__.__name__) + '] ('
        strout += str(self.id) + ') ' + str(self.__dict__)
        return strout

    def save(self):
        '''update attribute with datetime'''
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        '''return a dic with all key/values of the instance'''

        newdic = self.__dict__
        newdic["__class__"] = self.__class__.__name__
        newdic["created_at"] = self.created_at.isoformat()
        newdic["update_at"] = self.updated_at.isoformat()
        return newdic
