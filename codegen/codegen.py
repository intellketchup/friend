from ast.ast import VarDeclarationNode, BinaryOpNode, NumberNode, IfNode, WhileNode

class CodeGenerator:
    def generate(self, node):
        if isinstance(node, VarDeclarationNode):
            return f'{node.var_type.value} {node.identifier.value} = {self.generate(node.value)};'
        elif isinstance(node, BinaryOpNode):
            return f'{self.generate(node.left)} {node.op.value} {self.generate(node.right)}'
        elif isinstance(node, NumberNode):
            return str(node.value)
        elif isinstance(node, IfNode):
            if_code = f'if ({self.generate(node.condition)}) {{ {self.generate(node.then_branch)} }}'
            if node.else_branch:
                if_code += f' else {{ {self.generate(node.else_branch)} }}'
            return if_code
        elif isinstance(node, WhileNode):
            return f'while ({self.generate(node.condition)}) {{ {self.generate(node.body)} }}'
        else:
            raise ValueError(f"Tipo de nodo desconocido: {type(node)}")
