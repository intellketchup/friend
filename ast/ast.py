class ASTNode:
    pass

class BinaryOpNode(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class NumberNode(ASTNode):
    def __init__(self, token):
        self.token = token
        self.value = int(token.value)

class VarDeclarationNode(ASTNode):
    def __init__(self, var_type, identifier, value):
        self.var_type = var_type
        self.identifier = identifier
        self.value = value

class IfNode(ASTNode):
    def __init__(self, condition, then_branch, else_branch=None):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch

class WhileNode(ASTNode):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body
