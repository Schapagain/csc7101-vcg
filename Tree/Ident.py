import sys
from Tree import Exp

class Ident(Exp):
    def __init__(self, n):
        self.name = n

    def print(self):
        sys.stdout.write(self.name)

    def substitute(self, ident, expr):
        if self.name == ident.name:
            return expr
        return self