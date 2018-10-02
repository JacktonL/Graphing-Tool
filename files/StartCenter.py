from time import sleep
from .commands import Commands


class Start:

    def __init__(self, name, typ):
        self.name = name
        self.typ = typ

    def start(self):

        for i in range(1, 5):
            print('. ' * i)
            sleep(0.1)

        print("Welcome to the {} Tool!".format(self.name.title()))

        while True:
            comm = input("Enter a command or 'help' for list of commands ")
            c = Commands(comm)
            c.toolset(self.typ)

            if c.check():
                c.run()
                if c.getquit():
                    print('Exiting {} tool...'.format(self.name))
                    break

            else:
                print("That is not a valid command!")
