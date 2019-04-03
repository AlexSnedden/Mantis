""" classes to represent tokens """

from enum import Enum

class TokenType(Enum):
    def __str__(self):
        return str(self.value)

    # single character
    LEFT_PAREN =    1
    RIGHT_PAREN =   2
    LEFT_BRACE =    3
    RIGHT_BRACE =   4
    COMMA =         5
    DOT =           6
    MINUS =         7
    PLUS =          8
    SEMICOLON =     9
    STAR =          10
    #one or two characters
    ASSIGN =        11
    NOT_EQUAL =     12
    EQUAL =         13
    GREATER =       14
    GREATER_EQUAL = 15
    LESS =          16
    LESS_EQUAL =    18

    #Literals
    STRING_LITERAL =       19
    #eoF
    EOF =           20

class Token:
    type = 0
    lexeme = ""
    literal = None
    line = 0

    def __init__(self, type, lexeme, literal, line):
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def get_type(self):
        return self.type

    def __str__(self):
        if(self.literal):
            return '{} line {} : {}'.format(self.type.name, self.line, self.literal)
        return 'Token {} line {}'.format(self.type.name, self.line)
