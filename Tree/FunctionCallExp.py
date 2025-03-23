import sys
from Tree import Exp

class FunctionCallExp(Exp):
    def __init__(self, ident, args):
        self.ident = ident 
        self.args = args 
    
    def __str__(self):
        args_str = ", ".join(str(arg) for arg in self.args)
        return f"{self.ident}({args_str})"
    
    def print(self):
        self.ident.print()
        sys.stdout.write("(")
        for i, arg in enumerate(self.args):
            if i > 0:
                sys.stdout.write(", ")
            arg.print()
        sys.stdout.write(")")
    
    def substitute(self, ident, exp):
        new_args = [arg.substitute(ident, exp) for arg in self.args]
        return FunctionCallExp(self.ident, new_args)
    
    def wp(self, post):
        return post
    
    def free_vars(self):
        result = set()
        for arg in self.args:
            result.update(arg.free_vars())
        return result