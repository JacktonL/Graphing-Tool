from .Graph import Graph
from sympy import *
from graphics import *
from math import *
from math import radians as rad


class GraphPara(Graph):

    def __init__(self, size):
        Graph.__init__(self, size)

    def draw(self, expr1, expr2, tang=False):

        plist = []

        j = 0

        size = self.size

        temp1 = expr1

        temp2 = expr2

        win = Graph.window(self)

        Graph.drawAxis(self, win)

        half = int(size / 2)

        for i in range(-half, half):

            expr1 = temp1

            expr2 = temp2

            expr1 = sympify(expr1)

            expr2 = sympify(expr2)

            x = symbols('x')

            expr1 = expr1.evalf(subs={x: i})

            expr2 = expr2.evalf(subs={x: i})
            try:
                point = Point(expr1 + half, half - expr2)
                plist.append(point)
                if len(plist) > 1:
                    line = Line(plist[j], plist[j+1])
                    j += 1
                    line.draw(win)
            except TypeError:
                pass

        if tang:
            tang.graph().draw(win)
            tang.string()

        win.getMouse()
        win.close()
