#!/usr/bin/python3
"""Contains a FileStorage class"""


import datetime
import os.path
import uuid
import json

from models.base_model import BaseModel


class FileStorage:
    """serializes instances to a JSON file and 
        deserializes JSON file to instances"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""

        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        self.__objects[type(obj).__name__+ '.' + obj.id] = obj
        
    def save(self):
        """Serializes __objects to the JSON file"""

        tempDict = {}
        for key, value in self.__objects.items():
            tempDict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding='utf-8') as jsonfile:
            json.dump(tempDict, jsonfile)

    def reload(self):
        """Deserializes the JSON file to __objects"""

        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding='utf-8') as jsonfile:
                tempDict = json.load(jsonfile)
                for key, value in tempDict.items():
                    self.new(eval(value["__class__"])(**value))
        else:
            pass
