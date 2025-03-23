import sys
from enum import Enum
from enum import IntEnum
from Tree import Exp,Ident

class QuantExp(Exp):
    class Quant(IntEnum):
        FORALL = 0
        EXISTS = 1

    class LR(Enum):
        LEFT = 0
        RIGHT = 1

    __opnames = ["forall", "exists"]

    def __init__(self, quant, ident, expr):
        self.quant = quant
        self.ident = ident
        self.expr = expr.substitute(ident,Ident(f'${ident.name}'))

    def print(self):
        print(f"{QuantExp.__opnames[self.quant]} ${self.ident.name}.", end="")
        self.expr.print()

    def wp(self, post_condition):
        if self.quant == QuantExp.Q.FORALL:
            return QuantExp(QuantExp.Q.FORALL, self.ident, self.expr.wp(post_condition))
        else:
            return QuantExp(QuantExp.Q.EXISTS, self.ident, self.expr.wp(post_condition))
    
    def substitute(self, ident, exp):
        if self.ident == ident:
            return self
        return QuantExp(self.quant, self.ident, self.expr.substitute(ident, exp))