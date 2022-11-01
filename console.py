#!/usr/bin/python3
"""Entry point for tfrom modelshe console"""
from models.base_model import BaseModel
from models import base_model
from models.engine.file_storage import FileStorage
import cmd
import inspect
import models


class HBNBCommand(cmd.Cmd):
    """Class containing methods for the console"""

    prompt = '(hbnb)'
    file = None

    def emptyline(self):
        """Defines behaviour of console if empty line is enmtered"""

        pass

    def close(self):
        if self.file:
            self.file.close()
            self.file = None

    def do_quit(self, arg):
        """Command for exiting the console"""

        self.close()
        return True

    def do_EOF(self, arg):
        """Command for exiting the console"""

        self.close()
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel class and saves it"""

        my_module_classes = list(x[0] for x in inspect.getmembers(base_model, inspect.isclass))
        print(my_module_classes)
        if arg == "" :
            print("** class name missing **")
        elif arg not in my_module_classes:
            print("** class doesn't exist **")
        else:
            self.arg = BaseModel()
            self.arg.save()
            print(self.arg.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
