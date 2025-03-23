#!/usr/bin/python3

import sys
from antlr4 import *
from Parse import *
from Tree import *


def main(argv):
    if (len(argv) != 2):
        sys.stderr.write("Usage: python3 VCG.py test.vcg\n")
        sys.exit(1)

    input = FileStream(argv[1])
    lexer = IMPLexer(input)
    tokens = CommonTokenStream(lexer)
    parser = IMPParser(tokens)

    parser.program()


if __name__ == "__main__":
    main(sys.argv)
