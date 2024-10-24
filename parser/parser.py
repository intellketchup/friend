from lexer.lexer import Lexer, Token
from ast.ast import ASTNode, BinaryOpNode, NumberNode, VarDeclarationNode, IfNode, WhileNode

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        return self.statement()

    def statement(self):
        current_token = self.current_token()
        if current_token.type in ('VAR', 'LET', 'CONST'):
            return self.var_declaration()
        elif current_token.type == 'IF':
            return self.if_statement()
        elif current_token.type == 'WHILE':
            return self.while_statement()
        else:
            return self.expression()

    def var_declaration(self):
        var_type = self.current_token()
        self.advance()
        identifier = self.current_token()
        self.expect('IDENTIFIER')
        self.advance()
        self.expect('ASSIGN')
        self.advance()
        value = self.expression()
        self.expect('SEMICOLON')
        self.advance()
        return VarDeclarationNode(var_type, identifier, value)

    def if_statement(self):
        self.expect('IF')
        self.advance()
        self.expect('LEFT_PAREN')
        self.advance()
        condition = self.expression()
        self.expect('RIGHT_PAREN')
        self.advance()
        self.expect('LEFT_BRACE')
        self.advance()
        then_branch = self.statement()
        self.expect('RIGHT_BRACE')
        self.advance()
        
        if self.current_token().type == 'ELSE':
            self.advance()
            self.expect('LEFT_BRACE')
            self.advance()
            else_branch = self.statement()
            self.expect('RIGHT_BRACE')
            self.advance()
            return IfNode(condition, then_branch, else_branch)
        
        return IfNode(condition, then_branch)

    def while_statement(self):
        self.expect('WHILE')
        self.advance()
        self.expect('LEFT_PAREN')
        self.advance()
        condition = self.expression()
        self.expect('RIGHT_PAREN')
        self.advance()
        self.expect('LEFT_BRACE')
        self.advance()
        body = self.statement()
        self.expect('RIGHT_BRACE')
        self.advance()
        return WhileNode(condition, body)

    def expression(self):
        left = self.term()
        while self.current_token().type in ('PLUS', 'MINUS', 'GT', 'LT', 'GE', 'LE', 'EQ', 'NEQ'):
            op = self.current_token()
            self.advance()
            right = self.term()
            left = BinaryOpNode(left, op, right)
        return left

    def term(self):
        current_token = self.current_token()
        if current_token.type == 'NUMBER':
            self.advance()
            return NumberNode(current_token)
        else:
            raise ValueError("Se esperaba un número")

    def current_token(self):
        return self.tokens[self.pos]

    def advance(self):
        self.pos += 1

    def expect(self, token_type):
        if self.current_token().type != token_type:
            raise ValueError(f'Se esperaba {token_type}, pero se encontró {self.current_token().type}')
