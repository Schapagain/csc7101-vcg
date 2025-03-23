import sys
from Tree import Stmt, Exp, OpExp

class AssertStmt(Stmt):
    def __init__(self, assertion):
        """
        Initialize an assert statement.
        
        Args:
            assertion: The assertion expression (an Exp object)
        """
        self.assertion = assertion
    
    def print(self):
        """Print the assert statement."""
        sys.stdout.write("assert ")
        self.assertion.print()
    
    def wp(self, post_condition):
        
        # Print the implication condition
        assertion_implies_post = OpExp(self.assertion, OpExp.Op.IMP, post_condition)
        assertion_implies_post.print()
        sys.stdout.write("\n")
        
        # Return the assertion as the effective precondition
        # This allows other statements to connect with this precondition
        return self.assertion