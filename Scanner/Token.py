from enum import Enum

class TokenType(Enum):
    def __str__(self):
        return str(self.value)
    #eoF
    EOF =           0
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
    NUMERIC_LITERAL =      20

    #KeyWords
    AND =                  21
    OR =                   22
    NOT =                  23

    IF =                   24
    WHILE =                25

    #identifiers
    FUNCTION =             26
    VARIABLE =             27

keyword_lexemes = {'and':TokenType.AND, 'or':TokenType.OR, 'not':TokenType.NOT,
                   'if':TokenType.IF, 'while':TokenType.WHILE}

keyword_alphabet = '&|andnotorifwhile'

def is_identifer_character(char):
    if(char.isalpha() or char == '_' or char in '1234567890'):
        return True
    return False

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
        if(self.type == TokenType.STRING_LITERAL):
            return 'string: {}'.format(self.literal)
        elif(self.type == TokenType.NUMERIC_LITERAL):
            return 'numerical: {}'.format(self.literal)
        elif(self.type == TokenType.VARIABLE):
            return 'variable: {}'.format(self.lexeme)
        elif(self.type == TokenType.FUNCTION):
            return 'function: {}'.format(self.lexeme)
        else:
            return '{}'.format(self.type.name)
