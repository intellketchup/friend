from lexer.lexer import Lexer
from parser.parser import Parser
from codegen.codegen import CodeGenerator
from vm.vm import VM

def main():
    source_code = 'let x = 3 + 5; if (x > 5) { let y = 2; } else { let y = 10; }'
    lexer = Lexer(source_code)
    tokens = lexer.tokenize()
    
    parser = Parser(tokens)
    ast = parser.parse()
    
    codegen = CodeGenerator()
    js_code = codegen.generate(ast)
    
    print("Generated JS Code:")
    print(js_code)
    
    vm = VM()
    vm.execute(js_code)

if __name__ == '__main__':
    main()
