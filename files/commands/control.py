from .size import Size
from .radians import radians
from .graphing import GraphPolar
from .graphing import GraphCart
from time import sleep


class Commands:

    tool_set = 0

    expr_set = False

    isQuit = False

    expr = 0

    command_list = 'help setsize expr graph quit'.split()

    def __init__(self, comm):
        self.comm = comm

    def toolset(self, tool):
        self.tool_set = tool

    def check(self):
        if self.comm in self.command_list:
            return True
        else:
            return False

    def help(self):
        for i in self.command_list:
            print("· " + i)
            sleep(0.1)

    def thesize(self):
        s = Size()
        while True:
            try:
                x = int(input("Please enter a number: "))
                s.setsize(x)
                print("Window Size set to {}".format(s.getsize()))
                break
            except ValueError:
                print("Oops!  That was not a valid number.  Try again...")

    def expression(self):

        expr_string = input("Enter your expression: ")
        print("Your expression is set to {}".format(expr_string))
        expr_string = radians(expr_string)
        Commands.expr = expr_string
        Commands.expr_set = True

    def graph(self):
        s = Size()
        if self.tool_set == 'p':
            graph = GraphPolar(s.getsize())
            graph.draw(Commands.expr)
        elif self.tool_set == 'c':
            graph = GraphCart(s.getsize())
            graph.draw(Commands.expr)

    def quit(self):
        self.isQuit = True

    def getquit(self):
        return self.isQuit

    def run(self):
        if self.comm == 'help':
            Commands.help(self)

        elif self.comm == 'setsize':
            Commands.thesize(self)

        elif self.comm == 'expr':
            Commands.expression(self)

        elif self.comm == 'graph':
            if self.expr_set:
                Commands.graph(self)
            else:
                print("You have not set an expression")

        elif self.comm == 'quit':
            Commands.quit(self)
