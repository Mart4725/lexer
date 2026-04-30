import os
from lexer import Lexer

# carpeta donde están los tests

# elegir carpeta (basics o triton)
## NOTA ext se puede cambiar a cualquier archivo en especifico

# suit = "test_cases/basics"
# ext = ".txt"

# OR (Checar que solo un suit y ext esten activos)

suit = "test_cases/triton"
ext = ".triton" 


base_dir = os.path.dirname(__file__)
tests_dir = os.path.join(base_dir, suit)  # crea esta carpeta

for filename in os.listdir(tests_dir):
    if filename.endswith(ext):
        filepath = os.path.join(tests_dir, filename)

        print(f"\n📄 Procesando: {filename}")
        print("-" * 40)

        with open(filepath, "r", encoding="utf-8") as file:
            code = file.read()

        lexer = Lexer(code)
        tokens = lexer.tokenize()

        for token in tokens:
            print(token)