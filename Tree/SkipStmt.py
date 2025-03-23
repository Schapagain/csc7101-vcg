import sys
from Tree import Stmt

class SkipStmt(Stmt):
    def __init__(self):
        pass
    
    def __str__(self):
        return "skip"
    
    def print(self):
        sys.stdout.write(str(self))

    def wp(self,post):
        return post
