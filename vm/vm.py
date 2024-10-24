class VM:
    def __init__(self):
        self.variables = {}

    def execute(self, code):
        for statement in code.split(';'):
            self._execute_statement(statement.strip())

    def _execute_statement(self, statement):
        if '=' in statement:
            var, expr = statement.split('=')
            var = var.strip()
            expr = expr.strip()
            self.variables[var] = eval(expr, {}, self.variables)
        elif 'if' in statement:
            pass
        elif 'while' in statement:
            pass
        else:
            print(f"Unknown statement: {statement}")

# Ejemplo de uso:
vm = VM()
vm.execute("x = 3 + 5; y = x * 2;")
print(vm.variables)
