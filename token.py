class Token:
    def __init__(self, type_, value, error=None, line=None, column=None):
        self.type = type_
        self.value = value
        self.error = error
        self.line = line
        self.column = column

    def __repr__(self):
        return f"{self.type:>8} | {self.value:>4} | {self.error}"