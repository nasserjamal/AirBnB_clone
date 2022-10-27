#!/usr/bin/python3
"""Contains a FileStorage class"""


import datetime
import os.path
import uuid
import json


class FileStorage:
    """serializes instances to a JSON file and 
        deserializes JSON file to instances"""

    __file_path = __file__
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""

        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""

        self.__objects[type(self).__name__ + ".id"] = obj

    def save(self):
        """Serializes __objects to the JSON file"""

        my_string = json.dumps(self.__objects)
        with open(self.__file_path, "w", encoding='utf-8') as jsonfile:
            jsonfile.write(my_string)

    def reload(self):
        """Deserializes the JSON file to __objects"""

        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding='utf-8') as jsonfile:
                self.__objects = json.loads(my_string)
        else:
            pass


