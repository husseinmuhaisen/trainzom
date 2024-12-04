from tokens import *
from model import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.curr = 0 

    # Token by token
    def advance(self):
        # consume the current token and advance to the next one
        token = self.token[self.curr]
        self.curr = self.curr + 1
        return token
    
    def peek(self):
        # return the current token
        return self.tokens[self.curr]
        
    def is_next(self, expected_type):
        # check if the next token matches the expected type
        if self.curr >= len(self.tokens):
            return False
        return self.peek().token_type() == expected_type

    def expect(self, expected_type):
        # test if the current token is of the expected type else display an error
        if self.curr >= len(self.tokens):
           raise  SyntaxError(f'Found {self.previous_token().lexeme!r} at the end of parsing')
        elif self.peek().token_type == expected_type:
            token = self.advance()
            return token
        else:
            raise SyntaxError(f'Expected {expected_type!r}, found {self.peek().lexeme!r}.')
    
    def previous_token(self):
        # return the previous token 
        return self.tokens[self.curr - 1]
    
    def match(self, expected_type):
        # check if current token matches the expected type and return the token, else false
        if self.curr >= len(self.tokens):
            return False
        if self.peek().token_type != expected_type:
            return False
        self.curr = self.curr + 1
        return True

    #  <primary> ::= <integer> | <float> | '(' <expr> ')'
    def primary(self):
        if self.match(TOK_INTEGER): return Integer(int(self.previous_token().lexeme))
        if self.match(TOK_FLOAT): return Float(float(self.previous_token().lexeme))
        if self.match(TOK_LPAREN):
            expr = self.expr()
            if(not self.match(TOK_RPAREN)):
                raise SyntaxError(f'Error: ")" expected.')
            else:
                return Grouping(expr)

    # <unary> ::= ('+'|'-'|'~') <unary> | <primary>
    def unary(self):
        if self.match(TOK_NOT) or self.match(TOK_MINUS) or self.match(TOK_PLUS):
            op = self.previous_token()
            operand = self.unary()
            return UnOp(op, operand)
        return self.primary()
    
    # <factor> ::= <unary>
    def factor(self):
        return self.unary()
    
    # <term> ::= <factor> ( ('/') <factor> )*
    def term(self):
        expr = self.factor()
        while self.match(TOK_STAR) or self.match(TOK_SLASH):
            op = self.previous_token()
            right = self.factor()
            expr = BinOp(op, expr, right)
        return expr
    
    # <expr> ::= <term> ( ('+'|'-') <term> )*
    def expr(self):
        expr = self.term()
        while self.match(TOK_PLUS) or self.match(TOK_MINUS):
            op = self.previous_token()
            right = self.term()
            expr = BinOp(op, expr, right)
        return expr

    def parse(self):
        # Start parsing an expression -- first entry door
        ast = self.expr()
        return ast

