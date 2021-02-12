#!/usr/bin/python3
'''Define FileStorage class'''
import json
from models.base_model import BaseModel


class FileStorage():
    '''Serialized instances to Json and Json to Instances'''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' return dict'''
        return self.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj_class_name>.id'''
        if obj:
            self.__objects["{}.{}".format(
                str(type(obj).__name__), obj.id)] = obj

    def save(self):
        ''' serializes __objects to the JSON file'''
        newdic = {}
        for key, value in self.__objects.items():
            newdic[key] = value.to_dict()
            with open(FileStorage.__file_path, "w") as file:
                json.dump(newdic, file)

    def reload(self):
        ''' deserializes the JSON file to __objects'''
        try:
            with open(FileStorage.__file_path) as outfile:
                fload = json.load(outfile)
                for key, value in fload.items():
                    FileStorage.__objects[key] = eval(value["__class__"])(**value)
        except FileNotFoundError:
            return
