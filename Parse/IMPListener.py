# Generated from IMP.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .IMPParser import IMPParser
else:
    from IMPParser import IMPParser

from Tree import *
import pdb
import sys


# This class defines a complete listener for a parse tree produced by IMPParser.
class IMPListener(ParseTreeListener):

    # Enter a parse tree produced by IMPParser#program.
    def enterProgram(self, ctx:IMPParser.ProgramContext):
        pass

    # Exit a parse tree produced by IMPParser#program.
    def exitProgram(self, ctx:IMPParser.ProgramContext):
        pass


    # Enter a parse tree produced by IMPParser#statementlist.
    def enterStatementlist(self, ctx:IMPParser.StatementlistContext):
        pass

    # Exit a parse tree produced by IMPParser#statementlist.
    def exitStatementlist(self, ctx:IMPParser.StatementlistContext):
        pass


    # Enter a parse tree produced by IMPParser#statement.
    def enterStatement(self, ctx:IMPParser.StatementContext):
        pass

    # Exit a parse tree produced by IMPParser#statement.
    def exitStatement(self, ctx:IMPParser.StatementContext):
        pass


    # Enter a parse tree produced by IMPParser#assertion.
    def enterAssertion(self, ctx:IMPParser.AssertionContext):
        pass

    # Exit a parse tree produced by IMPParser#assertion.
    def exitAssertion(self, ctx:IMPParser.AssertionContext):
        pass


    # Enter a parse tree produced by IMPParser#boolexp.
    def enterBoolexp(self, ctx:IMPParser.BoolexpContext):
        pass

    # Exit a parse tree produced by IMPParser#boolexp.
    def exitBoolexp(self, ctx:IMPParser.BoolexpContext):
        pass


    # Enter a parse tree produced by IMPParser#boolterm.
    def enterBoolterm(self, ctx:IMPParser.BooltermContext):
        pass

    # Exit a parse tree produced by IMPParser#boolterm.
    def exitBoolterm(self, ctx:IMPParser.BooltermContext):
        pass


    # Enter a parse tree produced by IMPParser#boolterm2.
    def enterBoolterm2(self, ctx:IMPParser.Boolterm2Context):
        pass

    # Exit a parse tree produced by IMPParser#boolterm2.
    def exitBoolterm2(self, ctx:IMPParser.Boolterm2Context):
        pass


    # Enter a parse tree produced by IMPParser#boolfactor.
    def enterBoolfactor(self, ctx:IMPParser.BoolfactorContext):
        pass

    # Exit a parse tree produced by IMPParser#boolfactor.
    def exitBoolfactor(self, ctx:IMPParser.BoolfactorContext):
        pass


    # Enter a parse tree produced by IMPParser#compexp.
    def enterCompexp(self, ctx:IMPParser.CompexpContext):
        pass

    # Exit a parse tree produced by IMPParser#compexp.
    def exitCompexp(self, ctx:IMPParser.CompexpContext):
        pass


    # Enter a parse tree produced by IMPParser#arithexp.
    def enterArithexp(self, ctx:IMPParser.ArithexpContext):
        pass

    # Exit a parse tree produced by IMPParser#arithexp.
    def exitArithexp(self, ctx:IMPParser.ArithexpContext):
        pass


    # Enter a parse tree produced by IMPParser#arithterm.
    def enterArithterm(self, ctx:IMPParser.ArithtermContext):
        pass

    # Exit a parse tree produced by IMPParser#arithterm.
    def exitArithterm(self, ctx:IMPParser.ArithtermContext):
        pass


    # Enter a parse tree produced by IMPParser#arithfactor.
    def enterArithfactor(self, ctx:IMPParser.ArithfactorContext):
        pass

    # Exit a parse tree produced by IMPParser#arithfactor.
    def exitArithfactor(self, ctx:IMPParser.ArithfactorContext):
        pass


    # Enter a parse tree produced by IMPParser#arithexplist.
    def enterArithexplist(self, ctx:IMPParser.ArithexplistContext):
        pass

    # Exit a parse tree produced by IMPParser#arithexplist.
    def exitArithexplist(self, ctx:IMPParser.ArithexplistContext):
        pass


    # Enter a parse tree produced by IMPParser#ident.
    def enterIdent(self, ctx:IMPParser.IdentContext):
        pass

    # Exit a parse tree produced by IMPParser#ident.
    def exitIdent(self, ctx:IMPParser.IdentContext):
        pass


    # Enter a parse tree produced by IMPParser#integer.
    def enterInteger(self, ctx:IMPParser.IntegerContext):
        pass

    # Exit a parse tree produced by IMPParser#integer.
    def exitInteger(self, ctx:IMPParser.IntegerContext):
        pass



del IMPParser