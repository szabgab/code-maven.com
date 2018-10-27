from cmd import Cmd


class MyPrompt(Cmd):
    prompt = 'pb> '
    intro = "Welcome! Type ? to list commands"
    t = 'p> '

    def do_exit(self, inp):
        '''exit the application.'''
        print("Bye")
        return True

    def do_set(self, inp):
        self.text = input("input text> ")

    def do_show(self, inp):


if __name__ == '__main__':
    MyPrompt().cmdloop()

