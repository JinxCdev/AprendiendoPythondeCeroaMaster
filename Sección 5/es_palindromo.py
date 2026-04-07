palabra = input("Ingrese una palabra: ")
palabra = palabra.lower()
palabra = palabra.replace(" ", "")
palabra_invertida = palabra[::-1]
if palabra == palabra_invertida:
    print(f"{palabra} es un palíndromo.")
else:
    print(f"{palabra} no es un palíndromo.")