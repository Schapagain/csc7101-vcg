import sys
from Tree import Stmt, Exp, OpExp

class WhileStmt(Stmt):
    def __init__(self, invariant, condition, body):
        self.invariant = invariant
        self.condition = condition
        self.body = body
    
    def print(self):
        self.invariant.print()
        sys.stdout.write(" while ")
        self.condition.print()
        sys.stdout.write(" do ")
        self.body.print()
    
    def wp(self, post):
        """
        Compute and print the verification conditions for a while loop:
        1. Exit condition: I and not B => Q
        2. Invariant maintenance: I and B => wp(S, I)
        3. Before loop: P => I (where P is the precondition)
        
        Returns a placeholder expression representing the combined conditions.
        """
        # 1. Exit condition: (I and not B => Q)
        not_condition = OpExp(None, OpExp.Op.NOT, self.condition)
        invariant_and_not_condition = OpExp(self.invariant, OpExp.Op.AND, not_condition)
        exit_condition = OpExp(invariant_and_not_condition, OpExp.Op.IMP, post)
        
        
        
        # 2. Invariant maintenance: (I and B => wp(S, I))
        invariant_and_condition = OpExp(self.invariant, OpExp.Op.AND, self.condition)
        wp_body_invariant = self.body.wp(self.invariant)
        invariant_condition = OpExp(invariant_and_condition, OpExp.Op.IMP, wp_body_invariant)
        
        # Print exit condition
        exit_condition.print()
        sys.stdout.write("\n")

        # Print invariant condition
        invariant_condition.print()
        sys.stdout.write("\n")
        
        # 3. The precondition implies the invariant
        # This will be used when this while statement is part of a larger program
        
        # We return the invariant as the effective wp
        # This allows other statements to build verification conditions
        # that ensure the invariant holds before the loop
        return self.invariant