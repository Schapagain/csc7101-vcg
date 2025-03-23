import sys
from Tree import Stmt, Exp, OpExp

class IfStmt(Stmt):
    def __init__(self, condition, then_stmt, else_stmt):
        """
        Initialize an if-then-else statement.
        
        Args:
            condition: The condition expression (an Exp object)
            then_stmt: The statement to execute if condition is true (a Stmt object)
            else_stmt: The statement to execute if condition is false (a Stmt object)
        """
        self.condition = condition
        self.then_stmt = then_stmt
        self.else_stmt = else_stmt
    
    def print(self):
        """Print the if-then-else statement."""
        sys.stdout.write("if ")
        self.condition.print()
        sys.stdout.write(" then ")
        self.then_stmt.print()
        sys.stdout.write(" else ")
        self.else_stmt.print()
    
    def wp(self, post_condition):
        """
        Compute the weakest precondition for an if-then-else statement.
        
        For "if B then S1 else S2", the weakest precondition is:
        (B => wp(S1, Q)) and (not B => wp(S2, Q))
        where Q is the postcondition.
        
        Args:
            post_condition: The postcondition expression
            
        Returns:
            The weakest precondition expression
        """
        # Calculate wp for the 'then' branch
        wp_then = self.then_stmt.wp(post_condition)
        # Calculate wp for the 'else' branch
        wp_else = self.else_stmt.wp(post_condition)
        
        # (B => wp(S1, Q))
        condition_implies_then = OpExp(self.condition, OpExp.Op.IMP, wp_then)
        
        # (not B => wp(S2, Q))
        not_condition = OpExp(None, OpExp.Op.NOT, self.condition)
        not_condition_implies_else = OpExp(not_condition, OpExp.Op.IMP, wp_else)
        
        # Combine with AND: (B => wp(S1, Q)) and (not B => wp(S2, Q))
        return OpExp(condition_implies_then, OpExp.Op.AND, not_condition_implies_else)