def es_palindromo():
    palabra = input("Introduce una palabra: ")
    return palabra == palabra[::-1]

resultado = es_palindromo()
print(resultado)


