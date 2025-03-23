import sys
from Tree import Exp

class IntLit(Exp):
    def __init__(self, v):
        self.value = v

    def print(self):
        sys.stdout.write(str(self.value))

    def substitute(self,ident,expr):
        return self