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
        """Defines behaviour of console if empty line is entered"""

        pass

    def do_quit(self, arg):
        """Command for exiting the console"""

        return True

    def do_EOF(self, arg):
        """Command for exiting the console"""

        print("")
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel class and saves it"""

        my_module_classes = list(x[0] for x in inspect.getmembers(base_model, inspect.isclass))
        if arg == "" :
            print("** class name missing **")
        elif arg not in my_module_classes:
            print("** class doesn't exist **")
        else:
            self.arg = BaseModel()
            self.arg.save()
            print(self.arg.id)

    def do_show(self, *args):
        """Shows the string representation of the instance"""

        my_module_classes = list(x[0] for x in inspect.getmembers(base_model, inspect.isclass))
        if args[0] == "":
           print("** class name missing **")
        elif args[0] not in my_module_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[1] not in self.__dict__.values():
            print("** no instance found **")
        



if __name__ == '__main__':
    HBNBCommand().cmdloop()
