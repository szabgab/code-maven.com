from cmd import Cmd

class MyPrompt(Cmd):
   def do_exit(self, inp):
        '''exit the application.'''
        print("Bye")
        return True

   def do_add(self, inp):
        print("Adding '{}'".format(inp))

   def help_add(self):
       print("Add a new entry to the system.")

MyPrompt().cmdloop()

