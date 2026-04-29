# Analizador léxico

Comprender la importancia del análisis léxico en el proceso de traducción de un lenguaje. 

## How it works

1. `main.py` lee el archivo `input.txt`.
2. `Lexer` recorre el texto carácter por carácter.
3. Según el carácter actual, crea tokens de palabras, números, cadenas, operadores o delimitadores.
4. Los espacios se ignoran y los saltos de línea se guardan como `NEWLINE`.

## How to use

1. Escribe tu código en `input.txt`.
2. Ejecuta `main.py`.
3. El programa imprime los tokens encontrados en la terminal.

## Example input

	def suma(a, b):
		return a + b

	x = 10
	y = 20
	resultado = suma(x, y)

	if resultado >= 30:
		print("mayor o igual")

## Example output

	DEF | def | None
	NAME | suma | None
	LPAREN | ( | None
	NAME | a | None
	COMMA | , | None
	NAME | b | None
	RPAREN | ) | None
	COLON | : | None
	NEWLINE | \n | None
	RETURN | return | None

## Notes

- Las palabras clave se definen en `rules.py`.
- Los valores de los tokens y los mensajes de error se definen en `custom_token.py`.
- El proyecto aún no gestiona tokens de sangría como `INDENT` y `DEDENT`.
