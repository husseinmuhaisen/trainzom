import sys
from tokens import *
from lexer import *

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('usage: python3 trainzom.py <filename>')
    filename = sys.argv[1]
    print(filename)

    """
    Now that we have the source ready we need to start tokenizing

    """
    with open(filename) as file:
        source = file.read()
        print("LEXER:")
        tokens = Lexer(source).tokenize()
        for tok in tokens: print(tok)



# todo: Tokenize the input source.
