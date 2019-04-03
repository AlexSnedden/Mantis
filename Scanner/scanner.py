from Token import Token
from Token import TokenType
from Token import keyword_lexemes
from Token import keyword_alphabet
from Token import is_identifer_character
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

    def scan_literal(self):
        numerical_characters = ('0','1','2','3','4','5','6','7','8','9')
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
        #check if numerical literal
        elif(self.source[self.current] in numerical_characters):
            isFloat = False
            lit_start = self.current
            lit_end = lit_start + 1
            while(True):
                if(self.source[lit_end] in numerical_characters):
                    lit_end += 1
                    self.current += 1
                elif(self.source[lit_end] == '.'):
                    if(isFloat): MantisScanner.reportSyntaxError('multiple decimal points in numeric token', self.line, True)
                    isFloat = True
                    lit_end += 1
                    self.current += 1
                else:
                    self.current += 1
                    break
            val = float(self.source[lit_start:lit_end])
            self.tokens.append(Token(TokenType.NUMERIC_LITERAL, None, val, self.line))
            return True
        return False

    def scan_identifier(self):
        #check if function identifier (will have @ in front)
        type = None
        if(self.source[self.current] == '@'):
            type = TokenType.FUNCTION
        #check if variable identifier (will have _ in front)
        elif(self.source[self.current] == '_'):
            type = TokenType.VARIABLE
        if(type):
            self.current += 1
            id_start = self.current
            id_end = self.current
            while(is_identifer_character(self.source[self.current])):
                id_end += 1
                self.current += 1
            self.tokens.append(Token(type, self.source[id_start:id_end], None, self.line))
            return True
        else:
            return False

    def scan_keyword(self):
        #extract whole word
        start = self.current
        end = start
        while(self.source[end] in keyword_alphabet):
            end += 1
            self.current += 1
        if self.source[start:end] in keyword_lexemes:
            self.tokens.append(Token(keyword_lexemes[self.source[start:end]], self.source[start:end], None, self.line))
            return True
        MantisScanner.reportSyntaxError('Unidentified word \"{}\"'.format(self.source[start:end]), self.line, True)

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
            #check for double char tokens
            elif(character in double_char_tokens):
                self.double_char_token_handler(self.line, character)
            #check if string literal
            elif(not self.scan_literal()):
                #check if identifier
                if(not self.scan_identifier()):
                    #check if keyword
                    if(not self.scan_keyword()):
                        MantisScanner.reportSyntaxError('unidentified character \'{}\''.format(self.source[self.current]), self.line, True)

        self.tokens.append(Token(TokenType.EOF, '', None, self.line))
        return self.tokens



#pdb.set_trace()
m = MantisScanner()
for t in m.tokens_from('C:\\Users\\Alex\\Interpreter\\Scanner\\test.mantis'):
    print(str(t))
