import sys
sys.path.append('C:\\Users\\Alex\\Interpreter\\Scanner\\')
from Token import TokenType
from Scanner import MantisScanner
from expressions import Expression

class Parser:
    tokens = None
    current = 0
    def __init__(self, tokens):
        self.tokens = tokens

    def parse_tokens(self):
        while(self.tokens[self.current].type != TokenType.EOF):
            print(str(self.tokens[self.current]))
            self.current += 1

    def peek_token(self):
        return self.tokens[self.current + 1]

    def current_token(self):
        return self.tokens[self.current]

    def advance(self):
        self.current += 1
        
    def parseExpression(self):
        if()


p = Parser(MantisScanner().tokens_from('C:\\Users\\Alex\\Interpreter\\Scanner\\test.mantis'))
p.parse_tokens()

#print(str(Expression(operator='*', left_expression=Expression(numeric_literal=234), right_expression=Expression(inner_expression=Expression(left_expression=Expression(numeric_literal=5.6), operator='+', right_expression=Expression(numeric_literal=6))))))
