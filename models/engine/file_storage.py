#!/usr/bin/python3
"""Contains a FileStorage class"""


import datetime
import os.path
import uuid
import json


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

        with open(self.__file_path, "w", encoding='utf-8') as jsonfile:
            for value in self.__objects.values():
                json.dump(value.to_dict(), jsonfile)

    def reload(self):
        """Deserializes the JSON file to __objects"""

        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding='utf-8') as jsonfile:
                self.__objects = json.loads(jsonfile)
        else:
            pass


