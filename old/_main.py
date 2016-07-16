import sys

from interpreter import Interpreter

from old.settings import *
from old.token import Token

print ('hello from python')
print(sys.version)

t1 = Token(INTEGER, 4)
t2 = Token(PLUS, '+')


def main():
    while True:
        try:
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()



