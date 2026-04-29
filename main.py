import os
print(os.getcwd())

from lexer import Lexer

filename = "input.txt"

def read_source(path):
    for encoding in ("utf-8", "utf-8-sig", "utf-16"):
        try:
            with open(path, "r", encoding=encoding) as file:
                return file.read()
        except UnicodeError:
            continue
    with open(path, "r") as file:
        return file.read()


code = read_source(filename)

lexer = Lexer(code)
tokens = lexer.tokenize()

for token in tokens:
    print(token)