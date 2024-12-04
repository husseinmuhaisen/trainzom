import sys
from utils import *
from tokens import *
from lexer import *
from parser import *

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('usage: python3 trainzom.py <filename>')
    filename = sys.argv[1]
    print(filename)
    with open(filename) as file:
        source = file.read()
        print("LEXER:")
        tokens = Lexer(source).tokenize()
        for tok in tokens: print(tok)

        print("PARSED AST:")
        ast = Parser(tokens).parse()
        print(ast)

        print(f'***********************************************************')
        print('SOURCE: ')
        print(f'***********************************************************')
        print(source)

        print(f'***********************************************************')
        print('LEXER: ')
        print(f'***********************************************************')
        tokens = Lexer(source).tokenize()
        for tok in tokens: print(tok)

        print()
        print(f'***********************************************************')
        print('PARSED AST: ')
        print(f'***********************************************************')
        ast = Parser(tokens).parse()
        print_pretty_ast(ast)


