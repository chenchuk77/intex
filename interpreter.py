
from token import Token
from settings import *

class Interpreter(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None

    def error(self):
        raise Exception('Error parsing input')

    def get_next_token(self):
        text = self.text

        if self.pos > len(text) - 1:
            return Token(EOF, None)

        # if its a space, move forward and read again
        current_char = text[self.pos]
        while current_char.isspace():
            self.pos += 1
            current_char = text[self.pos]

        if current_char == '+':
            token = Token(PLUS, current_char)
            self.pos += 1
            return token

        if current_char == '-':
            token = Token(MINUS, current_char)
            self.pos += 1
            return token

        # multidigit integer as string
        if current_char.isdigit():
            number_builder = ''
            while current_char.isdigit():
                number_builder += current_char
                print(number_builder)
                self.pos += 1
                current_char = text[self.pos]
            return Token(INTEGER, int(number_builder))

        self.error()

    def eat(self, token_type):
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        self.current_token = self.get_next_token()

        left = self.current_token
        self.eat(INTEGER)

        op = self.current_token
        if op.type == PLUS:
            self.eat(PLUS)
        if op.type == MINUS:
            self.eat(MINUS)

        right = self.current_token
        self.eat(INTEGER)

        if op.type == PLUS:
            result = left.value + right.value
            return result
        if op.type == MINUS:
            result = left.value - right.value
            return result

