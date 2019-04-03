from Token import Token
from Token import TokenType
import re
import pdb

class MantisScanner:
    source = ''
    tokens = []
    line = 1
    start = 0
    current = 0

    single_char_token_callbacks = {
            ',': lambda token_list, line: token_list.append(Token(TokenType.COMMA, ',', None, line)),
            '.': lambda token_list, line: token_list.append(Token(TokenType.DOT, '.', None, line)),
            '+': lambda token_list, line: token_list.append(Token(TokenType.PLUS, '+', None, line)),
            '-': lambda token_list, line: token_list.append(Token(TokenType.MINUS, '-', None, line)),
            '(': lambda token_list, line: token_list.append(Token(TokenType.LEFT_PAREN, '(', None, line)),
            ')': lambda token_list, line: token_list.append(Token(TokenType.RIGHT_PAREN, ')', None, line)),
            '{': lambda token_list, line: token_list.append(Token(TokenType.LEFT_BRACE, '{', None, line)),
            '}': lambda token_list, line: token_list.append(Token(TokenType.RIGHT_BRACE, '}', None, line)),
            '*': lambda token_list, line: token_list.append(Token(TokenType.STAR, '*', None, line)),
            ';': lambda token_list, line: token_list.append(Token(TokenType.SEMICOLON, ';', None, line))
    }

    @staticmethod
    def reportSyntaxError(message, line, stop_run):
        print('Syntax error on line {}: {}'.format(line, message))
        if(stop_run): exit()

    def double_char_token_handler(self, line, character):
        next_char = self.source[self.current+1]
        if(character == '!'):
            if(next_char == '='):
                self.tokens.append(Token(TokenType.NOT_EQUAL, '!=', None, line))
                self.current += 2
            else:
                MantisScanner.reportSyntaxError('stray \'!\' is not valid.', self.line, True)
        elif(character == '>'):
            if(next_char == '='):
                self.tokens.append(Token(TokenType.GREATER_EQUAL, '>=', None, line))
                self.current += 2
            else:
                self.tokens.append(Token(TokenType.GREATER, '>', None, line))
                self.current += 1
        elif(character == '<'):
            if(next_char == '='):
                self.tokens.append(Token(TokenType.LESS_EQUAL, '<=', None, line))
                self.current += 2
            else:
                self.tokens.append(Token(TokenType.LESS, '<', None, line))
                self.current += 1
        elif(character == '='):
            if(next_char == '='):
                self.tokens.append(Token(TokenType.EQUAL, '==', None, line))
                self.current += 2
            else:
                self.tokens.append(Token(TokenType.ASSIGN, '=', None, line))
                self.current += 1

    def scan_literal(self, line):
        #check if string literal
        if(self.source[self.current] == '\"'):
            self.current += 1
            string_start = self.current
            string_end = string_start
            while(self.source[string_end] != '\"'):
                string_end += 1
                self.current += 1
            self.current += 1
            self.tokens.append(Token(TokenType.STRING_LITERAL, None, self.source[string_start:string_end], self.line))
            return True

    def tokens_from(self, file):
        double_char_tokens = ('!', '>', '<', '=')
        with open(file) as f:
            self.source = f.read()
        while(self.current < len(self.source)):
            character = self.source[self.current]
            #check if newline
            if(character == '\n'):
                self.current += 1
                self.line += 1
            #check if space
            elif(character == ' '):
                self.current += 1
            #check for single character tokens
            elif(character in self.single_char_token_callbacks):
                self.single_char_token_callbacks[character](self.tokens, self.line)
                self.current += 1
            # check for double char tokens
            elif(character in double_char_tokens):
                self.double_char_token_handler(self.line, character)
            # check if string Literal
            elif(not self.scan_literal(self.line)):
                MantisScanner.reportSyntaxError('unidentified character \'{}\''.format(self.source[self.current]), self.line, True)
        self.tokens.append(Token(TokenType.EOF, '', None, self.line))
        return self.tokens



#pdb.set_trace()
m = MantisScanner()
for t in m.tokens_from('C:\\Users\\Alex\\Interpreter\\Scanner\\test.mantis'):
    print(str(t))
