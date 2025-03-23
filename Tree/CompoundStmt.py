from Tree import Stmt
class CompoundStmt(Stmt):
    def __init__(self, first, rest):
        self.first = first
        self.rest = rest
    
    def print(self):
        self.first.print()
        print(";", end=" ")
        self.rest.print()
    
    def wp(self, post):
        """
        wp(S1;S2, Q) = wp(S1, wp(S2, Q))
        """
        intermediate_condition = self.rest.wp(post)
        return self.first.wp(intermediate_condition)