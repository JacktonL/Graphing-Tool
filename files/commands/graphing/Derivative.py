from sympy import symbols, diff, sympify


class Derivative:

    def __init__(self, exprx, expry, point):

        self.exprx = exprx
        self.expry = expry
        self.point = point

    def value(self):

        x = symbols("x")

        expry = diff(self.expry, x)
        exprx = diff(self.exprx, x)

        top = expry.subs(x, float(self.point))
        bottom = exprx.subs(x, float(self.point))

        return top/bottom

    def slope(self):

        neg = -800*Derivative.value(self) + (self.expry.subs("x", self.point) - -800*Derivative.value(self))

        pos = 800*Derivative.value(self) + (self.expry.subs("x", self.point) - 800*Derivative.value(self))

        return neg, pos

    def string(self):

        x = symbols("x")
        expr = self.expry.subs("x", x)
        return "y = {}x + {}".format(Derivative.value, expr.subs("x", self.point))
