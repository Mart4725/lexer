from token import Token
from rules import KEYWORDS, OPERATORS, DELIMITERS


class Lexer:
    def __init__(self, code):
        self.code = code
        self.pos = 0
        self.tokens = []
        self.line = 1
        self.column = 1

    def peek(self):
        if self.pos < len(self.code):
            return self.code[self.pos]
        return None

    def advance(self):
        if self.peek() == '\n':
            self.line += 1
            self.column = 1
        else:
            self.column += 1
        self.pos += 1

    def tokenize(self):
        while self.pos < len(self.code):
            current = self.peek()

            if current.isspace():
                self.handle_whitespace()

            elif current.isalpha() or current == '_':
                self.tokens.append(self.handle_identifier())

            elif current.isdigit():
                self.tokens.append(self.handle_number())

            elif current == '"':
                self.tokens.append(self.handle_string())

            else:
                self.tokens.append(self.handle_symbol())

        return self.tokens

    def handle_whitespace(self):
        if self.peek() == '\n':
            self.tokens.append(Token("NEWLINE", "\\n", None, self.line, self.column))
        self.advance()

    def handle_identifier(self):
        start = self.pos

        while self.peek() and (self.peek().isalnum() or self.peek() == '_'):
            self.advance()

        lexeme = self.code[start:self.pos]

        if lexeme in KEYWORDS:
            return Token(KEYWORDS[lexeme], lexeme)

        return Token("NAME", lexeme)

    def handle_number(self):
        start = self.pos
        has_dot = False

        while self.peek() and (self.peek().isdigit() or self.peek() == '.'):
            if self.peek() == '.':
                if has_dot:
                    break
                has_dot = True
            self.advance()

        # detectar error tipo 2bad
        if self.peek() and self.peek().isalpha():
            while self.peek() and (self.peek().isalnum() or self.peek() == '_'):
                self.advance()
            lexeme = self.code[start:self.pos]
            return Token("ERROR", lexeme, "Identificador inválido")

        lexeme = self.code[start:self.pos]
        return Token("NUMBER", lexeme)

    def handle_string(self):
        self.advance()  # saltar "

        start = self.pos

        while self.peek() and self.peek() != '"':
            self.advance()

        if self.peek() != '"':
            return Token("ERROR", None, "Cadena no terminada")

        lexeme = self.code[start:self.pos]
        self.advance()

        return Token("STRING", lexeme)

    def handle_symbol(self):
        # operadores de 2 caracteres
        if self.pos + 1 < len(self.code):
            two = self.code[self.pos:self.pos+2]
            if two in OPERATORS:
                self.pos += 2
                return Token(OPERATORS[two], two)

        current = self.peek()

        if current in OPERATORS:
            self.advance()
            return Token(OPERATORS[current], current)

        if current in DELIMITERS:
            self.advance()
            return Token(DELIMITERS[current], current)

        self.advance()
        return Token("ERROR", current, "Carácter inválido")