from cmd import Cmd

import readline

def input_with_prefill(prompt, text):
    def hook():
        readline.insert_text(text)
        readline.redisplay()
    readline.set_pre_input_hook(hook)
    result = input(prompt)
    readline.set_pre_input_hook()
    return result
# https://stackoverflow.com/questions/8505163/is-it-possible-to-prefill-a-input-in-python-3s-command-line-interface

class MyPrompt(Cmd):
    prompt = 'pb> '
    intro = "Welcome! Type ? to list commands"
    t = ''

    def do_exit(self, inp):
        '''exit the application.'''
        print("Bye")
        return True

    def do_edit(self, inp):
        self.t = input_with_prefill("edit text> ", self.t)

    def do_show(self, inp):
        print(self.t)


MyPrompt().cmdloop()


