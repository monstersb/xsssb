from .token import Token, TokenType
from collections import deque

class Tokenizer(object):
    def __init__(self, input):
        self.input = input
        self.buffer = deque()
        self.read()
        self.last_token_value = ''
        self.last_token_type = TokenType.invalid

    def tokenize(self):
        while True:
            token = self.tokenize_one()
            if token.type != TokenType.space and token.type != TokenType.single_line_comment and token.type != TokenType.multi_line_comment:
                self.last_token_type = token.type
                #print token
                yield token
            if token.type == TokenType.terminator:
                break

    def tokenize_one(self):
        #print repr(self.char)
        if self.accept_space():
            return Token(TokenType.space, ' ')
        elif self.accept_identifier():
            if self.last_token_value in ['await', 'abstract', 'break', 'boolean', 'byte', 'case', 'catch', 'char', 'class', 'const', 'continue', 'debugger', 'default', 'delete', 'do', 'double', 'else', 'enum', 'export', 'extends', 'final', 'finally', 'float',  'for', 'function', 'goto', 'if', 'import', 'implements', 'in', 'instanceof', 'int', 'interface', 'let', 'long', 'native', 'new', 'null', 'of', 'package', 'private', 'protected', 'public', 'return', 'short', 'static', 'super', 'switch', 'synchronized','this', 'throw', 'throws', 'transient', 'try', 'typeof', 'var', 'void', 'volatile', 'while', 'with', 'yield']:
                return Token(getattr(TokenType, 'keyword_' + self.last_token_value), self.last_token_value)
            else:
                return Token(TokenType.identifier, self.last_token_value)
        elif self.accept_char('('):
            return Token(TokenType.left_parenthesis, '(')
        elif self.accept_char(')'):
            return Token(TokenType.right_parenthesis, ')')
        elif self.accept_char('['):
            return Token(TokenType.left_bracket, '[')
        elif self.accept_char(']'):
            return Token(TokenType.right_bracket, ']')
        elif self.accept_char('{'):
            return Token(TokenType.left_brace, '{')
        elif self.accept_char('}'):
            return Token(TokenType.right_brace, '}')
        elif self.accept_char(':'):
            return Token(TokenType.colon, ':')
        elif self.accept_char(';'):
            return Token(TokenType.semicolon, ';')
        elif self.accept_char(','):
            return Token(TokenType.comma, ',')
        elif self.accept_char('.'):
            return Token(TokenType.dot, '.')
        elif self.accept_char('?'):
            return Token(TokenType.ask, '?')
        elif self.accept_char('='):
            if self.accept_char('='):
                if self.accept_char('='):
                    return Token(TokenType.strict_equal, '===')
                else:
                    return Token(TokenType.equal, '==')
            else:
                return Token(TokenType.assignment, '=')
        elif self.accept_char('+'):
            if self.accept_char('+'):
                return Token(TokenType.increment, '++')
            elif self.accept_char('='):
                return Token(TokenType.addition_assignment, '+=')
            else:
                return Token(TokenType.addition, '+')
        elif self.accept_char('-'):
            if self.accept_char('-'):
                return Token(TokenType.decrement, '--')
            elif self.accept_char('='):
                return Token(TokenType.subtraction_assignment, '-=')
            else:
                return Token(TokenType.subtraction, '-')
        elif self.accept_char('*'):
            if self.accept_char('*'):
                if self.accept_char('='):
                    return Token(TokenType.exponentiation_assignment, '**=')
                else:
                    return Token(TokenType.exponentiation, '**')
            elif self.accept_char('='):
                return Token(TokenType.multiplication_assignment, '*=')
            else:
                return Token(TokenType.multiplication, '*')
        elif self.accept_char('/'):
            if self.accept_single_line_comment():
                return Token(TokenType.single_line_comment, self.last_token_value)
            elif self.accept_multi_line_comment():
                return Token(TokenType.multi_line_comment, self.last_token_value)
            elif self.last_token_type in [TokenType.addition, TokenType.addition_assignment, TokenType.ask, TokenType.assignment, TokenType.bitwise_and, TokenType.bitwise_and_assignment, TokenType.bitwise_not, TokenType.bitwise_not_assignment, TokenType.bitwise_or, TokenType.bitwise_or_assignment, TokenType.bitwise_xor, TokenType.bitwise_xor_assignment, TokenType.colon, TokenType.comma, TokenType.decrement, TokenType.division, TokenType.division_assignment, TokenType.equal, TokenType.exponentiation, TokenType.exponentiation_assignment, TokenType.greater_than, TokenType.greater_than_or_equal, TokenType.increment, TokenType.left_brace, TokenType.left_bracket, TokenType.left_parenthesis, TokenType.left_shift, TokenType.left_shift_assignment, TokenType.less_than, TokenType.less_than_or_equal, TokenType.endl, TokenType.logical_and, TokenType.logical_not, TokenType.logical_or, TokenType.multiplication, TokenType.multiplication_assignment, TokenType.not_equal, TokenType.remainder, TokenType.remainder_assignment, TokenType.right_shift, TokenType.right_shift_assignment, TokenType.semicolon, TokenType.single_line_comment, TokenType.strict_equal, TokenType.strict_not_equal, TokenType.subtraction, TokenType.subtraction_assignment, TokenType.unsigned_right_shift, TokenType.unsigned_right_shift_assignment, TokenType.keyword_return]:
                if self.accept_regexp():
                    return Token(TokenType.regexp, self.last_token_value)
            elif self.accept_char('='):
                return Token(TokenType.division_assignment, '/=')
            else:
                return Token(TokenType.division, '/')
        elif self.accept_char('%'):
            if self.accept_char('='):
                return Token(TokenType.remainder_assignment, '%=')
            else:
                return Token(TokenType.remainder, '%')
        elif self.accept_char('&'):
            if self.accept_char('&'):
                return Token(TokenType.logical_and, '&&')
            elif self.accept_char('='):
                return Token(TokenType.bitwise_and_assignment, '&=')
            else:
                return Token(TokenType.bitwise_and, '&')
        elif self.accept_char('|'):
            if self.accept_char('|'):
                return Token(TokenType.logical_or, '||')
            elif self.accept_char('='):
                return Token(TokenType.bitwise_or_assignment, '|=')
            else:
                return Token(TokenType.bitwise_or, '|')
        elif self.accept_char('^'):
            if self.accept_char('='):
                return Token(TokenType.bitwise_xor_assignment, '^=')
            else:
                return Token(TokenType.bitwise_xor, '^')
        elif self.accept_char('~'):
            if self.accept_char('='):
                return Token(TokenType.bitwise_not_assignment, '~=')
            else:
                return Token(TokenType.bitwise_not, '~')
        elif self.accept_char('!'):
            if self.accept_char('='):
                if self.accept_char('='):
                    return Token(TokenType.strict_not_equal, '!==')
                else:
                    return Token(TokenType.not_equal, '!=')
            else:
                return Token(TokenType.logical_not, '!')
        elif self.accept_char('<'):
            if self.accept_char('='):
                return Token(TokenType.less_than_or_equal, '<=')
            elif self.accept_char('<'):
                if self.accept_char('='):
                    return Token(TokenType.left_shift_assignment, '<<=')
                else:
                    return Token(TokenType.left_shift, '<<')
            else:
                return Token(TokenType.less_than, '<')
        elif self.accept_char('>'):
            if self.accept_char('='):
                return Token(TokenType.greater_than_or_equal, '>=')
            elif self.accept_char('>'):
                if self.accept_char('='):
                    return Token(TokenType.right_shift_assignment, '>>=')
                elif self.accept_char('>'):
                    if self.accept_char('='):
                        return Token(TokenType.unsigned_right_shift_assignment, '>>>=')
                    else:
                        return Token(TokenType.unsigned_right_shift, '>>>')
                else:
                    return Token(TokenType.right_shift, '>>')
            else:
                return Token(TokenType.greater_than, '>')
        elif self.accept_number():
            return Token(TokenType.number, self.last_token_value)
        elif self.accept_string():
            return Token(TokenType.string, self.last_token_value)
        elif self.accept_line_separator():
            return Token(TokenType.endl, '\n')
        elif self.accept_char(''):
            return Token(TokenType.terminator, '')

    def read(self):
        self.char = self.buffer.pop() if len(self.buffer) > 0 else self.input.read(1)
        self.eof = len(self.char) == 0

    def accept_char(self, c):
        if len(self.char) == 0:
            self.read()
        if c == '' and self.eof:
            return True, ''
        if self.eof == False and self.char in c:
            t = self.char
            self.char = ''
            return True, t
        else:
            return False

    def accept_until(self, c, allow_terminator=False):
        buf = ''
        while True:
            if len(self.char) == 0:
                self.read()
            if self.eof:
                if allow_terminator:
                    return True, buf
                else:
                    return False
            if self.char in c:
                return True, buf
            else:
                buf += self.char

    def push_buffer(self, s):
        if self.char != '':
            self.buffer.appendleft(self.char)
            self.char = ''
        for c in s:
            self.buffer.appendleft(c)

    def accept_space(self):
        buffer = ''
        while True:
            t = self.accept_char('\t\v\f ')
            if t:
                buffer += t[1]
            else:
                if len(buffer) > 0:
                    self.last_token_value = buffer
                    return True, buffer
                else:
                    return False

    def accept_line_separator(self):
        return self.accept_char('\n\r')

    def accept_single_line_comment(self):
        if self.accept_char('/') == False:
            return False
        buffer = '//'
        while True:
            self.read()
            if self.eof:
                self.last_token_value = buffer
                return True, buffer
            if self.char in '\r\n':
                self.last_token_value = buffer
                return True, buffer
            else:
                buffer += self.char

    def accept_multi_line_comment(self):
        if self.accept_char('*') == False:
            return False
        buffer = '/*'
        while True:
            self.read()
            if self.eof:
                return False
            if self.char == '*':
                buffer += self.char
                self.read()
                if self.eof:
                    return False
                if self.char == '/':
                    buffer += self.char
                    self.char = ''
                    self.last_token_value = buffer
                    return True, buffer
                else:
                    self.push_buffer('')
            else:
                buffer += self.char

    def accept_identifier(self):
        t = self.accept_char('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_$')
        if t:
            buffer = t[1]
            while True:
                t = self.accept_char('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_$')
                if t:
                    buffer += t[1]
                else:
                    break
            self.last_token_value = buffer
            return True, buffer
        else:
            return False

    def accept_number(self):
        buffer = ''
        t = self.accept_char('123456789')
        if t:
            buffer = t[1]
            while True:
                t = self.accept_char('123456789')
                if t:
                    buffer += t[1]
                else:
                    break
        elif self.accept_char('0'):
            buffer = '0'
            if self.accept_char('Xx'):
                buffer += 'x'
                while True:
                    t = self.accept_char('0123456789abcdefABCDEF')
                    if t:
                        buffer += t[1]
                    else:
                        if len(buffer) > 2:
                            self.last_token_value = buffer
                            return True, buffer
                        else:
                            return False
            elif self.accept_char('Oo'):
                buffer += 'o'
                while True:
                    t = self.accept_char('01234567')
                    if t:
                        buffer += t[1]
                    else:
                        if len(buffer) > 2:
                            self.last_token_value = buffer
                            return True, buffer
                        else:
                            return False
            elif self.accept_char('Bb'):
                buffer += 'b'
                while True:
                    t = self.accept_char('01')
                    if t:
                        buffer += t[1]
                    else:
                        if len(buffer) > 2:
                            self.last_token_value = buffer
                            return True, buffer
                        else:
                            return False
            else:
                pass
        elif self.accept_char('.'):
            self.push_buffer('.')
        else:
            return False
        if self.accept_char('.'):
            buffer += '.'
            while True:
                t = self.accept_char('0123456789')
                if t:
                    buffer += t[1]
                else:
                    break
            if buffer == '.':
                return False
        if self.accept_char('Ee'):
            buffer += 'e'
            t = self.accept_char('0123456789')
            if t is False:
                return False
            buffer += t[1]
            while True:
                t = self.accept_char('0123456789')
                if t:
                    buffer += t[1]
                else:
                    break
        self.last_token_value = buffer
        return True, buffer

    def accept_string(self):
        t = self.accept_char('"\'')
        if t is False:
            return False
        buffer = t[1]
        while True:
            self.read()
            if self.char == '\\':
                buffer += '\\'
                self.read()
                if self.char == 'x':
                    buffer += 'x'
                    self.read()
                    if self.char not in '0123456789abcdefABCDEF':
                        return False
                    buffer += self.char
                    self.read()
                    if self.char not in '0123456789abcdefABCDEF':
                        return False
                    buffer += self.char
                elif self.char == 'u':
                    buffer += 'u'
                    self.read()
                    if self.char not in '0123456789abcdefABCDEF':
                        return False
                    buffer += self.char
                    self.read()
                    if self.char not in '0123456789abcdefABCDEF':
                        return False
                    buffer += self.char
                    self.read()
                    if self.char not in '0123456789abcdefABCDEF':
                        return False
                    buffer += self.char
                    self.read()
                    if self.char not in '0123456789abcdefABCDEF':
                        return False
                    buffer += self.char
                else:
                    buffer += self.char
            elif self.char == buffer[0]:
                buffer += self.char
                self.char = ''
                #self.last_token_value = eval('u' + buffer)
                self.last_token_value = buffer
                return True, buffer
            else:
                buffer += self.char

    def accept_regexp(self):
        buffer = '/'
        par_count = 0
        has_bracket = False
        while True:
            self.read()
            buffer += self.char
            if self.char == '/':
                if par_count > 0 or has_bracket:
                    continue
                flag = 'gimy'
                while True:
                    self.read()
                    if self.char != '' and self.char in flag:
                        buffer += self.char
                        flag = flag.replace(self.char, '')
                    else:
                        self.push_buffer('')
                        return True, buffer
            elif self.char == '\\':
                self.read()
                if self.char == '':
                    return False
                buffer += self.char
            elif self.char == '(' and has_bracket == False:
                par_count += 1
            elif self.char == ')' and has_bracket == False:
                if par_count == 0:
                    return False
                else:
                    par_count -= 1
            elif self.char == '[':
                has_bracket = True
            elif self.char == ']':
                has_bracket = False
            elif self.char == '':
                return False
            else:
                pass

