from .size import Size
from .radians import radians
from .graphing import GraphPolar
from .graphing import GraphCart
from .graphing import GraphPara
from .graphing import Derivative
from time import sleep


class Commands:

    tool_set = 0

    expr_set = False

    derv_set = False

    isQuit = False

    expr1 = ""

    expr2 = ""

    command_list = 'help setsize expr derv graph quit'.split()

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
        if self.tool_set == "t":
            expr_stringx = input("Enter your X expression: ")
            expr_stringy = input("Enter your Y expression: ")
            print("Your expression X is set to {}".format(expr_stringx))
            print("Your expression Y is set to {}".format(expr_stringy))

            expr_string1 = radians(expr_stringx)
            expr_string2 = radians(expr_stringy)

            Commands.expr1 = expr_string1
            Commands.expr2 = expr_string2
            Commands.expr_set = True

        else:
            expr_string = input("Enter your expression: ")
            print("Your expression is set to {}".format(expr_string))
            expr_string = radians(expr_string)
            Commands.expr1 = expr_string
            Commands.expr_set = True

    def differentiate(self):

        expr_string = input("Enter a value to differentiate at: ")

        try:
            if self.tool_set == 't':
                diff = Derivative(self.expr1, self.expr2, float(expr_string))
                self.derv_set = True
            elif self.tool_set == 'p':
                diff = Derivative(self.expr1+"*cos(x)", self.expr1+"*sin(x)", float(expr_string))
                self.derv_set = True
            else:
                diff = Derivative("x", self.expr1, float(expr_string))
                self.derv_set = True
                diff.graph()

            print("The slope at {} is: {}".format(expr_string, diff.string()))
        except ValueError:
            print("Enter a number to differentiate")

    def graph(self):
        s = Size()
        if self.tool_set == 'p':
            graph = GraphPolar(s.getsize())
            graph.draw(Commands.expr1)
        elif self.tool_set == 'c':
            graph = GraphCart(s.getsize())
            graph.draw(Commands.expr1)
        elif self.tool_set == "t":
            graph = GraphPara(s.getsize())
            graph.draw(Commands.expr1, Commands.expr2)

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

        elif self.comm == 'derv':
            if self.expr_set:
                Commands.differentiate(self)
            else:
                print("You have not set an expression")
        elif self.comm == 'quit':
            Commands.quit(self)
