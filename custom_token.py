class Token:
    """Representa un token reconocido por el lexer."""
    
    def __init__(self, type_, value, error=None, line=None, column=None):
        self.type = type_        # Tipo del token
        self.value = value       # Valor literal
        self.error = error       # Mensaje de error (si aplica)
        self.line = line         # Linea en el codigo
        self.column = column     # Columna en el codigo

    def clean(self, v):
        """Formatea un valor para visualizacion."""
        if v is None:
            return "—"
        return str(v)

    def __repr__(self):
        """Retorna representacion legible del token."""
        return f"{self.type:>10} | {self.clean(self.value):>10} | {self.clean(self.error):>25} | {self.line}:{self.column}"