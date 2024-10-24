import re

TOKEN_TYPES = {
    'VAR': r'\bvar\b',
    'LET': r'\blet\b',
    'CONST': r'\bconst\b',
    'NUMBER': r'\b\d+\b',
    'IDENTIFIER': r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',
    'ASSIGN': r'=',
    'PLUS': r'\+',
    'MINUS': r'-',
    'SEMICOLON': r';',
    'WHITESPACE': r'[ \t\n]+',
    'STRING': r'"[^"]*"',
    'IF': r'\bif\b',
    'ELSE': r'\belse\b',
    'WHILE': r'\bwhile\b',
    'LEFT_BRACE': r'\{',
    'RIGHT_BRACE': r'\}',
    'LEFT_PAREN': r'\(',
    'RIGHT_PAREN': r'\)',
    'GT': r'>',
    'LT': r'<',
    'GE': r'>=',
    'LE': r'<=',
    'EQ': r'==',
    'NEQ': r'!='
}

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f'Token({self.type}, {self.value})'

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []
        self.pos = 0

    def tokenize(self):
        while self.pos < len(self.source_code):
            match = None
            for token_type, pattern in TOKEN_TYPES.items():
                regex = re.compile(pattern)
                match = regex.match(self.source_code, self.pos)
                if match:
                    if token_type != 'WHITESPACE':
                        token = Token(token_type, match.group(0))
                        self.tokens.append(token)
                    self.pos = match.end(0)
                    break
            if not match:
                raise ValueError(f'Error de tokenización en: {self.source_code[self.pos:]}')
        return self.tokens
