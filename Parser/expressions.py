from enum import Enum

class ExpressionType(Enum):
    UNARY = 1
    BINARY = 2
    STRING_LITERAL = 3
    NUMERIC_LITERAL = 4
    GROUPING = 5

class Expression:
    type = None
    expression = None
    left_expression = None
    operator = None
    right_expression = None
    string_literal = None
    numeric_literal = None
    inner_expression = None

    def __init__(self, operator = None, left_expression = None, right_expression = None,
                 string_literal = None, numeric_literal = None, inner_expression = None):
        if(left_expression != None and operator != None and right_expression != None):
            self.type = ExpressionType.BINARY
            self.left_expression = left_expression
            self.operator = operator
            self.right_expression = right_expression
        elif(operator != None and expression != None):
            self.type = ExpressionType.UNARY
            self.operator = operator
            self.expression = expression
        elif(string_literal != None):
            self.type = ExpressionType.STRING_LITERAL
            self.string_literal = string_literal
        elif(numeric_literal != None):
            self.type = ExpressionType.NUMERIC_LITERAL
            self.numeric_literal = numeric_literal
        elif(inner_expression != None):
            self.type = ExpressionType.GROUPING
            self.inner_expression = inner_expression

    def __str__(self):
        if(self.type == ExpressionType.UNARY):
            return '{} {}'.format(self.operator, str(self.expression))
        elif(self.type == ExpressionType.STRING_LITERAL):
            return self.string_literal
        elif(self.type == ExpressionType.NUMERIC_LITERAL):
            return str(self.numeric_literal)
        elif(self.type == ExpressionType.GROUPING):
            return '({})'.format(str(self.inner_expression))
        elif(self.type == ExpressionType.BINARY):
            return '{} {} {}'.format(str(self.left_expression), self.operator, str(self.right_expression))
