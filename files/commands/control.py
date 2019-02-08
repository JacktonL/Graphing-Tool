from .size import Size
from .radians import radians
from .graphing import GraphPolar
from .graphing import GraphPara
from .graphing import Derivative
from time import sleep
from sympy import sympify


class Commands:

    size = Size()
    tool_set = 0
    expr_set = False
    derv_set = False
    isQuit = False
    expr1 = ""
    expr2 = ""
    scale_value = "1"

    command_list = 'help setsize scale expr graph tang quit'.split()

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

    def scale(self):

        scale_value = input("Enter a value to scale by: ")

        try:
            scale_value = sympify(scale_value)
            float(scale_value)
            Commands.scale_value = str(scale_value)
            print("Scale set to {}".format(Commands.scale_value))
        except TypeError:
            print("Cannot scale by {}".format(scale_value))
            print("Enter an expression or number to scale")

    def true_expression(self):
        if self.tool_set == "c":
            return self.expr1, self.expr2+"*"+self.scale_value
        else:
            return self.expr1+"*"+self.scale_value, self.expr2+"*"+self.scale_value

    def expression(self):
        if self.tool_set == "t":
            expr_stringx = input("Enter your X expression: ")
            expr_stringy = input("Enter your Y expression: ")
            print("Your expression X is set to {}".format(expr_stringx))
            print("Your expression Y is set to {}".format(expr_stringy))

            expr_string1 = radians(expr_stringx)
            expr_string2 = radians(expr_stringy)

            Commands.expr1 = "("+expr_string1+")"
            Commands.expr2 = "("+expr_string2+")"
            Commands.expr_set = True

        elif self.tool_set == "p":
            expr_string = input("Enter your expression: ")
            print("Your expression is set to {}".format(expr_string))
            expr_string = radians(expr_string)
            Commands.expr1 = "("+expr_string+")"+"*cos(rad(x))"
            Commands.expr2 = "("+expr_string+")"+"*sin(rad(x))"
            Commands.expr_set = True
        else:
            expr_string = input("Enter your expression: ")
            print("Your expression is set to {}".format(expr_string))
            expr_string = radians(expr_string)
            Commands.expr1 = "x"
            Commands.expr2 = "(" + expr_string + ")"
            Commands.expr_set = True

    def differentiate(self):

        expr_string = input("Enter a value to differentiate at: ")

        if "pi" in expr_string:
            expr_string.replace("pi", "3.14159265")

        try:
            if self.tool_set == 't' or self.tool_set == 'c':
                graph = GraphPara(self.size.getsize())
                tang = Derivative(self.size.getsize(),
                                  Commands.true_expression(self)[0],
                                  Commands.true_expression(self)[1], expr_string)
                graph.draw(Commands.true_expression(self)[0], Commands.true_expression(self)[1], tang)
                self.derv_set = True

            else:
                graph = GraphPolar(self.size.getsize())
                tang = Derivative(self.size.getsize(),
                                  Commands.true_expression(self)[0],
                                  Commands.true_expression(self)[1], expr_string)
                graph.draw(Commands.true_expression(self)[0], Commands.true_expression(self)[1], tang)
                self.derv_set = True

        except ValueError:
            print("Enter a number to differentiate")

    def graph(self):
        if self.tool_set == 'p':
            graph = GraphPolar(self.size.getsize())
            graph.draw(Commands.true_expression(self)[0], Commands.true_expression(self)[1])
        else:
            graph = GraphPara(self.size.getsize())
            graph.draw(Commands.true_expression(self)[0], Commands.true_expression(self)[1])

    def quit(self):
        self.isQuit = True

    def getquit(self):
        return self.isQuit

    def run(self):
        if self.comm == 'help':
            Commands.help(self)

        elif self.comm == 'setsize':
            Commands.thesize(self)

        elif self.comm == 'scale':
            Commands.scale(self)

        elif self.comm == 'expr':
            Commands.expression(self)

        elif self.comm == 'graph':
            if self.expr_set:
                Commands.graph(self)
            else:
                print("You have not set an expression")

        elif self.comm == 'tang':
            if self.expr_set:
                Commands.differentiate(self)
            else:
                print("You have not set an expression")

        elif self.comm == 'quit':
            Commands.quit(self)
