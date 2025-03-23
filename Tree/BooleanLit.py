import sys
from Tree import Exp

class BooleanLit(Exp):
    def __init__(self, v):
        self.value = v

    def print(self):
        sys.stdout.write(str(self.value).lower())

    def substitute(self,ident,expr):
        return self