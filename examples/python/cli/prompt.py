from cmd import Cmd

class MyPrompt(Cmd):
    prompt = 'pb> '
    intro = "Welcome! Type ? to list commands"

    def do_exit(self, inp):
        '''exit the application.'''
        print("Bye")
        return True

MyPrompt().cmdloop()
