#!/usr/bin/python3
"""Contains a BaseModel class"""


from models import storage
import datetime
import uuid


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Instantiation method for our class"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != '__class__':
                    self.__dict__[key] = value
        else:
            storage.new(self)
        

    def __str__(self):
        """String representation for our class"""

        return "[{}] ({}) {}"\
            .format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with the current datetime"""

        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary of all keys/values of __dict__ of instance"""

        dict_1 = self.__dict__.copy()
        dict_1["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if k in ("created_at", "updated_at"):
                v = self.__dict__[k].isoformat()
                dict_1[k] = v
        return dict_1
