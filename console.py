#!/usr/bin/python3
""" module console.py"""
import cmd
import models
import shlex
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """class console command"""
    prompt = "(hbnb) "
    class_list = {"BaseModel"}

    def do_quit(self, args):
        """Command to quit the program"""
        return True

    def do_EOF(self, args):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        """Create new instance"""
        arg = line.split()
        if len(line) > 0:
            if line in self.class_list:
                instance = eval(str(args[0]) + '()')
                instance.save()
                print(instance.id)
            else:
                print("** class name missing **")
        else:
            print("** class doesn't exist **")
    
    def do_show(self, line):
        




if __name__ == '__main__':
    HBNBCommand().cmdloop()