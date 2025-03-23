grammar IMP;

@header {
from Tree import *
import pdb
import sys
}

program
    : pre=assertion st=statementlist post=assertion
		{
# FIXME: Construct and print verification condition instead
wp = $statementlist.tree.wp($post.tree)
$pre.tree.print() 
sys.stdout.write(" => ")
wp.print()
sys.stdout.write("\n")
sys.stdout.flush()

		}
    ;

statementlist returns [Stmt tree]
    : statement
    {$tree = $statement.tree}
    | statement ';' statementlist
    {$tree = CompoundStmt($statement.tree, $statementlist.tree)}
    ;

statement returns [Stmt tree]
    : 'skip'
    {$tree = SkipStmt()}
    | ident ':=' arithexp
    {$tree = AssignStmt($ident.name, $arithexp.tree)}
    | 'begin' statementlist 'end'
    {$tree = $statementlist.tree}
    | 'if' boolterm 'then' s1=statement 'else' s2=statement
    {$tree = IfStmt($boolterm.tree, $s1.tree, $s2.tree)}
    | inv=assertion 'while' t3=boolterm 'do' st=statement
    {$tree = WhileStmt($inv.tree, $t3.tree, $st.tree)}
    | 'assert' assertion
    {$tree = AssertStmt($assertion.tree)}
    ;

assertion returns [Exp tree]
    : '{' boolexp '}'
		{$tree = $boolexp.tree}
    ;

boolexp returns [Exp tree]
    : boolterm
		{$tree = $boolterm.tree}
    | t1=boolterm '=>' t2=boolterm
    {$tree = OpExp($t1.tree,OpExp.Op.IMP,$t2.tree)}
    | t1=boolterm '<=>' t2=boolterm
    {$tree = OpExp($t1.tree,OpExp.Op.EQV,$t2.tree)}
    ;

boolterm returns [Exp tree]
    : boolterm2
		{$tree = $boolterm2.tree}
    | t1=boolterm 'or' t2=boolterm2
    {$tree = OpExp($t1.tree,OpExp.Op.OR,$t2.tree)}
    ;

boolterm2 returns [Exp tree]
    : boolfactor
		{$tree = $boolfactor.tree}
    | t1=boolterm2 'and' t2=boolfactor
    {$tree = OpExp($t1.tree,OpExp.Op.AND,$t2.tree)}
    ;

boolfactor returns [Exp tree]
    : 'true'
    {$tree = BooleanLit(True)}
    | 'false'
    {$tree = BooleanLit(False)}
    | compexp
		{$tree = $compexp.tree}
    | 'forall' ident '.' boolexp
    {$tree = QuantExp(QuantExp.Quant.FORALL, $ident.name, $boolexp.tree)}
    | 'exists' ident '.' boolexp
    {$tree = QuantExp(QuantExp.Quant.EXISTS, $ident.name, $boolexp.tree)}
    | 'not' boolfactor
    {$tree = OpExp(None, OpExp.Op.NOT, $boolfactor.tree)}
    | '(' boolexp ')'
		{$tree = $boolexp.tree}
    ;

compexp returns [Exp tree]
    : t1=arithexp '<' t2=arithexp
    {$tree = OpExp($t1.tree, OpExp.Op.LT, $t2.tree)}
    | t1=arithexp '<=' t2=arithexp
    {$tree = OpExp($t1.tree, OpExp.Op.LE, $t2.tree)}
    | t1=arithexp '=' t2=arithexp
		{$tree = OpExp($t1.tree, OpExp.Op.EQ, $t2.tree)}
    | t1=arithexp '!=' t2=arithexp
    {$tree = OpExp($t1.tree, OpExp.Op.NE, $t2.tree)}
    | t1=arithexp '>=' t2=arithexp
    {$tree = OpExp($t1.tree, OpExp.Op.GE, $t2.tree)}
    | t1=arithexp '>' t2=arithexp
    {$tree = OpExp($t1.tree, OpExp.Op.GT, $t2.tree)}
    ;

arithexp returns [Exp tree]
    : arithterm
		{$tree = $arithterm.tree}
    | t1=arithexp '+' t2=arithterm
		{$tree = OpExp($t1.tree, OpExp.Op.PLUS, $t2.tree)}
    | t1=arithexp '-' t2=arithterm
		{$tree = OpExp($t1.tree, OpExp.Op.MINUS, $t2.tree)}
    ;

arithterm returns [Exp tree]
    : arithfactor
		{$tree = $arithfactor.tree}
    | t1=arithterm '*' t2=arithfactor
		{$tree = OpExp($t1.tree, OpExp.Op.TIMES, $t2.tree)}
    | t1=arithterm '/' t2=arithfactor
		{$tree = OpExp($t1.tree, OpExp.Op.DIV, $t2.tree)}
    ;

arithfactor returns [Exp tree]
    : ident
		{$tree = $ident.name}
    | integer
		{$tree = $integer.value}
    | '-' arithfactor
    {$tree = OpExp(None, OpExp.Op.UMINUS, $arithfactor.tree)}
    | '(' arithexp ')'
		{$tree = $arithexp.tree}
    | ident '(' arithexplist ')'
    {$tree = FunctionCallExp($ident.name, $arithexplist.list)}
    ;

arithexplist returns [list list]
    : arithexp
    {$list = [$arithexp.tree]}
    | arithexp ',' arithexplist
    {$list = [$arithexp.tree] + $arithexplist.list}
    ;

ident returns [Ident name]
    : IDENT
		{$name = Ident($IDENT.text)}
    ;

integer returns [IntLit value]
    : INT
		{$value = IntLit(int($INT.text))}
    ;


IDENT
    : [A-Za-z][A-Za-z0-9_]*
    ;

INT
    : [0]|[1-9][0-9]*
    ;

WS
    : [ \r\n\t] -> skip
    ;
