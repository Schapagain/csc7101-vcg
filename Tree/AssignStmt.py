import sys
from Tree import Stmt

class AssignStmt(Stmt):
    def __init__(self, ident, expr):
        self.ident = ident
        self.expr = expr
    
    def __str__(self):
        return f"{self.ident} := {self.expr}"
    
    def print(self):
        sys.stdout.write(str(self))

    def wp(self, post_condition):
        return post_condition.substitute(self.ident, self.expr)
    