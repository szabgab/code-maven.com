from cmd import Cmd

class MyPrompt(Cmd):
   def do_exit(self, inp):
        print("Bye")
        return True

   def do_add(self, inp):
        print("Adding '{}'".format(inp))

MyPrompt().cmdloop()
print("after")

