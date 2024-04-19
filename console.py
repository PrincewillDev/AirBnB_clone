#!/usr/bin/python3
"""
This from models.engine import filemodule create a custom console for manipulating data
without a visual interface.

Class:
    HBNBCommand:- This class creates a custom Command line
    interface by inheritting from cmd module.
"""
import cmd
from models.base_model import BaseModel
from custom_functions.to_pydic import jsonpydic
import json
import models

class HBNBCommand(cmd.Cmd):
    """
    This class inherits the cmd class as its base class.
    It creates a custom command line.

    Attributes:
        prompt:- Class attribute for displaying the prompt
        in the command line interface.

    Methods:
        do_quit:- This method quits the command line
        interface by invoking the <quit command>.

        do_EOF:- This method handles EOF by sending an
        end of file signal when Ctrl-D is pressed.

        do_create:- This method creates an instance of BaseModel
        save the file to json and prints it id.

        do_show:- This Method prints the string representation
        of an instance based on the class name and id.
    """
    prompt = "(hbnb) "
    
    def do_quit(self, args):
        """ Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        Handle the EOF (End of File) command which is
        triggered by pressing Ctrl-D.
        """
        return True
        
    def do_create(self, args):
        """Creates a new instance of BaseModel and print its id"""
        if not args:
            print(" ** Class name missing ** ")
        elif args == "BaseModel":
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

        else:
            print(" ** class doesn't exist ** ")
    
    def do_show(self, args):
        """Prints the string representation of an instance
        based on the class name and id"""
        if not args:
            print(" ** class name missing ** ")
        args = args.split()
        if len(args) > 0:
            if args[0] != "BaseModel":
                print(" ** class doesn't exist ** ")
            elif len(args) < 2:
                print(" ** instance id missing ** ")
            else:
                data = jsonpydic()
                instanceFound = False
                for key, value in data.items():
                    if value.get("id") == args[1]:
                        instanceFound = True
                        print(str(value))
                        break
                if instanceFound == False:
                    print(" ** no instance found ** ")
    
    def do_destroy(self, args):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        if not args:
            print(" ** class name missing ** ")
        
        args = args.split()
        if len(args) > 0:
            if args[0] != 'BaseModel':
                print(" ** class doesn't exist ** ")
            elif len(args) < 2:
                print(" ** instance id missing ** ")
            
            else:
                myData = models.storage.all()
                key = args[0] + '.' + args[1]
                if key in myData:
                    del myData[key]
                    models.storage.save()
                else:
                    print(" ** No instance found ** ")
        
    def do_all(self, args):
        """Prints all string representation of all instances
        based or not on the class name. 
        """
        args = args.split()
        if not args:
            all_objects = models.storage.all()
            print(all_objects)

        elif args[0] == 'BaseModel':
            myData = models.storage.all()
            key = args[0]
            
        else:
            print("Testing might work")

    def do_update(self, args):
        """This method updates an instance based on class name and id"""
        if not args:
            print(" ** class name missing ** ")
        args = args.split()
        if len(args) > 0:
            if args[0] != 'BaseModel':
                print(" ** class doesn't exist ** ")
            elif len(args) < 2:
                print(" ** instance id missing ** ")
            elif len(args) < 3:
                print(" ** attribute name missing ** ")
            elif len(args) < 4:
                print(" ** value missing ** ")
            else:
                myData = models.storage.all()
                key = args[0] + '.' + args[1]
                attrname = args[2]
                attrvalue = args[3]
                if key not in myData:
                    print(" ** no instance found ** ")
                #Retrive the instance
                instance = myData[key]
                if attrname in {"id", "created_at", "updated-at"}:
                    return
                existingVal = getattr(instance, attrname, None)
                if existingVal is None:
                    print("")
                if isinstance(existingVal, str):
                    existingVal = str(attrvalue)
                
                elif isinstance(existingVal, int):
                    existingVal = int(attrvalue)
                elif isinstance(existingVal, int):
                    existingVal = float(attrvalue)
                
                setattr(instance, attrname, attrvalue)
                models.storage.save()

    def emptyline(self):
        "Do nothing when an emptyline is entered"   
        pass



if __name__ == '__main__':
    HBNBCommand().cmdloop()