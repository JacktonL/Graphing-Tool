from sympy import symbols, diff, sympify
from .Graph import Graph
from graphics import Line, Point


class Derivative(Graph):

    def __init__(self, size, exprx, expry, point):
        Graph.__init__(self, size)
        self.exprx = exprx
        self.expry = expry
        self.point = sympify(point)

    def value(self):

        x = symbols("x")

        expry = diff(self.expry, x)
        exprx = diff(self.exprx, x)

        top = expry.evalf(subs={x: float(self.point)})
        bottom = exprx.evalf(subs={x: float(self.point)})

        return top/bottom

    def slope(self):

        half = float(Graph.getSize(self)/2)
        expry = sympify(self.expry)
        exprx = sympify(self.exprx)
        x = symbols("x")

        neg = expry.evalf(subs={x: self.point}) + Derivative.value(self)*(-half - exprx.evalf(subs={x: self.point}))

        pos = expry.evalf(subs={x: self.point}) + Derivative.value(self)*(half - exprx.evalf(subs={x: self.point}))

        return neg, pos

    def string(self):

        x = symbols("x")
        exprx = sympify(self.exprx)
        expry = sympify(self.expry)
        print("Equation of tangent: y = {}x + {}".format(Derivative.value(self),
                                                         expry.evalf(subs={x: self.point}) -
                                                         exprx.evalf(subs={x: self.point})*Derivative.value(self)))

    def graph(self):

        half = int(Graph.getSize(self)/2)

        p1 = Point(0, half - Derivative.slope(self)[0])
        p2 = Point(Graph.getSize(self), half - Derivative.slope(self)[1])

        line = Line(p1, p2)

        return line



