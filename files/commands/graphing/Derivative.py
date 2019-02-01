from sympy import symbols, diff, sympify
from .Graph import Graph
from graphics import Line, Point
from .graphCart import GraphCart


class Derivative(Graph):

    def __init__(self, size, exprx, expry, point):
        Graph.__init__(self, size)
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

        half = float(Graph.getSize(self)/2)
        expr = sympify(self.expry)
        der = diff(expr)
        x = symbols("x")

        neg = -half*Derivative.value(self) + (expr.evalf(subs={x: self.point}) - self.point*der.evalf(subs={x: self.point}))

        pos = half*Derivative.value(self) + (expr.evalf(subs={x: self.point}) - self.point*der.evalf(subs={x: self.point}))

        return neg, pos

    def string(self):

        x = symbols("x")
        expr = sympify(self.expry)
        der = diff(expr)
        print("Equation of tangent:" " y = {}x + {}".format(Derivative.value(self),
                                     expr.evalf(subs={x: self.point}) - self.point*der.evalf(subs={x: self.point})))

    def graph(self):

        half = int(Graph.getSize(self)/2)

        p1 = Point(0, half - Derivative.slope(self)[0])
        p2 = Point(Graph.getSize(self), half - Derivative.slope(self)[1])

        line = Line(p1, p2)

        return line



