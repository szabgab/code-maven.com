from cmd import Cmd

class MyPrompt(Cmd):
    prompt = 'pb> '
    intro = "Welcome! Type ? to list commands"

    def do_exit(self, inp):
        '''exit the application. Shorthand: x q.'''
        print("Bye")
        return True

    def do_add(self, inp):
        print("adding '{}'".format(inp))

    def help_add(self):
       print("Add a new entry to the system.")

    def do_edit(self, inp):
        t = "this is some ext"

    def default(self, inp):
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)

        print("Default: {}".format(inp))

MyPrompt().cmdloop()
