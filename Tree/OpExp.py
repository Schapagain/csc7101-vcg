import sys
from enum import Enum
from enum import IntEnum
from Tree import Exp

class OpExp(Exp):
    class Op(IntEnum):
        IMP = 0
        EQV = 1
        OR = 2
        AND = 3
        NOT = 4
        LT = 5
        LE = 6
        EQ = 7
        NE = 8
        GT = 9
        GE = 10
        PLUS = 11
        MINUS = 12
        TIMES = 13
        DIV = 14
        UMINUS = 15

    class LR(Enum):
        LEFT = 0
        RIGHT = 1

    __opnames = [" => ", " <=> ", " or ", " and ", "not ",
                 "<", "<=", "=", "!=", ">", ">=",
                 "+", "-", "*", "/", "-"]
    
    __precedence = [2, 2, 3, 4, 5,
                    6, 6, 6, 6, 6, 6,
                    7, 7, 8, 8, 9]
    
    def __init__(self, l, o, r):
        self.left = l
        self.op = o
        self.right = r

    def print(self):
        if self.left != None:
            self.left._print(self.op, OpExp.LR.LEFT)
        sys.stdout.write(OpExp.__opnames[int(self.op)])
        self.right._print(self.op, OpExp.LR.RIGHT)

    def _print(self, parent, child):
        if (OpExp.__precedence[int(parent)]>OpExp.__precedence[int(self.op)] or
                (child==OpExp.LR.RIGHT and parent==OpExp.Op.MINUS and
                 self.op==OpExp.Op.MINUS)):
            sys.stdout.write('(')
            self.print()
            sys.stdout.write(')')
        else:
            self.print()


    def substitute(self, ident, expr):
        if self.left is None:
            new_right = self.right.substitute(ident, expr)
            return OpExp(None, self.op, new_right)
        else: 
            new_left = self.left.substitute(ident, expr)
            new_right = self.right.substitute(ident, expr)
            return OpExp(new_left, self.op, new_right)
