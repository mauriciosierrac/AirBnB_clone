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
        '''print the string representation of an instance based on the class name'''
        arg = line.split()
        odic = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            odic = storage.all()
            for key, value in odic.items():
                if value.id == arg[1] and value.__class__.__name__ == arg[0]:
                    print(value.__str__())
                    return
            print("** no instance found **")

    def do_destroy(self, line):
        '''Deletes an instance based on the class name and id'''
        arg = line.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            odic = storage.all()
            for key, value in odic.items():
                if value.id == arg[1] and value.__class__.__name__ == arg[0]:
                    del(odic[key])
                    models.storage.save()
                    return
            print("** no instance found **")

    def do_all(self, line):
        ''' Prints all string representation of all instances based or not on the class name'''
        arg = line.split()
        if len(arg) > 0 and arg[0] not in self.class_list:
            print("** class doesn't exist **")
        else:
            ndic = []
            odic = storage.all()
            for values in odic.values():
                if len(arg) > 0 and arg[0] == values.__class__.__name__:
                    ndic.append(values.__str__())
                elif len(arg) == 0:
                    ndic.append(values.__str__())
            print(ndic)
            
    def do_update(self, line):
        ''' Updates an instance based on the class name and id by adding or updating attribute '''
        arg = line.split()
        odic = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        if arg[0] not in self.class_list:
            print("** class doesn't exist **")
        if len(arg) < 2:
            print("** instance id missing **")
        if "{}.{}".format(arg[0], arg[1]) not in odic.keys():
            print("** no instance found **")
        if len(arg) < 3:
            print("** attribute name missing **")
        if len(arg) < 4:
            print("** value missing **")
        
            
            


if __name__ == '__main__':
    HBNBCommand().cmdloop()
