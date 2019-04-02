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
            ',': lambda token_list, line : token_list.append(Token(TokenType.COMMA, ',', None, line)),
            '.': lambda token_list, line : token_list.append(Token(TokenType.DOT, '.', None, line)),
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
        print('Sytax error on line {}: {}'.format(line, message))
        if(stop_run): exit()

    def double_char_token_handler(self, line, character):
        next_char = self.source[self.current+1]
        if(character == '!'):
            if(next_char == '='):
                self.tokens.append(Token(TokenType.NOT_EQUAL, '!=', None, line))
                self.current += 2
            else:
                MantisScanner.reportSyntaxError('stray \'!\' is not valid.', self.line, True)

    def tokens_from(self, file):
        with open(file) as f:
            self.source = f.read()
        while(self.current < len(self.source)):
            #check if newline
            if(self.source[self.current] == '\n'):
                self.current += 1
                self.line += 1
            else:
                # check for single character tokens
                if(self.source[self.current] in self.single_char_token_callbacks):
                    self.single_char_token_callbacks[self.source[self.current]](self.tokens, self.line)
                    self.current += 1
                if(self.source[self.current] == '!'):
                    self.double_char_token_handler(self.line, '!')
        self.tokens.append(Token(TokenType.EOF, '', None, self.line))
        return self.tokens



#pdb.set_trace()
m = MantisScanner()
for t in m.tokens_from('C:\\Users\\Alex\\Interpreter\\Scanner\\test.mantis'):
    print(str(t))
