import pytest
from lexer.lexer import Lexer

def test_lexer():
    source_code = 'let x = 10 + 20;'
    lexer = Lexer(source_code)
    tokens = lexer.tokenize()
    assert len(tokens) == 7
    assert tokens[0].type == 'LET'
    assert tokens[1].type == 'IDENTIFIER'
    assert tokens[2].type == 'ASSIGN'
    assert tokens[3].type == 'NUMBER'

if __name__ == '__main__':
    pytest.main()
