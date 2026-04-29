import os
print(os.getcwd())

from lexer import Lexer

filename = 'input.txt'

with open(filename, "r", encoding="utf-8") as file:
    code = file.read()

lexer = Lexer(code)
tokens = lexer.tokenize()

for token in tokens:
    print(token)