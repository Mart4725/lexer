import os
from lexer import Lexer

# carpeta donde están los tests
base_dir = os.path.dirname(__file__)
tests_dir = os.path.join(base_dir, "test_cases")  # crea esta carpeta

for filename in os.listdir(tests_dir):
    if filename.endswith(".txt"):
        filepath = os.path.join(tests_dir, filename)

        print(f"\n📄 Procesando: {filename}")
        print("-" * 40)

        with open(filepath, "r", encoding="utf-8") as file:
            code = file.read()

        lexer = Lexer(code)
        tokens = lexer.tokenize()

        for token in tokens:
            print(token)