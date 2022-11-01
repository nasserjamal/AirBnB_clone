#!/usr/bin/python3
"""Entry point for the console"""
import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
