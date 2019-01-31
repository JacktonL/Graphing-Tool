from sympy import symbols, diff, sympify
from .Graph import Graph
from graphics import Line


class Derivative:

    def __init__(self, exprx, expry, point):

        self.exprx = exprx
        self.expry = expry
        self.point = point

    def value(self):

        x = symbols("x")

        expry = diff(self.expry, x)
        exprx = diff(self.exprx, x)

        top = expry.evalf(subs={x: float(self.point)})
        bottom = exprx.evalf(subs={x: float(self.point)})

        return top/bottom

    def slope(self):

        graph = Graph(self)
        half = float(graph.getSize()/2)

        neg = -half*Derivative.value(self) + (self.expry.subs("x", self.point) - -half*Derivative.value(self))

        pos = half*Derivative.value(self) + (self.expry.subs("x", self.point) - half*Derivative.value(self))

        return neg, pos

    def string(self):

        x = symbols("x")
        expr = sympify(self.expry)
        der = diff(expr)
        return "y = {}x + {}".format(Derivative.value(self),
                                     expr.evalf(subs={x: self.point}) - self.point*der.evalf(subs={x: self.point}))

    def graph(self):

        graph = Graph(self)
        win = graph.window()
        half = float(graph.getSize()/2)

        line = Line(half + Derivative.slope(self)[0], Derivative.slope(self)[1])

        line.draw(win)